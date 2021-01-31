import random

def hangman():
	rand = random.randint(0,3)
	word_list = ["кот", "снеговик", "медведь"]
	word = word_list[rand]
	fail = 0
	stages = ["",
			 "__________        ",
			 "|        |         ",
			 "|        0         ",
			 "|      / | \       ",
			 "|       / \        ",
			 "|                     ",
			 ]
	rletters = list(word)
	board = ["__"] * len(word)
	win = False
	print("Добро пожаловать на казнь!")
	while fail < len(stages) - 1:
		print("\n")
		msg = input("Введите букву: ")
		if msg in rletters:
			cind = rletters.index(msg)
			board[cind] = msg
			rletters[cind] = '$'
		else:
			fail += 1
		print((" ".join(board)))
		e = fail + 1
		print("\n".join(stages[0: e]))
		if "__" not in board:
			print("Вы смогли избежать казни. Было загадано слово: ")
			print(" ".join(board))
			win = True
			break
	if not win:
		print("\n".join(stages[0: fail]))
		print("Вас повесили. Было загадано слово: {}".format(word))


hangman()