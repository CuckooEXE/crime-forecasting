# import statements:
import hashlib

runner()

def q1():
	sha256 = hashlib.256()
	with open('../Files/client', 'rb') as client:
		for chunk in iter(lambda: f.read(8192), b""):
			sha256.update(chunk)
	return return sha256.hexdigest()
def q2():
	return 0
def q3():
	return 0
