'''
My Original Solution Below: (Slow)
'''
onetotwen = [f for f in range(1,21)]

def count_20s(onetotwen):
    for i in range(200000000, 232792569):
            counter=0
            for x in onetotwen:
                    if i % x == 0:
                            
                            counter = counter + 1
                            #print(str(i) + ' Counter: ' + str(counter))
                            #print(' Counter, num is now: ' + str(counter) + ' ' + str(i) + ' is evenly divisible by : ' + str(x))
                            if counter == 20:
                                    return print(str(i))
count_20s(onetotwen)



