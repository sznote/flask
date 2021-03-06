
import unittest

from flask_testing import TestCase
from project import app, db
from flask_login import current_user
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
	
	#Ensure that the main page requires login
	def  test_main_route_requires_login(self):
		#tester = app.test_client(self)
		response  = self.client.get('/', follow_redirects = True)
		self.assertIn(b'Please log in to access this page.', response.data)

	#Ensure that posts  show up on  the main page
	def test_post_show_up_on_main_page(self):
		#tester = app.test_client(self)
		response  = self.client.post(
			'/login',
			 data=dict(username="admin",password="admin"),
			 follow_redirects = True
		)
		self.assertIn(b'This is a test. Only a test.', response.data)

class UsersViewsTests(BaseTestCase):
# # Ensure  that  the login  pages  loads  correctly.
	def test_login_page_loads(self):
		#tester = app.test_client(self)
		response  = self.client.get('/login', content_type='html/text')
		self.assertTrue(b'Please sign in' in response.data)



	

	# Ensure login  behaves  correctly  given the incorrect  credentials
	def test_incorrect_login(self):
		#tester = app.test_client(self)
		response  = self.client.post(
			'/login',
			 data=dict(username="hello",password="hello"),
			 follow_redirects = True
		)
		self.assertIn(b'Invalid credentials Plases try again', response.data)
	

	# Ensure login  behaves  correctly  given the correct  credentials
	def test_correct_login(self):
		with self.client:		
			#tester = app.test_client(self)
			response  = self.client.post(
				'/login',
				 data=dict(username="admin",password="admin"),
				 follow_redirects = True
			)
			self.assertIn(b'You are login Success!!', response.data)
			self.assertTrue(current_user.name == "admin")
			self.assertTrue(current_user.is_active())

	# # Ensure logout  behaves  correctly 
	def test_logout(self):
		with self.client:
			self.client.post(
				'/login', data=dict(username="admin",password="admin"), follow_redirects = True
			)		
			response = self.client.get('/logout', follow_redirects = True )
			self.assertIn(b'You were logged out', response.data)
			#self.assertFalse( current_user.is_active() )

	def test_logout_route_requires_login(self):
		response = self.client.get('/logout', follow_redirects=True)
		self.assertIn(b'Please log in to access this page', response.data)


	# Ensure user can register

	def test_user_registeration(self):
		with self.client:		
			#tester = app.test_client(self)
			response  = self.client.post(
				'/register/',
				 data=dict(username="somchai",email="somechai@gmail.com",  
				 	password="somchai", confirm="somchai"),
				 follow_redirects = True
			)
			self.assertIn(b'Welcome to Flask!', response.data)
			self.assertTrue(current_user.name == "somchai")
			self.assertTrue(current_user.is_active())


if __name__ == '__main__':
	unittest.main()