class Dog(object):
	dogs = []

	def __init__(self,name):
		self.name = name
		self.dogs.append(self)

	@classmethod
	def num_dogs(cls):
		return len(cls.dogs)

	@staticmethod
	def bark(n):
		"""barks n times"""
		for _ in range(n):
			print("Bark!")





Dog.bark(5)

# dog1 = Dog("Spayk")
# dog2 = Dog("Jemy")
# print(Dog.dogs)
# print(Dog.num_dogs())



