from typing import Any
from flask import Flask, jsonify, render_template
import plot

import mydb

app = Flask(__name__)

# エンドポイント
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/file_list')
def get_datafile_list():
    datafile_list = mydb.read_db(mydb.READ_DataFile_Request(all_flag=True))

    out_datafile_list = []
    for datafile in datafile_list:
        out_datafile_list.append({'id': datafile.id, 'filename': datafile.basename})

    return jsonify({'datafile_list': out_datafile_list})


@app.route('/graph')
def read_alldatafile_list():
    graph_html = plot.create_graph()
    return render_template('graph.html', graph_html=graph_html)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False, port=80)