Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [1,'a','2',3,3,4,5,'b']
>>> 
>>> a
[1, 'a', '2', 3, 3, 4, 5, 'b']
>>> b = [x for x in a if isinstance(x, int)]
>>> b
[1, 3, 3, 4, 5]
>>> sorted(b)
[1, 3, 3, 4, 5]
>>> b = sorted(b)
>>> set(b)
{1, 3, 4, 5}
>>> b = set(b)
>>> b[1]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b[1]
TypeError: 'set' object does not support indexing
>>> b = list(b)
>>> b
[1, 3, 4, 5]
>>> b[1]
3
>>> def find_2nd_largest(arr):
	b = [x for x in arr if isinstance(x, int)]
	b = sorted(b)
	b = set(b)
	b = list(b)
	return b[1]

>>> find_2nd_largest([1, 'a', '2', 3, 3, 4, 5, 'b'])
3
>>> def find_2nd_largest(arr):
	b = [x for x in arr if isinstance(x, int)]
	b = sorted(b)
	b = set(b)
	b = list(b)
	if len(b) == 1: 
		return 'nil'
	else:
		return b[1]

	
>>> 
>>> find_2nd_largest([1, 'a', '2', 3, 3, 4, 5, 'b'])
3
>>> 
>>> find_2nd_largest([1,'a','2',3,3,3333333333333333333334,
544444444444444444444444444444,'b'])
3333333333333333333334
>>> find_2nd_largest([1,1,1,1,1,1,1])
'nil'
>>> def find_2nd_largest(arr):
	b = [x for x in arr if isinstance(x, int)]
	b = sorted(b)
	b = set(b)
	b = list(b)
	if len(b) == 1: 
		return nil
	else:
		return b[1]

	
>>> find_2nd_largest([1,1,1,1,1,1,1])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    find_2nd_largest([1,1,1,1,1,1,1])
  File "<pyshell#29>", line 7, in find_2nd_largest
    return nil
NameError: name 'nil' is not defined
>>> def find_2nd_largest(arr):
	b = [x for x in arr if isinstance(x, int)]
	b = sorted(b)
	b = set(b)
	b = list(b)
	if len(b) == 1: 
		return 'nil'
	else:
		return b[1]

	
>>> find_2nd_largest([1,1,1,1,1,1,1])
'nil'
>>> find_2nd_largest([1,'a','2',3,3,4,5,'b'])
3
>>> find_2nd_largest([1,'a','2',3,3,3333333333333333333334,
544444444444444444444444444444,'b'])
3333333333333333333334
>>> find_2nd_largest(['4', 'Y', 56418, 28038, 87070, 'C', 68809, '7', 10798, 'F', 'C', 'W', '0', 7629, 10326, 61306, 'G', 1853, 11769, 'S'])
28038
>>> def find_2nd_largest(arr):
	b = [x for x in arr if isinstance(x, int)]
	b = sorted(b)
	b = set(b)
	b = list(b)
	if len(b) == 1: 
		return 'nil'
	else:
		return b[-2]

	
>>> find_2nd_largest(['4', 'Y', 56418, 28038, 87070, 'C', 68809, '7', 10798, 'F', 'C', 'W', '0', 7629, 10326, 61306, 'G', 1853, 11769, 'S'])
1853
>>> 
>>> 
>>> 
>>> 
>>> key = 'hello'
>>> 
>>> key = key.split()
>>> key
['hello']
>>> key.split('')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    key.split('')
AttributeError: 'list' object has no attribute 'split'
>>> key
['hello']
>>> key = str(key)
>>> key
"['hello']"
>>> key = 'hello'
>>> 
>>> l = []
>>> for x in key:
	l.append(x)

	
>>> l
['h', 'e', 'l', 'l', 'o']
>>> l[0].upper()
'H'
>>> for x in l:
	print(l[x].upper())

	
Traceback (most recent call last):
  File "<pyshell#64>", line 2, in <module>
    print(l[x].upper())
TypeError: list indices must be integers or slices, not str
>>> for x in range(len(l)):
	print(l[x].upper())

	
H
E
L
L
O
>>> 
>>> 
>>> l[0:].upper() + l[1:]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    l[0:].upper() + l[1:]
AttributeError: 'list' object has no attribute 'upper'
>>> l[0].upper()
'H'
>>> l[0].upper() + l[1:]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    l[0].upper() + l[1:]
TypeError: can only concatenate str (not "list") to str
>>> l[0].upper() + str(l[1:])
"H['e', 'l', 'l', 'o']"
>>> l[0].upper() + ''.join(l[1:])
'Hello'
>>> l
['h', 'e', 'l', 'l', 'o']
>>> for x in range(len(l)):
	print(l[x].upper() + ''.join(l[x+1:]))

	
Hello
Ello
Llo
Lo
O
>>> a = []
>>> key.index(1)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    key.index(1)
TypeError: must be str, not int
>>> key
'hello'
>>> key
'hello'
>>> key.index('h')
0
>>> for x in key:
	c = key.index(x)
	key.strip(x)

	
'ello'
'hello'
'hello'
'hello'
'hell'

>>> l
['h', 'e', 'l', 'l', 'o']
>>> l.index('h')
0
>>> l.insert(0, "H")
>>> l
['H', 'h', 'e', 'l', 'l', 'o']
>>> key
'hello'
>>> l = []
>>> l = key.split()
>>> l
['hello']
>>> l =[]
>>> l = key.split('')
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    l = key.split('')
ValueError: empty separator
>>> l = list(key)
>>> l
['h', 'e', 'l', 'l', 'o']
>>> ans = list()
>>> ans
[]
>>> for x in range(len(l)):
	l.remove(l[x])
	l.insert(x, l[x].upper())
	ans.append(l)

	
Traceback (most recent call last):
  File "<pyshell#114>", line 3, in <module>
    l.insert(x, l[x].upper())
IndexError: list index out of range
>>> for x in range(len(l)):
	item = l.pop(index=x)
	l.remove(item)
	l.insert(x, item.upper())
	ans.append(l)

	
Traceback (most recent call last):
  File "<pyshell#116>", line 2, in <module>
    item = l.pop(index=x)
TypeError: pop() takes no keyword arguments
>>> l
['E', 'L', 'L', 'O']
>>> l = ['h', 'e', 'l', 'l', 'o']
>>> 
>>> l
['h', 'e', 'l', 'l', 'o']
>>> l.pop(index=0)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    l.pop(index=0)
TypeError: pop() takes no keyword arguments
>>> l.pop(0)
'h'
>>> for x in range(len(l)):
	item = l.pop(x)
	l.remove(item)
	l.insert(x, item.upper())
	ans.append(l)

	
Traceback (most recent call last):
  File "<pyshell#128>", line 3, in <module>
    l.remove(item)
ValueError: list.remove(x): x not in list
>>> l
['l', 'l', 'o']
>>> ans
[['E', 'L', 'L', 'O'], ['E', 'L', 'L', 'O'], ['E', 'L', 'L', 'O'], ['E', 'L', 'L', 'O']]
>>> ans = []
>>> for x in range(len(l)):
	item = l.pop(x)
	l.remove(item)
	l.insert(x, item.upper())
	ans.append(l)

	
Traceback (most recent call last):
  File "<pyshell#133>", line 3, in <module>
    l.remove(item)
ValueError: list.remove(x): x not in list
>>> l
['L']
>>> l = ['h', 'e', 'l', 'l', 'o']
>>> l.pop(0)
'h'
>>> l
['e', 'l', 'l', 'o']
>>> l.insert(0, 'H')
>>> l
['H', 'e', 'l', 'l', 'o']
>>> for x in range(len(l)):
	l = ['h', 'e', 'l', 'l', 'o']
	item = l.pop(x)
	l.insert(x, item.upper())
	ans.append(l)

	
>>> ans
[['L'], ['H', 'e', 'l', 'l', 'o'], ['h', 'E', 'l', 'l', 'o'], ['h', 'e', 'L', 'l', 'o'], ['h', 'e', 'l', 'L', 'o'], ['h', 'e', 'l', 'l', 'O']]
>>> ans = []
>>> l
['h', 'e', 'l', 'l', 'O']
>>> l = ['h', 'e', 'l', 'l', 'o']
>>> ans
[]
>>> for x in range(len(l)):
	l = ['h', 'e', 'l', 'l', 'o']
	item = l.pop(x)
	l.insert(x, item.upper())
	ans.append(l)

	
>>> ans
[['H', 'e', 'l', 'l', 'o'], ['h', 'E', 'l', 'l', 'o'], ['h', 'e', 'L', 'l', 'o'], ['h', 'e', 'l', 'L', 'o'], ['h', 'e', 'l', 'l', 'O']]
>>> for x in ans:
	print(''.join(x))

	
Hello
hEllo
heLlo
helLo
hellO
>>> 
>>> 
>>> key = 'hello'
>>> key = list(key)
>>> key
['h', 'e', 'l', 'l', 'o']
>>> ans = []
>>> key
['h', 'e', 'l', 'l', 'o']
>>> li = ['h', 'e', 'l', 'l', 'o']
>>> 
>>> ans
[]
>>> key
['h', 'e', 'l', 'l', 'o']
>>> key = 'hello'
>>> lkey = list(key)
>>> lkey
['h', 'e', 'l', 'l', 'o']
>>> for x in range(len(key)):
	item = lkey.pop(x)
	lkey.insert(x, item.upper())
	ans.append(lkey)

	
>>> ans
[['H', 'E', 'L', 'L', 'O'], ['H', 'E', 'L', 'L', 'O'], ['H', 'E', 'L', 'L', 'O'], ['H', 'E', 'L', 'L', 'O'], ['H', 'E', 'L', 'L', 'O']]
>>> key = 'hello'
>>> lkey = list(key)
>>> lkey
['h', 'e', 'l', 'l', 'o']
>>> ans = []
>>> for i in range(len(lkey)):
	item = lkey.pop(x)
	lkey.insert(x, item.upper())
	ans.append(lkey)

	
>>> ans
[['h', 'e', 'l', 'l', 'O'], ['h', 'e', 'l', 'l', 'O'], ['h', 'e', 'l', 'l', 'O'], ['h', 'e', 'l', 'l', 'O'], ['h', 'e', 'l', 'l', 'O']]
>>> ans =[]
>>> for i in range(len(key))
SyntaxError: invalid syntax
>>> for i in range(len(key)):
	item = lkey.pop(x)
	lkey.insert(x, item.upper())
	ans.append(lkey)

	
>>> ans
[['h', 'e', 'l', 'l', 'O'], ['h', 'e', 'l', 'l', 'O'], ['h', 'e', 'l', 'l', 'O'], ['h', 'e', 'l', 'l', 'O'], ['h', 'e', 'l', 'l', 'O']]
>>> ans = []
>>> key
'hello'
>>> lkey
['h', 'e', 'l', 'l', 'O']
>>> lkey = list(key)
>>> lkey
['h', 'e', 'l', 'l', 'o']
>>> for i in range(len(key)):
	lkey = list(key)
	item = lkey.pop(x)
	lkey.insert(x, item.upper())
	ans.append(lkey)

	
>>> ans
[['h', 'e', 'l', 'l', 'O'], ['h', 'e', 'l', 'l', 'O'], ['h', 'e', 'l', 'l', 'O'], ['h', 'e', 'l', 'l', 'O'], ['h', 'e', 'l', 'l', 'O']]
>>> lkey
['h', 'e', 'l', 'l', 'O']
>>> for i in range(len(key)):
	print(i)

	
0
1
2
3
4
>>> key
'hello'
>>> lkey
['h', 'e', 'l', 'l', 'O']
>>> lkey = list(key)
>>> lkey
['h', 'e', 'l', 'l', 'o']
>>> ans = []
>>> for i in range(len(key)):
	lkey = list(key)
	item = lkey.pop(i)
	lkey.insert(i, item.upper())
	ans.append(lkey)

	
>>> ans
[['H', 'e', 'l', 'l', 'o'], ['h', 'E', 'l', 'l', 'o'], ['h', 'e', 'L', 'l', 'o'], ['h', 'e', 'l', 'L', 'o'], ['h', 'e', 'l', 'l', 'O']]
>>> a = [''.join(x) for x in ans]
>>> a
['Hello', 'hEllo', 'heLlo', 'helLo', 'hellO']
>>> ' '.upper()
' '
>>> def wave(key):
	lkey = list(key)
	ans = []
	for i in range(len(key)):
		lkey = list(key)
		item = lkey.pop(i)
		lkey.insert(i, item.upper())
		ans.append(lkey)
	a = [''.join(x) for x in ans]
	return a

>>> wave('hello')
['Hello', 'hEllo', 'heLlo', 'helLo', 'hellO']
>>> def wave(key):
	lkey = list(key)
	ans = []
	for i in range(len(key)):
		if lkey.pop(i) == ' ':
			pass
		else: 	
			lkey = list(key)
			item = lkey.pop(i)
			lkey.insert(i, item.upper())
			ans.append(lkey)
	a = [''.join(x) for x in ans]
	return a

>>> wave('hello bobby')
['Hllo bobby', 'hElo bobby', 'heLo bobby', 'helL bobby', 'hellObbby', 'hello Bbby', 'hello bOby', 'hello boBy', 'hello bobB', 'hello bobbY']
>>> 
>>> 
>>> def wave(key):
	lkey = list(key)
	ans = []
	for i in range(len(key)):
		if lkey[i] == ' ':
			pass
		else: 	
			lkey = list(key)
			item = lkey.pop(i)
			lkey.insert(i, item.upper())
			ans.append(lkey)
	a = [''.join(x) for x in ans]
	return a

>>> wave('hello bobby')
['Hello bobby', 'hEllo bobby', 'heLlo bobby', 'helLo bobby', 'hellO bobby', 'hello Bobby', 'hello bObby', 'hello boBby', 'hello bobBy', 'hello bobbY']
>>> 
