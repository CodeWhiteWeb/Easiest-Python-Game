import random

def gameWin(comp, you):
    # declaring a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose r
    elif comp == 'r':
        if you=='p':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose p
    elif comp == 'p':
        if you=='s':
            return False
        elif you=='r':
            return True
    
    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='r':
            return False
        elif you=='p':
            return True

print('''Computer's Turn:
 Rock(r) Paper(p) or Scissors(s)? COMPUTER CHOSE A MOVE''')
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input('''Your Turn:
 Rock(r) Paper(p) or Scissors(s)?''')
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win! Yepppp")
else:
    print("You Lose! Loser")