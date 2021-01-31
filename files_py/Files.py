import csv
import os

string = open("fl.txt","w+")
string.write("HELLO MOTO")
string.close()

with open("fl.txt", "a") as wr: #запись 
	wr.write("\nHiHiHI")


with open("fl.txt", "r") as read: #чтение
	print(read.read())

#csv file
#delimiter - указывает разделяющие символы 


with open("table.csv", "w") as writ:
	f = csv.writer(writ, delimiter = ",")
	f.writerow(["one",
				"two",
				"three"])
	f.writerow(["four",
				"five",
				"six"])



with open("table.csv", "r") as r:
	x = csv.reader(r, delimiter = ",")
	for row in x:
		print(",".join(row))




#stat = os.path.join('C:/',
#				'Users/',
#			 	'OneDrive/',
#			 	'Desktop/',
#			 	'Games/',
#			 	'MyStat.txt')


#-1----------------------------------------------------------
path = "C:/Users/tolik/OneDrive/Рабочий стол/Games/MyStat.txt"

with open(path, "r") as r:
	print(r.read())

#-2----------------------------------------------------------

quest = input("What are you doing?")
path = "C:/Users/tolik/OneDrive/Рабочий стол/Games/File_py.txt"
with open(path, "w") as w:
	w.write(quest)


#-3----------------------------------------------------------

lists = [["Звездные войны", "Терминатор", "Искуственный интеллект"], 
		 ["Дурак", "Матильда","Левиафан"], 
		 ["Люди в черном", "Я - робот", "Эволюция"]]

with open("lists.csv", "w+") as w:
	f = csv.writer(w, delimiter = ",")
	for show in lists:
		f.writerow(show)


					
