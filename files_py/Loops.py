music_list = ["Комната", "Там где нас нет", "Лакоста", "Дура"]

name = "Ted"
i = 0

for i, show in enumerate(music_list):
	music_list[i] = show.upper()

print(music_list)
print("\n")

for i, show in enumerate(music_list):
	music_list[i] = show.lower()

print(music_list)


for i in range(1, 6):
	print(i)

x = 10
while x > 0:
	print(x)
	x -= 1
print("Happy New Year!")

#---------------------------
lists = ["How are you?",
		 "What are you doing?",
		 "Say me compliment"]
n = 0
while True:
	print("Input x for exit")
	a = input(lists[n])
	if(a == 'x'):
		break
	n = (n + 1) % 3

#----------------------------

for i in range(1, 11):
	if(i == 5 or i == 8):
		continue
	print(i)

print("\n")
#-----------------------------

x = 0
while x < 5:
	if x == 3:
		x +=1
		continue
	print(x)
	x +=1

#-1----------------------------

shows = ["Ходячие мертвецы",
		"Красавцы",
		"Клан Сопрано",
		"Дневники вампира"]

i = 0
for show in shows:
	shows[i] = show
	print(show)

for i, show in enumerate(shows):
	print(show)

#-2-----------------------------

for i in range(25,51):
	print(i)

#-3-----------------------------

for i, show in enumerate(shows):
	print(i, ")", show)

#-4-----------------------------

numbers = [4, 1, 2, 3, 5, 12, 16]
print('\n', "if you want exit, press x")

while True:
	answ = input("if you want exit, press x, Input number: ")
	if answ == 'x':
		break
	try:
		answ = int(answ)
	except ValueError:
		print("Please type a number or x to exit")
	if answ in numbers:
		print("You win!")
		break
	

#-5-----------------------------

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
	for j in list2:
		list3.append(i * j)
print(list3)		



