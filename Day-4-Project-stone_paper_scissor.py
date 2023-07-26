rock = '''
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
'''

paper = '''
    ___
---'   _)_
          __)
          ___)
         ___)
---.____)
'''

scissor = '''
    ___
---'   _)_
          __)
       ____)
      (__)
---._(__)
'''

# Write your code below this line 👇

import random

print("****WELCOME TO ROCK,PAPER AND SCISSOR GAME____")
print("")
alpha = int(input("What do you choose? enter 1 for rock,2 for paper and 3 for scissor.\n"))
a = random.randint(1, 3)

if alpha == 1 and a == 2:
    print(rock)
    print("Your choice is rock.")
    print("computer choice:")
    print(paper)
    print("computer choice is paper.")
    print("You lose!!")


elif alpha == 2 and a == 3:
    print(paper)
    print("Your choice is paper.")
    print("computer choice:")
    print(scissor)
    print("computer choice is scissor.")
    print("You lose!!")


elif alpha == 3 and a == 1:
    print(scissor)
    print("Your choice is scissor.")
    print("computer choice:")
    print(rock)
    print("computer choice is rock.")
    print("You lose!!")


elif alpha == 1 and a == 3:
    print(rock)
    print("Your choice is rock.")
    print("computer choice:")
    print(scissor)
    print("computer choice is scissor.")
    print("You win!!")


elif alpha == 3 and a == 2:
    print(scissor)
    print("Your choice is scissor.")
    print("computer choice:")
    print(paper)
    print("computer choice is paper.")
    print("You win!!")


elif alpha == 2 and a == 1:
    print(paper)
    print("Your choice is paper.")
    print("computer choice:")
    print(rock)
    print("computer choice is rock.")
    print("You win!!")
