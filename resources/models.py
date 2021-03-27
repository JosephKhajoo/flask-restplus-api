from . import db
from datetime import datetime

class UserModel(db.Model):
	id = db.Column(db.Integer, primary_key=True, unique=True)
	name = db.Column(db.String(120), nullable=False)
	username = db.Column(db.String(60), nullable=False, unique=True, primary_key=True)
	password = db.Column(db.String(120), nullable=False)

	posts = db.relationship('PostModel', backref='author', lazy=True)

	def __repr__(self):
		return f"User('{self.name}', '{self.username}', '{self.password}')"


class PostModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user_model.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"