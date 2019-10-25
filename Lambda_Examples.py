Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f(x):
	return 3*x +1

>>> f(2)
7
>>>  lambda x: 3x+1
SyntaxError: unexpected indent
>>> lambda x: 3x + 1
SyntaxError: invalid syntax
>>> g = lambda x: 3x + 1
SyntaxError: invalid syntax
>>> g = lambda x: 3*x + 1
>>> g(2)
7
>>> g(5)
16
>>> 
>>> g(10)
31
>>> # Combine first and last names.
>>> 
>>> full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
>>> fill_name(' lenoard', 'smith ')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    fill_name(' lenoard', 'smith ')
NameError: name 'fill_name' is not defined
>>> full_name(' lenoard', 'smith ')
'Lenoard Smith'
>>> 
