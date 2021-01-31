import re

string = "Красивое лучше, чем уродливое"


result = re.findall("Красивое", string, re.IGNORECASE)
#re.IGNORECASE позволяет не учитывать регистр при поиске
print(result)

#Совпадение в начале
zen = """
		Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
	  """

m = re.findall("^If", zen, re.MULTILINE)

print(m)

#Поиск совпадений с несколькими символами
string2 = " Два даа."

mes = re.findall("д[ав]а", string2, re.IGNORECASE)
print(string2)


#Совпадение цифр "\d"
line = "123?34 hello?"

res = re.findall("\d", line, re.IGNORECASE)

print(res)

#Нежадный поиск совпадений

t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)

for match in found:
	print(match)


#Нежадный поиск в игре чепуха

text = """
		  Жирафы любят таскать 
		  различные __СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__
		  целый день напролет. Жирафы 
		  также славятся тем, что поедают
		  прекрасные __СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__, но 
		  после этого у них часто
		  болит __ЧАСТЬ_ТЕЛА__. Если же
		  жирафы находят __ЧИСЛО__
		  __СУЩЕСТВИТЕЛЬНОЕ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ__, у
		  них моментально отваливается __ЧАСТЬ ТЕЛА__.
	   """

def mad_libs(mls):
	"""
	:param mls: В строках пользавательский
	ввод должен быть окружен двойными подчеркиваниями.
	Подчеркивания нельзя вставлять в подсказку:
	__подсказка_подсказка__ (нельзя);
	__подсказка__ (можно).
	"""
	hints = re.findall("__.*?__", mls)

	if hints is not None:
		for word in hints:
			q = input("Введите {}".format(word))
			mls = mls.replace(word, q, 1)
		print('\n')
		mls = mls.replace('\n', "")
		print(mls)
	else: print("Ошибка ввода")
		
mad_libs(text)


#Управляющие символы

line = "I love $"

res = re.findall("\\$", line, re.IGNORECASE)

print(res)

#-Ex-----------

text = "Привидение прошуршало и исчезло в углу"
res = re.findall(".ло", text, re.IGNORECASE)
result = re.findall("[за]ло", text, re.IGNORECASE)

print(res)
print(result)