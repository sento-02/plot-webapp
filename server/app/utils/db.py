import sqlite3
from sqlite3 import Error
import os
import hashlib

# -------------------------------------------------
# クラス

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
        print(self.id, self.basename, self.path,
              self.graph_png_path, self.graph_html_path)


class GraphFile:
    def __init__(self, hash, id_list, path=None):
        self.hash = hash
        self.id_list = id_list
        self.path = path


# データファイルリクエストクラス
# mode="READ" or "WRITE",
# READの場合はid_listかall_flagを指定
class READ_DataFile_Request:
    def __init__(self, all_flag=False, id_list=None):
        self.mode = "READ_DATAFILE"
        self.all_flag = all_flag
        self.id_list = id_list
        if self.all_flag == False and id_list == None:
            raise ValueError('id_list or all_flag must be specified.')

    def __call__(self, cursor):
        if self.all_flag:
            cursor.execute("SELECT id, basename, path FROM datafile")
        else:
            cursor.execute("SELECT id, basename, path FROM datafile WHERE id IN ({})".format(
                ','.join('?'*len(self.id_list))), self.id_list)
        rows = cursor.fetchall()
        datafile_list = []
        for row in rows:
            id, basename, path = row
            datafile = DataFile(id, basename, path)
            datafile_list.append(datafile)
        return datafile_list


class READ_Graph_Request:
    def __init__(self, graph_hash):
        self.mode = "READ_GRAPH"
        self.graph_hash = graph_hash

    def __call__(self, cursor):
        cursor.execute("SELECT * FROM graph WHERE hash=?", (self.graph_hash,))
        row = cursor.fetchone()
        if row is None:
            return None
        else:
            hash, id_list_str, path = row
            id_list = list(map(int, id_list_str.split()))
            return GraphFile(hash, id_list, path)


class WRITE_Graph_Request:
    def __init__(self, id_list):
        self.mode = "WRITE_GRAPH"
        self.id_list = id_list
        self.id_list_str = ' '.join(map(str, sorted(self.id_list)))
        self.hash = None
        self.path = None

    def __call__(self, cursor):
        # id_listをソートしてASH-256でハッシュ化
        salt = 'salt0910'
        hash = hashlib.sha1(self.id_list_str.encode(
            'utf-8') + salt.encode('utf-8')).hexdigest()
        row = cursor.execute(
            "SELECT * FROM graph WHERE hash=?", (hash,)).fetchone()
        if row is None:
            cursor.execute("INSERT INTO graph (hash, id, path) VALUES (?, ?, ?)",
                           (hash, self.id_list_str, "None"))
        self.hash = hash
        return self


# -------------------------------------------------
# モジュール


# 情報をDBとやりとり
def request_db(db_request):
    conn = None

    # Create a database connection to a SQLite database
    conn = sqlite3.connect('data/db.sqlite')
    c = conn.cursor()
    contents = db_request(c)
    conn.commit()
    conn.close()
    return contents


def init_db():
    conn = None

    # Create a database connection to a SQLite database
    conn = sqlite3.connect('data/db.sqlite')
    c = conn.cursor()

    # テーブルが既に存在していれば削除
    c.execute("DROP TABLE IF EXISTS datafile")

    # datafileテーブルを作成
    c.execute('''CREATE TABLE datafile
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                basename TEXT NOT NULL,
                path TEXT)''')

    # data/ディレクトリ内のCSVファイルを検索してデータを挿入
    data_dir = 'data/csv'
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            basename = os.path.splitext(filename)[0]
            path = os.path.join(data_dir, filename)
            c.execute(
                "INSERT INTO datafile (basename, path) VALUES (?, ?)", (basename, path))

    # テーブルが既に存在していれば削除
    c.execute("DROP TABLE IF EXISTS graph")

    # graphテーブルを作成
    # hash:文字列、id:整数のリスト、path:グラフ画像のパス
    c.execute('''CREATE TABLE graph
                (hash TEXT PRIMARY KEY,
                id TEXT NOT NULL,
                path TEXT)''')

    # 変更をコミットする
    conn.commit()

    """
    # 結果を表示
    c.execute("SELECT * FROM datafile")
    rows = c.fetchall()
    for row in rows:
        print(row)
    """

    conn.close()


if __name__ == '__main__':
    init_db()
    datafile_list = request_db(READ_DataFile_Request(all_flag=True))
    for datafile in datafile_list:
        datafile.print()
