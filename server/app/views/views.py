from flask import jsonify, request, blueprints, current_app
from ..utils import db, plot


bp = blueprints.Blueprint('views', __name__)


@bp.route('/')
@bp.route('/test_file_list')
@bp.route('/init')
def get_datafile_list():
    datafile_list = db.request_db(db.READ_DataFile_Request(all_flag=True))
    out_datafile_list = []
    for datafile in datafile_list:
        out_datafile_list.append(
            {'id': datafile.id, 'filename': datafile.basename})

    return jsonify({'list': out_datafile_list})


@bp.route('/v1/test_graph')
@bp.route('/graph')
def response_of_graph():
    datafile = db.request_db(db.READ_DataFile_Request(
        all_flag=False, id_list=['1']))[0]
    return plot.create_graph(datafile)


@bp.route('/test_graph', methods=['POST'])
@bp.route('/v2/test_graph', methods=['POST'])
def v2_response_of_graph():
    current_app.logger.info(request.headers)
    current_app.logger.info(request.data)
    current_app.logger.info(request.json)
    id_list = request.json['id']
    graph = db.request_db(db.WRITE_Graph_Request(id_list))
    res = jsonify({"url": "src_graph/" + graph.hash})
    current_app.logger.info(res)
    return res


@bp.route('/v3/test_graph')
def v3_response_of_graph():
    id_list = [1, 3]
    graph = db.request_db(db.WRITE_Graph_Request(id_list=id_list))
    return jsonify({"url": "src_graph/" + graph.hash})


@bp.route('/src_graph/<hash>')
def src_graph(hash):
    graph = db.request_db(db.READ_Graph_Request(hash))
    datafile_list = db.request_db(db.READ_DataFile_Request(
        all_flag=False, id_list=graph.id_list))
    return plot.create_graph(datafile_list)


@app.after_request
def compress_response(response):
    accept_encoding = request.headers.get('Accept-Encoding', '')

    if 'gzip' not in accept_encoding.lower():
        return response

    response.direct_passthrough = False

    if response.status_code < 200 or response.status_code >= 300 or 'Content-Encoding' in response.headers:
        return response

    gzip_buffer = io.BytesIO()
    gzip_file = gzip.GzipFile(mode='wb', compresslevel=5, fileobj=gzip_buffer)
    gzip_file.write(response.get_data())
    gzip_file.close()

    compressed_response = gzip_buffer.getvalue()

    response.set_data(compressed_response)
    response.headers['Content-Encoding'] = 'gzip'
    response.headers['Content-Length'] = len(compressed_response)

    return response
