from passlib.hash import sha256_crypt

password  = sha256_crypt.encrypt("password")
password2 =  sha256_crypt.encrypt("password")


print "password1: %s,\r\npassword2: %s" %( password, password2 )


print(sha256_crypt.verify("password", password))

#if user is not None and bcrypt.check_password_hash(user.password,request.form['password'] ):

# if password == password2:
# 	print "yay"
# else:
# 	print "fail"



