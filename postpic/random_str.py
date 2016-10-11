import random
import string

def random_generator(size=11, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))
