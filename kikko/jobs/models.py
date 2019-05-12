from kikko import db


class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, ids, name):
        self.id = ids
        self.name = name
