def compress(input):
	temp = {}
	result = " "
	for x in input:
		if x in temp:
			temp[x] = temp[x] + 1
		else:
			temp[x] = 1
	for key, value in temp.items():
		result += str(key) + str(value)
	print(result)
	return result

def compress_str(input):
	comp_str = ""
	counter = 1
	for i in range(len(input)-1):
		next = input[i+1]
		if input[i] == next:
			counter += 1
		else:
			comp_str += input[i] + str(counter)
			counter = 1
	comp_str += input[i] + str(counter)

	if len(comp_str) >= len(input):
		print(input)
		return input
	else:
		print(comp_str)
		return comp_str

if __name__ == "__main__":
	input = input("Enter a string\n")
	compress_str(input)
	compress(input)