def function_delenie(int_num):
	return int_num / 2

def function_umnozh(int_num):
	int_num = int(int_num)
	print(int_num * 4) 


num = input("Введите число: ")
num = int(num)

result = function_delenie(num)
function_umnozh(result)


def function_string(value):
	value = float(value)
	return value

value = input("Input value: ")

try:
	results = function_string(value)
except ValueError:
	print("Невозможно преобразовать тип данных str в float")