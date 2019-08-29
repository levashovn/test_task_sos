def general_swap(x, y):
	x ,y = y, x
	print(x, y)

def string_swap(x, y):
	x = x + y
	y = x[0: (len(x) - len(y))]
	x = x[len(y):]
	print(x, y)

def int_second_swap(x, y):
	x ^= y
	y ^= x
	x ^= y
	print(x, y)

def int_third_swap(x, y):
	x = x + y
	y = x - y
	x = x - y
	print(x, y)

def int_fourth_swap(x, y):
	x = x * y
	y = x / y
	x = x / y
	print(int(x), int(y))

if __name__ == "__main__":
	general_swap(1, 2)
	string_swap('hello', 'world')
	int_second_swap(1, 2)
	int_third_swap(1, 2)
	int_fourth_swap(1, 2)

