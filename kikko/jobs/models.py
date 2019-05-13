from kikko import db
from marshmallow import Schema, fields


class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    contact_email = db.Column(db.String)
    password = db.Column(db.String)
    company_name = db.Column(db.String)
    job_title = db.Column(db.String)
    job_description = db.Column(db.String)
    location = db.Column(db.String)
    salary_min = db.Column(db.Integer)
    salary_max = db.Column(db.Integer)

    def __init__(self, ids, contact_email, password, company_name, job_title,
                 job_description, location, salary_min, salary_max):
        self.id = ids
        self.contact_email = contact_email
        self.password = password
        self.company_name = company_name
        self.job_title = job_title
        self.job_description = location
        self.salary_min = salary_min
        self.salary_max = salary_max


class JobSchema(Schema):
    id = fields.Int(dump_only=True)
    contact_email = fields.Str()
    password = fields.Str()
    company_name = fields.Str()
    job_title = fields.Str()
    job_description = fields.Str()
    location = fields.Str()
    salary_min = fields.Str()
    salary_max = fields.Str()
