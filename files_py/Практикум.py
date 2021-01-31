
num_1 = input("Введите делимое: ")
int_num = int(num_1)
num_2 = input("Введите делитель: ")
int_num2 = int(num_2)
print(int_num / int_num2)



age = input("Введите ваш возраст: ")
int_age = int(age)

if int_age > 10 and int_age < 15:
	print("Так вы еще ребёнок")
elif int_age > 15 and int_age < 20:
	print("Вы уже подросток получается")
elif int_age > 20:
	print("Добро пожаловать на сайт")