def findit(n):
		   lst1 = []
		   lst2 = []
		   d1 = {}
		   d2 = {}
		   for x in n[::2]:
			   lst1.append(x)
		   for x in n[1::2]:
			   lst2.append(x)
		   for x in lst1:
			   d1.setdefault(x, lst1.count(x))
		   for x in lst2:
			   d2.setdefault(x, lst2.count(x))
		   ans1 = min(d1, key=d1.get)
		   ans2 = min(d2, key=d2.get)
		   if ans1:
			   return ans1
		   elif ans2:
			   return ans2
