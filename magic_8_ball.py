import random, time
def magic_eight():
    n = 'y'
    
    while n != 'n':
        i = input("What do you want to ask the Magic 8 ball?")
        print(f"Your question: {i}")
        print(". . .")
        time.sleep(3)
        
        n = random.randint(0,14)
        if n == 1:
            print("Doesn't look so good")
        elif n == 2:
            print("You might want to reconsider the question")
        elif n == 3:
            print("You might want to reconsider the question")
        elif n == 4:
            print("Lets talk about it.")
        elif n == 5:
            print("No, go fuck yourself.")
        elif n == 6:
            print("Maybe when you fucking stop bitching.")
        elif n == 7:
            print("Yea sure.")
        elif n == 8:
            print("Stop, just stop")
        elif n == 9:
            print("Please no more questions!")
        elif n == 10:
            print("I dont really care.")
        elif n == 11:
            print("Fuhget about it!")
        elif n == 12:
            print("Yes")
        elif n == 13:
            print("Fuck off.")
        n = input("Again? (y/n): " )


magic_eight()
    
