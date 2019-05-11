import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

user = os.environ.get('POSTGRES_USER')
passwd = os.environ.get('POSTGRES_PASSWORD')
host = os.environ.get('POSTGRES_DB')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@db:5432/jobs'.format(
        user=user,
        passwd=passwd,
        host=host)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Job(db.Model):
    id = db.Column('job_id', db.Integer, primary_key=True)
    job_title = db.Column(db.String(100))
    job_description = db.Column(db.String(1000))
    contact_email = db.Column(db.String(50))

    def __init__(self, job_title, job_description, contact_email):
        self.job_title = job_title
        self.job_description = job_description
        self.contact_email = contact_email


db.create_all()


@app.route('/create', methods=['POST'])
def create_job():
    job_data = request.json
    job = Job(**job_data)
    db.session.add(job)
    db.session.commit()


@app.route('/job/<job_id>', methods=['GET'])
def read_specific_job(job_id):
    job = Job.query.get(job_id)
    return jsonify({job_id: job})


@app.route('/jobs', methods=['GET'])
def read_all_jobs():
    jobs = Job.query.all()
    return jsonify({'results': jobs})


@app.route('/search', methods=['POST'])
def search_job():
    job_query = request.json
    job_results = Job.query.filter_by(**job_query)
    return jsonify(job_results.data)


@app.route('/delete_job/<job_id>', methods=['GET'])
def delete_job(job_id):
    job = Job.query.get(job_id)
    db.session.delete(job)
    db.session.commit()

    return jsonify({'Deleted': job})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
