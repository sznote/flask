import MySQLdb

def connection():
	conn = MySQLdb.Connection(host="27.254.149.216",
								user = "flask",
								passwd = "flask",
								port = 3307,
								db = "pythonprogramming"
								)
	c = conn.cursor()
	return c, conn


