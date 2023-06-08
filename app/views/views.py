from flask import render_template, jsonify, request, blueprints
from ..utils import db, plot



bp = blueprints.Blueprint('views', __name__)


@bp.route('/')
@bp.route('/test_file_list')
@bp.route('/init')
def get_datafile_list():
    datafile_list = db.request_db(db.READ_DataFile_Request(all_flag=True))
    out_datafile_list = []
    for datafile in datafile_list:
        out_datafile_list.append({'id': datafile.id, 'filename': datafile.basename})

    return jsonify({'list': out_datafile_list})


@bp.route('/v1/test_graph')
@bp.route('/graph')
def response_of_graph():
    datafile = db.request_db(db.READ_DataFile_Request(all_flag=False, id_list=['1']))[0]
    return plot.create_graph(datafile)

@bp.route('/test_graph')
@bp.route('/v2/test_graph')
def v2_response_of_graph():
    try:
        id_list = request.GET.getlist('id')
        graph = db.request_db(db.WRITE_Graph_Request(id_list))
        return graph.hash
    except Exception as e:
        return str(e)


@bp.route('/v3/test_graph')
def v3_response_of_graph():
    id_list = [1,3]
    graph = db.request_db(db.WRITE_Graph_Request(id_list = id_list))
    return "src_graph/" + graph.hash


@bp.route('/src_graph/<hash>')
def src_graph(hash):
    graph = db.request_db(db.READ_Graph_Request(hash))
    datafile_list = db.request_db(db.READ_DataFile_Request(all_flag=False, id_list=graph.id_list))
    return plot.create_graph(datafile_list)
