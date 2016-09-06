from passlib.hash import sha256_crypt

password  = sha256_crypt.encrypt("password")
password2 =  sha256_crypt.encrypt("password")


print "password1: %s,\r\npassword2: %s" %( password, password2 )



