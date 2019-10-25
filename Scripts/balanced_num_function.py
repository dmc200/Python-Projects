import math

def balanced_num(n):
		   res1=0
		   res2=0
		   len_ =0
		   n = list(str(n))
		   n = [int(x) for x in n]
		   if len(n) % 2 == 0:
                       #means length is even
		       len_ = (len(n) / 2)-1
			   for x in range(0,len_):
                    res1+= n[x]
               n.reverse()
			   for x in range(0,len_):
			       res2+= n[x]
		   else:
		   #means length is odd
		       len_ = math.floor((len(n) / 2))
			   for x in range(0,len_):
			       res1+=n[x]
			   n.reverse()
			   for x in range(0,len_):
				       res2+=n[x]
                       
		   if res1==res2:
		       return True
		   else:
		       return False

balanced_num(111311)

