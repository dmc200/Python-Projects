Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def square(x):
	return x * x

>>> def my_map(func, arg_list):
	result =[]
	for i in arg_list:
		result.append(func(i))
	return result

>>> squares = my_func(square, [1,2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    squares = my_func(square, [1,2,3,4,5])
NameError: name 'my_func' is not defined
>>> squares = my_map(square, [1,2,3,4,5])
>>> 
>>> 
>>> print(squares)
[1, 4, 9, 16, 25]
>>> 
>>> def cube(x):
	return x * x * x

>>> squares = my_func(cube, [1,2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    squares = my_func(cube, [1,2,3,4,5])
NameError: name 'my_func' is not defined

>>> squares = my_map(cube, [1,2,3,4,5])
>>> 
>>> squares
[1, 8, 27, 64, 125]
>>> 
>>> 
>>> 
>>> 
>>> def logger(msg):
	ref log_message():
		
SyntaxError: invalid syntax
>>> def logger(msg):
	def log_message():
		print('Log:', msg)
	return log_message

>>> log_hi = logger('Hi!')
>>> log_hi()
Log: Hi!
>>> # Above is an example of passing a function as an arg and returning a function
>>> # log_hi == log_message() function.
>>> 
>>> def html_tag(tag):
	def wrap_text(msg):
		print('<{0}>{1}</{0}>'.format(tag, msg))
	return wrap_text

>>> print_h1 = html_tag('h1')
>>> 
>>> print_h1()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print_h1()
TypeError: wrap_text() missing 1 required positional argument: 'msg'
>>> print(print_h1)
<function html_tag.<locals>.wrap_text at 0x0407EBB8>
>>> 
>>> print_h1('Hello World!')
<h1>Hello World!</h1>
>>> print_h1('Test Headline')
<h1>Test Headline</h1>
>>> print_h1('Another Headline!')
<h1>Another Headline!</h1>
>>> 
>>> 
>>> 
>>> # Below are examples of the concept of Closures.
>>> 
>>> def outer_func():
	message = 'Hi'
	def inner_func():
		print(message)
	return inner_func()

>>> outer_func()
Hi
>>> def outer_func():
	message = 'Hi'
	def inner_func():
		print(message)
	return inner_func

>>> outer_func()
<function outer_func.<locals>.inner_func at 0x0407EC48>
>>> my_func = outer_func()
>>> my_func
<function outer_func.<locals>.inner_func at 0x0407ECD8>
>>> my_func()
Hi
>>> print(my_func.__name__)
inner_func
>>> # A closure is an inner function that has access to the variables within its local scope.
>>> 
>>> def outer_func(msg):
	message = msg
	def inner_func():
		print(message)
	return inner_func

>>> hi_func = outer_func()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    hi_func = outer_func()
TypeError: outer_func() missing 1 required positional argument: 'msg'
>>> hi_func = outer_func('Hi')
>>> hi_func
<function outer_func.<locals>.inner_func at 0x0407ED20>
>>> hi_func()
Hi
>>> hello_func = outer_func("Hello")
>>> hello_func()
Hello
>>> # A Closure 'closes over' the outside function.
>>> 
>>> 
>>> # Below is an example of Python Decorators.
>>> 
>>> def outer_function():
	message = "Hi"

	
>>> def outer_function():
	message = "Hi"
	def inner_function():
		print(message)
	return inner_function()

>>> outer_function()
Hi
>>> # The inner function remembers the message = 'Hi' variable and value even after returned.
>>> 
>>> def outer_function():
	message = "Hi"
	def inner_function():
		print(message)
	return inner_function
	# Remove the () activating the inner_function being passed

	
>>> my_func = outer_function()
>>> my_func()
Hi
>>> def outer_function(msg):
	message = msg
	def inner_function():
		print(message)
	return inner_function

>>> hi_func = outer_function('Hi')
>>> 
>>> bye_func = outer_function('Bye')
>>> 
>>> hi_func()
Hi
>>> bye_func()
Bye
>>> def outer_function(msg):
	def inner_function():
		print(msg)
	return inner_function

>>> hello = outer_function('Hello')
>>> hello()
Hello
>>> # A decorator is a function that takes another function as an argument and adds functionality to another function.
>>> 
>>> # Additionally a decorator returns a function
>>> 
>>> 
>>> def decorator_function(message):
	def wrapper_function():
		print(message)
	return wrapper_function

>>> hi_func = outer_function('Hi')
>>> bye_func = outer_function('Bye')
>>> hi_func
<function outer_function.<locals>.inner_function at 0x0407EF60>
>>> hi_func()
Hi
>>> bye_func()
Bye
>>> def decorator_function(original_function):
	def wrapper_function():
		original_function()
	return wrapper_function

>>> def display():
	print('display function ran')

	
>>> decorated_display = decorator_function(display)
>>> 
>>> decorated_display()
display function ran
>>> # The decorator function accepts a function, passes that function to the wrapper function and returns the wrapper function.
>>> decorated_display()
display function ran
>>> # Executing the above function returns the value of the function passed into the wrapper function.
>>>  def decorator_function(original_function):
	def wrapper_function():
		print('Wrapper executed this before {}'.format(orignial_function.__name__))
		original_function()
	return wrapper_function
SyntaxError: unexpected indent
>>> def decorator_function(original_function):
	def wrapper_function():
		print('Wrapper executed this before {}'.format(orignial_function.__name__))
		original_function()
	return wrapper_function

>>> decorated_display = decorator_function(display)
>>> decorated_display()
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    decorated_display()
  File "<pyshell#145>", line 3, in wrapper_function
    print('Wrapper executed this before {}'.format(orignial_function.__name__))
NameError: name 'orignial_function' is not defined
>>> display
<function display at 0x0407EF18>
>>> def decorator_function(original_function):
	def wrapper_function():
		print('Wrapper executed this before {}'.format(orignial_function.__name__))
		original_function()
	return wrapper_function

>>> d = decorator_function(display)
>>> d()
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    d()
  File "<pyshell#150>", line 3, in wrapper_function
    print('Wrapper executed this before {}'.format(orignial_function.__name__))
NameError: name 'orignial_function' is not defined
>>> 
>>> 
>>> 
>>> 
>>> def decorator_function(original_function):
	def wrapper_function():
		print('Wrapper executed this before {}'.format(original_function.__name__))
		original_function()
	return wrapper_function

>>> d = decorator_function(display)
>>> d()
Wrapper executed this before display
display function ran
>>> 
== RESTART: C:/Users/dchrie504/Desktop/Tutorial/Python/Decorator_Example.py ==
Wrapper executed this before display
display function ran
>>> 
== RESTART: C:/Users/dchrie504/Desktop/Tutorial/Python/Decorator_Example.py ==
Wrapper executed this before display
display function ran
>>> 
== RESTART: C:/Users/dchrie504/Desktop/Tutorial/Python/Decorator_Example.py ==
display_info ran with arguments (John, 25)
>>> 
== RESTART: C:/Users/dchrie504/Desktop/Tutorial/Python/Decorator_Example.py ==
Traceback (most recent call last):
  File "C:/Users/dchrie504/Desktop/Tutorial/Python/Decorator_Example.py", line 15, in <module>
    display_info('John', 25)
TypeError: wrapper_function() takes 0 positional arguments but 2 were given
>>> 
== RESTART: C:/Users/dchrie504/Desktop/Tutorial/Python/Decorator_Example.py ==
Wrapper executed this before display_info
Traceback (most recent call last):
  File "C:/Users/dchrie504/Desktop/Tutorial/Python/Decorator_Example.py", line 15, in <module>
    display_info('John', 25)
  File "C:/Users/dchrie504/Desktop/Tutorial/Python/Decorator_Example.py", line 4, in wrapper_function
    original_function()
TypeError: display_info() missing 2 required positional arguments: 'name' and 'age'
>>> 
== RESTART: C:/Users/dchrie504/Desktop/Tutorial/Python/Decorator_Example.py ==
Wrapper executed this before display_info
display_info ran with arguments (John, 25)
>>> 
== RESTART: C:/Users/dchrie504/Desktop/Tutorial/Python/Decorator_Example.py ==
Call method executed this before display_info
display_info ran with arguments (John, 25)
>>> 
== RESTART: C:/Users/dchrie504/Desktop/Tutorial/Python/Decorator_Example.py ==
Call method executed this before display_info
display_info ran with arguments (John, 25)
Call method executed this before display
display function ran
>>> 
== RESTART: C:/Users/dchrie504/Desktop/Tutorial/Python/Decorator_Example.py ==
display_info ran with arguments (Tom, 22)
>>> 
