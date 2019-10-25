def ninety_nine_bottles():
    lst = [x for x in range(0,100)]
    lst.reverse()
    for x in lst:
        while x > 1:
            print(str(x) + " bottles of beer on the wall " + str(x) + " bottles of beer, take one down pass it around, " + str(x-1) + " bottles of beer on the wall!")
            print("\n")
            break
        if x == 1:
            print(str(x) + " bottles of beer on the wall " + str(x) + " bottles of beer, take one down pass it around, " + str(x-1) + " bottle of beer on the wall!")
            print("\n")

ninety_nine_bottles()
            
