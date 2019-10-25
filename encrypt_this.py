Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'A wise old owl lived in an oak'
>>> s
'A wise old owl lived in an oak'
>>> s2 = s.strip()
>>> s2
'A wise old owl lived in an oak'
>>> s2 = s.split(' ')
>>> s2
['A', 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> for x in s2:
	print(ord(x[0]))

	
65
119
111
111
108
105
97
111
>>> for x in s2:
	x[0] = ord(x[0])

	
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    x[0] = ord(x[0])
TypeError: 'str' object does not support item assignment
>>> s2
['A', 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> ord('a')
97
>>> ord('A')
65
>>> for x in s2:
	x[0] = ord(x[0])

	
Traceback (most recent call last):
  File "<pyshell#20>", line 2, in <module>
    x[0] = ord(x[0])
TypeError: 'str' object does not support item assignment
>>> s2[0] = ord(s2[0])
>>> s2
[65, 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> s2[1] = ord(s2[1][0])
>>> s2
[65, 119, 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> s2
[65, 119, 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> s2 = ['A', 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> s2
['A', 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> s2
['A', 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> s2[1][0] = ord(s2[1][0])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s2[1][0] = ord(s2[1][0])
TypeError: 'str' object does not support item assignment
>>> s2[1][0]
'w'
>>> o = ord(s2[1][0])
>>> s2[1][0] = o
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s2[1][0] = o
TypeError: 'str' object does not support item assignment
>>> s2
['A', 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> s3 = []
>>> s3[1] = ord(s2[1][0])
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s3[1] = ord(s2[1][0])
IndexError: list assignment index out of range
>>> s3.append(ord(s2[1][0]))
>>> s3
[119]
>>> s3 = []
>>> s2
['A', 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> s3.append(ord(s2[1][0] + s2[1][1:]))
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s3.append(ord(s2[1][0] + s2[1][1:]))
TypeError: ord() expected a character, but string of length 4 found
>>> s3.append(ord(s2[1][0]) + s2[1][1:]))
SyntaxError: invalid syntax
>>> s3.append(ord(s2[1][0]) + s2[1][1:])
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s3.append(ord(s2[1][0]) + s2[1][1:])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> s3.append(str(ord(s2[1][0])) + s2[1][1:])
>>> s3
['119ise']
>>> s3 = []
>>> s2
['A', 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> s2[1]
'wise'
>>> s2[1] = s2[1:] + s[0]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    s2[1] = s2[1:] + s[0]
TypeError: can only concatenate list (not "str") to list
>>> s2[1:] + s2[0]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s2[1:] + s2[0]
TypeError: can only concatenate list (not "str") to list
>>> s2[1][1:] + s2[1][0]
'isew'
>>> s2[1][1:] + s2[1][1]
'isei'
>>> s2[1][2:] + s2[1][1]
'sei'
>>> s3
[]
>>> s3.append(str(ord(s2[1][0])) + s2[1][2:] + s2[1][1])
>>> s3
['119sei']
>>> s2
['A', 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> s3
['119sei']
>>> s3 = []
>>> s3 = [str(ord(x[1][0])) + x[1][2:] + x[1][1] for x in s2]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s3 = [str(ord(x[1][0])) + x[1][2:] + x[1][1] for x in s2]
  File "<pyshell#65>", line 1, in <listcomp>
    s3 = [str(ord(x[1][0])) + x[1][2:] + x[1][1] for x in s2]
IndexError: string index out of range
>>> for x in s2:
	print(str(ord(x[1][0])) + x[1][2:] + x[1][1])

	
Traceback (most recent call last):
  File "<pyshell#68>", line 2, in <module>
    print(str(ord(x[1][0])) + x[1][2:] + x[1][1])
IndexError: string index out of range
>>> s2
['A', 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> for x in s2:
	if len(x) > 1:
		print(str(ord(x[1][0])) + x[1][2:] + x[1][1])
	else:
		print(ord(x[0]))

		
65
Traceback (most recent call last):
  File "<pyshell#75>", line 3, in <module>
    print(str(ord(x[1][0])) + x[1][2:] + x[1][1])
IndexError: string index out of range
>>> s = ['wise']
>>> len(s[0])
4
>>> 
>>> 
>>> for x in s2:
	if len(x) > 1:
		print(str(ord(x[1][0])) + x[1][2:] + x[1][1])
	else:
		print(ord(x[0]))

		
65
Traceback (most recent call last):
  File "<pyshell#87>", line 3, in <module>
    print(str(ord(x[1][0])) + x[1][2:] + x[1][1])
IndexError: string index out of range
>>> for x in s2:
	if len(x) > 1:
		print(str(ord(x[0])) + x[1][2:] + x[1][1])
	else:
		print(ord(x[0]))

		
65
Traceback (most recent call last):
  File "<pyshell#89>", line 3, in <module>
    print(str(ord(x[0])) + x[1][2:] + x[1][1])
IndexError: string index out of range
>>> for x in s2:
	if len(x) > 1:
		print(str(ord(x[1][0])) + x[2:] + x[1])
	else:
		print(ord(x[0]))

		
65
105sei
108dl
119lw
105vedi
110n
110n
97ka
>>> for x in s2:
	if len(x) > 1:
		print(str(ord(x[0])) + x[2:] + x[1])
	else:
		print(ord(x[0]))

		
65
119sei
111dl
111lw
108vedi
105n
97n
111ka
>>> s3
[]
>>> s2 = 'A wise old owl lived in an oak'
>>> s2 = s2.split('')
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s2 = s2.split('')
ValueError: empty separator
>>> s2 = s2.split(' ')
>>> s2
['A', 'wise', 'old', 'owl', 'lived', 'in', 'an', 'oak']
>>> s3 =[]
>>> for x in s2:
    	if len(x) > 1:
    		s3.append((str(ord(x[0])) + x[2:] + x[1]))
    	else:
    		s3.append(ord(x[0]))

    		
>>> s3
[65, '119sei', '111dl', '111lw', '108vedi', '105n', '97n', '111ka']
>>> def encrypt_this(text):
	    s2 = text.split(' ')
	    s3 = []
	    for x in s2:
		if len(x) > 1:
			s3.append((str(ord(x[0])) + x[2:] + x[1]))
		else:
			s3.append(ord(x[0]))
	    return ''.join(s3)
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> def encrypt_this(text):
		s2 = text.split(' ')
		s3 = []
		for x in s2:
			if len(x) > 1:
				s3.append((str(ord(x[0])) + x[2:] + x[1]))
			else:
				s3.append(ord(x[0]))
		return ''.join(s3)

	
>>> encrypt_this('A wise old owl lived in an oak')
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    encrypt_this('A wise old owl lived in an oak')
  File "<pyshell#106>", line 9, in encrypt_this
    return ''.join(s3)
TypeError: sequence item 0: expected str instance, int found
>>> def encrypt_this(text):
		s2 = text.split(' ')
		s3 = []
		for x in s2:
			if len(x) > 1:
				s3.append((str(ord(x[0])) + x[2:] + x[1]))
			else:
				s3.append(str(ord(x[0])))
		return ''.join(s3)

	
>>> encrypt_this('A wise old owl lived in an oak')
'65119sei111dl111lw108vedi105n97n111ka'
>>> def encrypt_this(text):
		s2 = text.split(' ')
		s3 = []
		for x in s2:
			if len(x) > 1:
				s3.append((str(ord(x[0])) + x[2:] + x[1]))
			else:
				s3.append(str(ord(x[0])))
		return ' '.join(s3)

	
>>> encrypt_this('A wise old owl lived in an oak')
'65 119sei 111dl 111lw 108vedi 105n 97n 111ka'
>>> 
