class Dummy:
	def __init__(self, name):
		self.name = name

	def __call__(self, value):
		return value ** 2

	def __str__(self):
		return self.name

if __name__ == '__main__':
	d = Dummy('ciao')
	print(d)
	print(d(6))