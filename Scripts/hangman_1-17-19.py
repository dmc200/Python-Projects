import random

#check if we want to play again. 
def replay():
    again = '' 
    while again != 'y' and again != 'n':
        again = input("Do you want to play again? (Y/N): ").lower()
        
    if again == 'y':
        return True
    else:
        return False
    
while True:
    answerList = ["world","look","hello", "goodbye"]

    random.shuffle(answerList)

    answer = answerList[0]

    display = []

    answer = list(answer)

    for i in range(len(answer)):
        display.append('_')

    
    counter = len(answer) - 1

    while counter > 0 :
        if '_' not in display:
                print("You won")
                break
            
        print(display)
        choice = input("Choose a letter: ").lower()
        if choice in answer: 
            for x,y in enumerate(answer):
                if y == choice:
                    display[x] = choice
        else:
            counter -= 1
            print(f"You guessed wrong you have {counter} choices left")
            

    play_again = replay()
    
    if play_again:
        continue
    else:
        break
    
    


            
    

    

