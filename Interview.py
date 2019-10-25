
# Run Fib Sequence up until a certain number of times. 
def fib(n):
	x=0
	a = 1
	b = 1
	while(x < n):
		print(a)
		a, b = b, a + b
		x = x + 1

#Basic FizzBuzz problem. 
def fib_buzz(n):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print('Buzz')
    elif x % 5 ==0:
        print("Fizz")



# What is the difference between Tuple and List?
    # Tuples have structure, lists have order
    tup = (43, 2) # 43 is page number, 2 is line number.
    lst = [1, 4, 5, 6, 7, 'asdf'] # Lists have order

    # Additionally touples are immutable, meanig values cannot be changed.
    # Lists are Mutable and the values can be changed once created. 
    # TypeError: 'tuple' object does not support item assignment




#**Include some Generator Examples below ** 
