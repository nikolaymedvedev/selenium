class Singltone(object):

	def __new__(cls):
		if hasattr(Singltone, "text") == False:
				cls.text = super().__new__(cls)
		return cls.text

a = Singltone()
b = Singltone()
print(a)
print(b)