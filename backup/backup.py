from flask_restplus import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# from models import UserModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api = Api(app)
ns = api.namespace("users", description="The users that are currently available")

user_field = api.model('User', {
	"id" : fields.Integer(0),
	"name" : fields.String("Name"),
	"username" : fields.String("Username"),
	"password" : fields.String("Password"),
})

# user = {"id" : 1, "name" : "Joseph", "username" : "josephkhajo", "password" : "Jj123456"}
# users.append(user)

db = SQLAlchemy(app)

class UserModel(db.Model):
	id = db.Column(db.Integer, primary_key=True, unique=True)
	name = db.Column(db.String(120), nullable=False)
	username = db.Column(db.String(60), nullable=False, unique=True, primary_key=True)
	password = db.Column(db.String(120), nullable=False)

	def __repr__(self):
		return f"User('{self.name}', '{self.username}', '{self.password}')"


all_users = []


def add_new_user(data):
	new_user = UserModel(
		id=data["id"],
		name=data["name"],
		username=data["username"],
		password=data["password"]
	)

	db.session.add(new_user)
	db.session.commit()
	
	users = UserModel.query.all()
	get_and_add_data(users)


def get_and_add_data(objects):
	for obj in objects:
		new_data = {
			"id" : obj.id,
			"name" : obj.name,
			"username" : obj.username,
			"password" : obj.password
		}

		if not new_data in all_users:
			all_users.append(new_data)


@ns.route('/')
class User(Resource):

	@api.marshal_with(user_field)
	def get(self):
		"""
		Returns the list of users that are currently available
		"""

		queried_users = UserModel.query.all()
		get_and_add_data(queried_users)

		return all_users

	@api.expect(user_field)
	def post(self):
		"""
		Creates a new user
		"""

		data = api.payload
		add_new_user(data)

		return {"message" : "New user created"}, 201


if __name__ == '__main__':
	app.run(debug=True)