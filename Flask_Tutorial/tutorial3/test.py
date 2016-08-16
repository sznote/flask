from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
	def test_index(self):
		tester = app.test_client(self)
		response  = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	# Ensure  that  the login  pages  loads  correctly.
	def test_login_page_loads(self):
		tester = app.test_client(self)
		response  = tester.get('/login', content_type='html/text')
		self.assertTrue(b'Please sign in' in response.data)

	# Ensure login  behaves  correctly  given the correct  credentials

	def test_correct_login(self):
		tester = app.test_client(self)
		response  = tester.post(
			'/login',
			 data=dict(username="admin",password="admin"),
			 follow_redirects = True
		)
		self.assertIn(b'You are login Success!!', response.data)
	# Ensure login  behaves  correctly  given the incorrect  credentials
	def test_incorrect_login(self):
		tester = app.test_client(self)
		response  = tester.post(
			'/login',
			 data=dict(username="hello",password="hello"),
			 follow_redirects = True
		)
		self.assertIn(b'Invalid credentials Plases try again', response.data)
	
	# Ensure logout  behaves  correctly 
	def test_logout(self):
		
		tester = app.test_client(self)
		response  = tester.post(
			'/login',
			 data=dict(username="admin",password="admin"),
			 follow_redirects = True
		)
		
		response = tester.get('/logout', follow_redirects = True )
		self.assertIn(b'You ware just logged out!!', response.data)

	#Ensure that the main page requires login
	def  test_main_route_requires_login(self):
		tester = app.test_client(self)
		response  = tester.get('/', follow_redirects = True)
		self.assertIn(b'You need to login  first', response.data)

	#Ensure that posts  show up on  the main page
	def test_post_show_up(self):
		tester = app.test_client(self)
		response  = tester.post(
			'/login',
			 data=dict(username="admin",password="admin"),
			 follow_redirects = True
		)
		self.assertIn(b'm good', response.data)



if __name__ == '__main__':
	unittest.main()