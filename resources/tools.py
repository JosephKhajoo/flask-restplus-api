from . import db
from resources.models import UserModel, PostModel
import sqlalchemy


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
	get_and_add_user(users)


def add_new_post(data):
	new_post = PostModel(
		id=data["id"],
		title=data["title"],
		content=data["content"],
		user_id=data["user_id"]
	)

	db.session.add(new_post)
	db.session.commit()
	
	posts = PostModel.query.all()
	get_and_add_post(posts)

def get_and_add_post(objects):
	all_posts = []
	for obj in objects:
		new_data = {
			"id" : obj.id,
			"title" : obj.title,
			"content" : obj.content,
			"date_posted" : obj.date_posted,
			"user_id" : obj.user_id
		}

		if not new_data in all_posts:
			all_posts.append(new_data)

	return all_posts


def get_and_add_user(objects):
	all_users = []
	for obj in objects:
		new_data = {
			"id" : obj.id,
			"name" : obj.name,
			"username" : obj.username,
			"password" : obj.password
		}

		if not new_data in all_users:
			all_users.append(new_data)

	return all_users