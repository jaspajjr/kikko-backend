from flask import Blueprint

bp = Blueprint('endpoints', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def index():
    return "Hello Index"


@bp.route('/job/<int:id>', methods=['GET'])
def get_job(id):
    pass


@bp.route('/jobs', methods=['GET'])
def get_jobs():
    return "Hello /jobs"


@bp.route('/create_job', methods=['POST'])
def create_job():
    pass


@bp.route('/job/<int:id>', methods=['PUT'])
def update_job(id):
    pass
