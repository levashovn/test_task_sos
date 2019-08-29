def check_reverse(a):
	reversed = a[::-1]
	if a == reversed:
		print("Palindrome!")
	else:
		print("Not a palindrome!")


def check_reverse_second(a):
	if len(a) == 0:
		print('Palindrome!')
	if a[0] == a[-1]:
		try:
			return check_reverse_second(a[1:-1])
		except IndexError:
			pass


def check_reverse_third(a):
	reverse_str = ""
	for c in a:
		reverse_str = c + reverse_str
	if a == reverse_str:
		print("Palindrome!")
	else:
		print('Not a palindrome!')


if __name__ == "__main__":
	a = input("Enter a string\n")
	check_reverse(a)
	check_reverse_second(a)
	check_reverse_third(a)
