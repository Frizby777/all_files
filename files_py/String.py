author = "Чехов"

print(author[0] + "\n" + author[1] + "\n" +author[2] + "\n" +author[3] + "\n" +author[4] + "\n")


a = input("Что вы писали вчера? ")
b = input("Куда ходили? ")
result = "Вчера я написал {}. Вчера я ходил {}!".format(a, b)

print(result)


result = "олдос Хасксли родился в 1894 году.".capitalize()

print(result)

newstring = "Где это? Кто это? Когда это?".split("? ")

print(newstring)

lists = ["Рыжая", "лиса", "перепрыгнула", "через", "низкий", "забор", "."]

one = " ".join(lists)
one = one.replace(" .", ".")

print(one)

child = "Ребенок - зеркало поступков родителей."
child = child.replace("о", "0")
print(child)


author = "Хемингуэй"
print(author.index("и"))

three = "три"
print(three+three+three)


string = "И зачем так орать! Я и в первый раз прекрасно слышал."

print(string[0:17])

i = 24
while i < 50:
	i+=1
	print(i)
#print(string[0:1])