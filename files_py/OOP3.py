
#class Square():
#	square_list = []
#	def __init__(self, a):
#		self.a = a
#		self.square_list.append(self.a)
#		return "{} на {} на {} на {}".format(self.a, self.a, self.a, self.a)

#-1----------------------------------
class Shape():
	def what_i_am(self):
		print("I'm a shape")

class Square(Shape):
	square_list = []

	def __init__(self, n, a):
		self.name = n
		self.a = a
		self.square_list.append(self)

	def what_i_am(self):
		super().what_i_am()
		print("I'm a square")	

	def calculate_perimeter(self):
		return self.a * 4
	def change_size(self, n):
		self.a += n
	def __repr__(self):
		return "{} на {} на {} на {}".format(self.a, self.a, self.a, self.a)

	def sravn(self, obj1, obj2):
		return obj1 is obj2


square = Square("Square", 4)
square2 = square

square3 = Square("Square", 10)

#square2 = Square("Square", 5)

#print(Square.square_list)
#print(Square.square_list)

print(square)
print(square.sravn(square, square2))
print(square.sravn(square, square3))


