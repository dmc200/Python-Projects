'''
def div42by(divideBy):
    return 42 /divideBy


try: 
    print(div42by(1))
    print(div42by(1))
    print(div42by(0))
    print(div42by(1))

except ZeroDivisionError:
    print("You have tried to divide by 0")

finally:
    print("This is finally done")
    
'''
play = True
while play:
    print("How many cats do you have?")
    
    numCats = input()

    try:
        if int(numCats) >= 4:
            print("Wow that is a lot of cats!")
        elif int(numCats) < 0:            
            myError = ValueError('# of cats should be a positive number')
            raise myError
        else:
            print("Not that many cats")
            break
    except ValueError:
        print("Not in integer, try again")

    play = input("Again?").lower()
    if play == 'y':
        play = True
    else:
        play = False
        
        
