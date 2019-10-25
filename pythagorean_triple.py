def pythag_trip():
    r = 'y'
    while r != 'n':
        try:
            s1 = int(input("Enter a side: "))
            s2 = int(input("Enter a side: "))
            s3 = int(input("Enter a side: "))
            l = [s1, s2, s3]
            max_l = max(l)
            #print(s1**2 + s2**2) == (max_l**2)
            if (s1**2 + s2**2) == (max_l**2):
                print("Yes it is a pythag Trip!")
            else:
                print("Not a pythag Trip!")
                
        except ValueError:
            print("Not an Integer, try again.")

        r = input("Again? (y/n): ")

pythag_trip()

        
        
