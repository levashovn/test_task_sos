import random

def create_txt_file():
	ask = True

	f = open('random_numbers.txt', 'w')
	while ask:
		try:
			rows_count = int(input('Please enter a number of rows to write: '))
			ask = False
			for row in range(rows_count):
				for i in range(25):
					num = random.randint(1, 100)
					f.write(str(num))
				f.write('\n')
		except:
			print('Please enter an integer number of rows')



def read_file():
	ask = True

	f = open('random_numbers.txt', 'r')
	while ask:

		try:
			rows_count = int(input('Please enter a number of rows to read: '))
			ask = False
			lines = f.readlines()
			if rows_count > len(lines):
				print('Provided number of rows is greater than the rows in a file, you will get the whole file as an ouput')
			for line in lines[-rows_count:]:
				##using split here to bypass endlines in console
				print(line.split('\n')[0])
		except:
			print('Please enter an integer number of rows')


if __name__ == "__main__":
	create_txt_file()
	read_file()