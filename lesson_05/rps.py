import sys
import random
from enum import Enum 

print("WELCOME TO THE RPS GAME !!")
statement = """
Pick one: 

1. Rock 
2. Paper
3. Scissors 
"""
print(statement)
question = input(f"Please pick one of the 3 above:\n")
player = int(question)
 

#program picks random number from the list
python =  random.randrange(1,3)

print(f"You chose:  {player}") 
print(f"Computer chose:  {python}") 

if player == 1 and python == 3:
    print("You Wins !")
elif player == 2 and python == 1:
     print("You Wins !")
elif player == 3 and python == 2:
      print("You Wins !")
elif player == python:
     print("its a draw  mate haha !")
else:
     print("Computer Wins")

