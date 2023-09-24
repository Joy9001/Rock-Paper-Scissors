import random
from sign import rock, paper, scissors


print("Welcome to the Ultiamte Rock Paper Scissors Challenge!\n")

user = input("What is your choice? (type 'rock', 'paper' or 'scissors') ")

print("You choose:\n")
if user == 'rock':
  print(f"{rock}\n")
elif user == 'paper':
  print(f"{paper}\n")
elif user == 'scissors':
  print(f"{scissors}\n")

options = ['rock','paper','scissors']
comp = random.choice(options)

if comp == 'rock':
  print(f"Computer choose:\n{rock}\n")
  if user == 'rock':
    print("Woah a TIE!\n")
  elif user == 'paper':
    print("Congratulation! you WON!\n")
  elif user == 'scissors':
    print("Sorry! you LOSE!\n")
  exit()
elif comp == 'paper':
  print(f"Computer choose:\n{paper}\n")
  if user == 'rock':
    print("Sorry! you LOSE!\n")
  elif user == 'paper':
    print("Woah a TIE!\n")
  elif user == 'scissors':
    print("Congratulation! you WON!\n")
  exit()
elif comp == 'scissors':
  print(f"Computer choose:\n{scissors}\n")
  if user == 'rock':
    print("Congratulation! you WON!\n")
  elif user == 'paper':
    print("Sorry! you LOSE!\n")
  elif user == 'scissors':
    print("Woah a TIE!\n")
  exit()