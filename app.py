from flask_restplus import Resource, fields
from resources import app, api
import sqlalchemy
from resources.tools import *
from resources.models import UserModel, PostModel


users_ns = api.namespace("users", description="The users that are currently available.")
posts_ns = api.namespace("posts", description="All of the posts that are currently available.")


user_field = api.model('User', {
	"id" : fields.Integer(),
	"name" : fields.String("Name"),
	"username" : fields.String("Username"),
	"password" : fields.String("Password"),
})

post_field = api.model('Post', {
	"id" : fields.Integer(0),
	"title" : fields.String("title"),
	"content" : fields.String("content"),
	"user_id" : fields.Integer(0),
})


@users_ns.route('/')
class User(Resource):

	@api.marshal_with(user_field)
	def get(self):
		"""
		Returns the list of users that are currently available
		"""

		queried_users = UserModel.query.all()
		all_users = get_and_add_user(queried_users)

		return all_users

	@api.expect(user_field)
	def post(self):
		"""
		Creates a new user
		"""

		data = api.payload	
		resp = add_new_user(data)

		return {"message" : "New user created"}, 201



@posts_ns.route('/')
class Post(Resource):
	
	@api.marshal_with(post_field)
	def get(self):
		queried_posts = PostModel.query.all()
		all_posts = get_and_add_post(queried_posts)
		return all_posts

	@api.expect(post_field)
	def post(self):
		data = api.payload
		add_new_post(data)

		return {"message" : "New post created succesfully"}, 201

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)