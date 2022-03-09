# rpc.py
import random

CHOICES = ["rock", "paper", "scissors"]

print("Make your throw!")
user_choice = input(  "Type rock, paper, or scissors: ")

if user_choice in CHOICES:
  computer_choice = random.choice(CHOICES)
  print(
    f"\nYou threw  '{user_choice}', the computer threw '{computer_choice}'"
  )
else:
  print(f"\nYou typed '{user_choice}', which isnt a valid throw.")

#WINS AND LOSES

#COMPUTER WINS
if  user_choice == "rock" and computer_choice == "paper":
  print("Computer won!")

if  user_choice == "scissors" and computer_choice == "rock":
  print("Computer won!")

if  user_choice == "paper" and computer_choice == "scissors":
  print("Computer won!")

#USER WINS

if  user_choice == "paper" and computer_choice == "rock":
  print("User won!")

if  user_choice == "rock" and computer_choice == "scissors":
  print("User won!")

if  user_choice == "scissors" and computer_choice == "paper":
  print("User won!")
