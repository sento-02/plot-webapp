from typing import Any
from flask import Flask, jsonify, render_template
import plot

import mydb

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test_file_list')
@app.route('/alldatafile_list')
@app.route('/init')
def get_datafile_list():
    datafile_list = mydb.read_db(mydb.READ_DataFile_Request(all_flag=True))

    out_datafile_list = []
    for datafile in datafile_list:
        out_datafile_list.append({'id': datafile.id, 'filename': datafile.basename})

    return jsonify({'list': out_datafile_list})


@app.route('/test_graph')
@app.route('/graph')
def response_of_graph():
    datafile = mydb.read_db(mydb.READ_DataFile_Request(all_flag=False, id_list=['1']))[0]
    return plot.create_graph(datafile)


@app.route('/v2/test_graph/')
def v2_response_of_graph(request: Any):
    try:
        id_list = request.GET.getlist('id')
        datafiles = mydb.read_db(mydb.READ_DataFile_Request(all_flag=False, id_list=id_list))

        htmls = [plot.create_graph(datafile) for datafile in datafiles]
        return render_template('graphs.html', items=htmls)
    except Exception as e:
        print(e)
        return



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False, port=80)