import random
def game(userinput):
    choices=['rock','paper','scissors']
    compchoice=random.choice(choices)
    if compchoice==userinput:
        print("Tie!")
    elif userinput=='rock':
        if compchoice=='paper':
            print("Computer wins!")
        else:
            print("You win!")
    elif userinput=='paper':
        if compchoice=='rock':
            print("Computer wins!")
        else:
            print("You win!")
    elif userinput=='scissors':
        if compchoice=='rock':
            print("Computer wins!")
        else:
            print("You win!")
n=1
while(n==1):
    userinput=input("Enter your choice between rock,paper,scissors")
    if userinput not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please try again.")
        continue
    game(userinput)
    n=int(input("Press 1 to play,0 to quit"))
    