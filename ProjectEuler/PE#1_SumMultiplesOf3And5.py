def sum_3_and_5():
    sumList = []
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            sumList.append(i)
    return sum(sumList)

n = sum_3_and_5()

print(str(n))
