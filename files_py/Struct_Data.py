#list
musicants = ["25/17",
			 "Оксимирон",
			 "Драгни",
			 "Дора"]

musicants.append("Кравц")


print(musicants)

#kortege in list
list_place = []

moscow_tuple = (55.4507,37.3659)
sain_p_tuple = (59.57,30.19)
nsk_tuple = (55.00835, 82.93573)

list_place.append(moscow_tuple)
list_place.append(sain_p_tuple)
list_place.append(nsk_tuple)

print(list_place)


info_dict = {"Имя":
			 "Виктиша",
			 "Рост":
			 "142",
			 "Любимый музыкант":
			 "Пьер Вудман",
			 "Любимая еда":
			 "Роллы"}


info = input("Что вы хотите узнать обомне?\n Рост, Имя, Любимую еду или музыканта?\n")

if info in info_dict:
	result = info_dict[info]
	print(result)
else:
	print("Информации об этом нет")

misic_list = ["Комната", "Там где нас нет", "Лакоста", "Дура"]


#Словарь, ключами которого является список
all_info_dict = {musicants[0]:
				 misic_list[0],
				 musicants[1]:
				 misic_list[1],
				 musicants[2]:
				 misic_list[2],
				 musicants[3]:
				 misic_list[3]}

print(all_info_dict)


#множества

a = set("hello")

print(a)


a = {i**2 for i in range(10)}
print(a)

other = [12, 5, 15, 3]


print(a.isdisjoint(other))