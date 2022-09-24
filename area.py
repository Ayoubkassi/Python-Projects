class Point(object):
	def __init__(self,x=0,y=0):
		self.x = x
		self.y = y 

	def set_x(self,x):
		self.x = x 

	def set_y(self,y):
		self.y = y 

	def get_x(slef):
		return self.x 

	def get_y(self):
		return self.y 

	def printCodinate(self):
		print("x -> ",x," | y -> ",y)

	def calculArea(self,Point):
		width  = abs(self.x - Point.x)
		height = abs(self.y - Point.y)
		return width * height



a = Point()
b = Point(2,2)
print(a.calculArea(b))

# the next problem is to calculate the area between two rectangles

