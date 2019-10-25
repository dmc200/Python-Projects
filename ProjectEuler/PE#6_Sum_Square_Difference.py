def sum_square_diff():
    l1=[]
    l2=[]
    for x in range(1,101):
        l1.append(x**2)
    for x in range(1,101):
        l2.append(x)
    return (sum(l2)**2)-(sum(l1))


n = sum_square_diff()
print(str(n))
