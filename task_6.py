import itertools
def create_dict_first(keys, values):
	print ({keys:values for keys,values in itertools.zip_longest(keys,values,fillvalue=None)})

def create_dict_second(keys, values):
	a = dict(zip(keys, values + [None] * (len(keys) - len(values))))
	print(a)

def create_dict_third(keys, values):
	it_k = iter(keys)
	it_v = iter(values)
	d = {}
	for x, y in itertools.zip_longest(it_k, it_v):
		d[x] = y
	print(d)


keys = [1, 3, 5, 6, 7, 10, 11, 15]
values = [5, 7, 8, 8, 9, 0, 5]
create_dict_first(keys, values)
create_dict_second(keys, values)
create_dict_third(keys, values)