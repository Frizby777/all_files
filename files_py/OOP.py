import math
#-Парадигмы программирования

#-1--------------------------------------------------
class Apple():
	def __init__(self, c, m, s, r):
		self.colour = c
		self.mass = m
		self.sort = s
		self.rot = r

appl = Apple("green", 54, "antonovka", 20)
print("\nInformation of apple:\n", 
	  "Colour: ", appl.colour, "\n", 
	  "Mass: ",appl.mass,"\n",
	  "Sort: ",appl.sort,"\n",
	  "Rot: ",appl.rot)

#-2-------------------------------------------------
#Area of circle

class Circle():
	def __init__(self, r):
		self.radius = r
	def area(self):
		return 3.14 * math.pow(self.radius,2)


circl = Circle(12)
areaCir = circl.area()
print("Area circle = ", areaCir)

#-3-------------------------------------------------
#Area of Triangle
class Triangle():
	def __init__(self, h, b):
		self.height = h
		self.base = b
	def area(self):
		return (0.5 * self.height) * self.base

triangle = Triangle(7, 5)

areaTri = triangle.area()

print("Area triangle = ",areaTri)

#-4-------------------------------------------------
#Perimetr Hexagon 6

class Hexagon():
	def __init__(self, a):
		self.side = a
	def calculate_perimetr(self):
		return self.side * 6

hexagon = Hexagon(6)

perimetr_hex = hexagon.calculate_perimetr()

print("Perimetr hexagon = ",perimetr_hex)