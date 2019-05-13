from flask import Blueprint, jsonify, request
from kikko import db
from .models import Job, JobSchema

bp = Blueprint('endpoints', __name__, url_prefix='/')

job_schema = JobSchema()
jobs_schema = JobSchema(many=True)


@bp.route('/', methods=['GET'])
def index():
    return "Hello Index"


@bp.route('/job/<int:id>', methods=['GET'])
def get_job(id):
    result = Job.query.filter_by(id=id).first()
    job = job_schema.dump(result)
    job_id = 'job_{id_val}'.format(id_val=id)

    return jsonify({job_id: job})


@bp.route('/jobs', methods=['GET'])
def get_jobs():
    result = Job.query.all()
    jobs = jobs_schema.dump(result)
    return jsonify(jobs=jobs)


@bp.route('/create_job', methods=['POST'])
def create_job():
    request_json = request.json
    job_description_data = request_json.get('job', 0)
    if job_description_data == 0:
        print(job_description_data)
        return jsonify("Incorrect data"), 400
    job = Job(**job_description_data)
    db.session.add(job)
    db.session.commit()

    return "Job created"


@bp.route('/job/<int:id>', methods=['PUT'])
def update_job(id):
    pass
