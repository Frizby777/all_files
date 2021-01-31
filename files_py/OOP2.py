
class Shape():
	def __init__(self, n, w, l):
		self.name = n
		self.weidth = w
		self.lenght = l
	def print_size(self):
		print("Name shape: {}, size {} on {}".format(self.name, self.weidth,self.lenght))


my_shape = Shape("Empty", 25, 30)

my_shape.print_size()


class Square(Shape):
	def area(self):
		return self.weidth * self.lenght
	def print_size(self): # переопределение метода класса Shape в производном классе Square
		print("Название фигуры: {}, размер = {} на {}".format(self.name, self.weidth, self.lenght))
	#pass #ключевое слово, заглушка

my_square = Square("Square", 44, 44)

my_square.print_size()
area_square = my_square.area()
name_shape = my_square.name 

print("Area {} = {}".format(name_shape,area_square))


#-Агрегация/Композиция
class Dog():
	def __init__(self, name, breed, owner):
		self.name = name
		self.breed = breed
		self.owner = owner

class Person():
	def __init__(self, name):
		self.name = name


person = Person("Микки Рурк")
dog = Dog("Беляш", "Лабрадор", person)

print(dog.owner.name)


#-1---2----3---------------------------------

class Shape():
	def what_i_am(self):
		print("I'm a shape")

class Rectangle(Shape):
	def __init__(self, n, a, b):
		self.name = n
		self.weidth = a
		self.lenght = b
	def calculate_perimeter(self):
		return 2 * (self.weidth + self.lenght)


class Square(Shape):
	def __init__(self, n, a):
		self.name = n
		self.a = a
	def calculate_perimeter(self):
		return self.a * 4
	def change_size(self, n):
		self.a += n


rectangle = Rectangle("Прямоугольник", 3, 5)
square = Square("Квадрат", 5)

p_rec = rectangle.calculate_perimeter()
p_square = square.calculate_perimeter()

print(p_rec, p_square)
print(square.a)
square.change_size(2)

print(p_square)

print(square.a)

rectangle.what_i_am()
square.what_i_am()
print("\n", "\n")
#-4---------------------------------------------

class Hors():
	def __init__(self, name, breed, owner):
		self.name = name
		self.breed = breed
		self.owner = owner


class Owner():
	def __init__(self, name):
		self.name = name


owner = Owner("Тоя")
hors = Hors("Викишки", "Звёздочка", owner)

print("У поняши {}, породы {}, есть любимый хозяин - {}".format(hors.name, hors.breed, hors.owner.name))