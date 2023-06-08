from flask import render_template, jsonify, request, blueprints
from ..utils import db, plot

bp = blueprints.Blueprint('views', __name__)


@bp.route('/')
def hello_world():
    return 'Hello, World!'


@bp.route('/test_file_list')
@bp.route('/init')
def get_datafile_list():
    datafile_list = db.read_db(db.READ_DataFile_Request(all_flag=True))

    out_datafile_list = []
    for datafile in datafile_list:
        out_datafile_list.append({'id': datafile.id, 'filename': datafile.basename})

    return jsonify({'list': out_datafile_list})


@bp.route('/test_graph')
@bp.route('/graph')
def response_of_graph():
    datafile = db.read_db(db.READ_DataFile_Request(all_flag=False, id_list=['1']))[0]
    return plot.create_graph(datafile)


@bp.route('/v2/test_graph/')
def v2_response_of_graph():
    try:
        #id_list = request.GET.getlist('id')
        id_list = [1,2,3]
        datafile_list = db.read_db(db.READ_DataFile_Request(all_flag=False, id_list=id_list))

        htmls = [plot.create_graph(datafile) for datafile in datafile_list]
        return render_template('graphs.html', items=htmls)
    except Exception as e:
        print(e)
        return
