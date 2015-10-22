from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(300))

    def __repr__(self):
        return '<Task %r>' % (self.title)
