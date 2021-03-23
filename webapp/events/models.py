from webapp.db import db


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    category = db.Column(db.String)
    status = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    location = db.Column(db.String)
    note = db.Column(db.String)
    info = db.Column(db.Text)

    def __repr__(self):
        return '<Event {} {}>'.format(self.title, self.url)
