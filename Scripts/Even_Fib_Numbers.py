 # generate fib numbers. 

 # ind all the even numbers. 

 # sum all of the even numbers. 

def fib():
	fibNumbers = [1, 2]
	evenFibs = []
	while fibNumbers[-1] < 4000000:
		fibNumbers.append(fibNumbers[-1] + fibNumbers[-2])

	for x in fibNumbers: 
		if x % 2 ==0: 
			evenFibs.append(x)

	
	return sum(evenFibs)


fib()

		

