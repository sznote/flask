
import unittest

from flask_testing import TestCase
from project import app, db
from project.models import BlogPost, User


class  BaseTestCase(TestCase):
	''' A base  test case. '''

	def create_app(self):
		app.config.from_object('config.TestConfig')
		return app

	def setUp(self):
		db.create_all()
		db.session.add(BlogPost("Test post", "This is a test. Only a test."))
		db.session.add(User("admin", "ad@min.com", "admin"))
		db.session.commit()

	def tearDown(self):
	  	db.session.remove()
	  	db.drop_all()
		


#class FlaskTestCase(unittest.TestCase):
class FlaskTestCase(BaseTestCase):
	def test_index(self):
		#tester = app.test_client(self)
		response  = self.client.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	# # Ensure  that  the login  pages  loads  correctly.
	def test_login_page_loads(self):
		#tester = app.test_client(self)
		response  = self.client.get('/login', content_type='html/text')
		self.assertTrue(b'Please sign in' in response.data)

	# # Ensure login  behaves  correctly  given the correct  credentials

	def test_correct_login(self):
		#tester = app.test_client(self)
		response  = self.client.post(
			'/login',
			 data=dict(username="admin",password="admin"),
			 follow_redirects = True
		)
		self.assertIn(b'You are login Success!!', response.data)


	# Ensure login  behaves  correctly  given the incorrect  credentials
	def test_incorrect_login(self):
		#tester = app.test_client(self)
		response  = self.client.post(
			'/login',
			 data=dict(username="hello",password="hello"),
			 follow_redirects = True
		)
		self.assertIn(b'Invalid credentials Plases try again', response.data)
	

	# # Ensure logout  behaves  correctly 
	def test_logout(self):
		
		#tester = app.test_client(self)
		#response  = self.client.post(
		self.client.post(
			'/login',
			 data=dict(username="admin", password="admin"),
			 follow_redirects = True
		)		
		response = self.client.get('/logout', follow_redirects = True )
		self.assertIn(b'You ware just logged out!!', response.data)


	#Ensure that the main page requires login
	def  test_main_route_requires_login(self):
		#tester = app.test_client(self)
		response  = self.client.get('/', follow_redirects = True)
		self.assertIn(b'You need to login  first', response.data)


	def test_logout_route_requires_login(self):
		response = self.client.get('/logout', follow_redirects=True)
		self.assertIn(b'You need to login first.', response.data)


	#Ensure that posts  show up on  the main page
	def test_post_show_up_on_main_page(self):
		#tester = app.test_client(self)
		response  = self.client.post(
			'/login',
			 data=dict(username="admin",password="admin"),
			 follow_redirects = True
		)
		self.assertIn(b'This is a test. Only a test.', response.data)


if __name__ == '__main__':
	unittest.main()