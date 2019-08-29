import datetime
def check_valid_date(y, m, d):
	is_valid = True
	try:
		date = datetime.datetime(y,m,d)
		if date > datetime.datetime.now():
			print('Future')
		else:
			print('Past')

	except ValueError:
		print('Non existing date')
		is_valid = False
	return is_valid

if __name__ == "__main__":
	check_valid_date(2019, 7, 3)
	check_valid_date(2039, 7, 3)
	check_valid_date(2012, 13, 40)
