import sqlite3
from sqlite3 import Error
import os

# dataファイル情報クラス
class DataFile:
    def __init__(self, id, basename, path=None):
        self.id = id
        self.basename = basename
        self.path = path
        self.graph_png_path = None
        self.graph_html_path = None

    def __call__(self, datafile_json):
        try:
            self.id = datafile_json['id']
            self.basename = datafile_json['basename']
            self.path = datafile_json['path']
        except KeyError as e:
            print(e)

        return self
    
    def print(self):
        print(self.id, self.basename, self.path, self.graph_png_path, self.graph_html_path)


# データファイルリクエストクラス
# mode="READ" or "WRITE", 
# READの場合はid_listかall_flagを指定
class READ_DataFile_Request:
    def __init__(self, all_flag=False, id_list=None):
        self.mode = "READ"
        self.all_flag = all_flag
        self.id_list = id_list
        if self.all_flag == False and id_list == None:
            raise ValueError('id_list or all_flag must be specified.')

class DataFile_Request:
    def __init__(self, mode, condition):
        self.mode = mode
        self.condition = condition



#-------------------------------------------------
# モジュール


# データファイル情報をDBから取得
def read_db(read_datafile_request):
    conn = None
    datafile_list = []
    try:
        conn = sqlite3.connect('data/db.sqlite')  # Create a database connection to a SQLite database
        c = conn.cursor()
        if read_datafile_request.all_flag:
            c.execute("SELECT id, basename, path FROM datafile")
        else:
            id_list = read_datafile_request.id_list
            c.execute("SELECT id, basename, path FROM datafile WHERE id IN ({})".format(','.join('?'*len(id_list))), id_list)
        rows = c.fetchall()

        # 取得した結果を形式変換
        for row in rows:
            id, basename, path = row
            datafile = DataFile(id, basename, path)
            datafile_list.append(datafile)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return datafile_list


def init_db():
    conn = None
    try:
        conn = sqlite3.connect('data/db.sqlite')  # Create a database connection to a SQLite database
        c = conn.cursor()
        
        # テーブルが既に存在していれば削除
        c.execute("DROP TABLE IF EXISTS datafile")
        
        # datafileテーブルを作成
        c.execute('''CREATE TABLE datafile
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    basename TEXT NOT NULL,
                    path TEXT NOT NULL)''')

        # data/ディレクトリ内のCSVファイルを検索してデータを挿入
        data_dir = 'data/csv'
        for filename in os.listdir(data_dir):
            if filename.endswith('.csv'):
                basename = os.path.splitext(filename)[0]
                path = os.path.join(data_dir, filename)
                c.execute("INSERT INTO datafile (basename, path) VALUES (?, ?)", (basename, path))

        # 変更をコミットする
        conn.commit()

        """
        # 結果を表示
        c.execute("SELECT * FROM datafile")
        rows = c.fetchall()
        for row in rows:
            print(row)
        """

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    init_db()
    datafile_list = read_db(READ_DataFile_Request(all_flag=True))
    for datafile in datafile_list:
        datafile.print()