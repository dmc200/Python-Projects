'''
Example : "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"

There is still and issue with this function that if the weight is the same the 11, needs to come before 2000
'''

def order_weight(string):
	string = string.split(' ')
	ans1 = []
	for x in string:
		tot = 0
		for i in x:
			tot += int(i)
		ans1.append((x, tot))
	ans1 = sorted(sorted(ans1, key=lambda tup: tup[1]))
	return ' '.join([x[0] for x in ans1])
