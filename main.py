import random
print("Welcome to the coin guessing Game!") 
print("Choose a method to toss the coin:")
print("1. Using random.randint()")
print("2. Using random.random()")
choice=input("Enter your choice (1 or 2): \n ")
if choice!="1" and choice!="2":
  print("Invalid choise. Please select either 1 or 2")
else:
  if choice== "1":
    randint=random.randint(0,1)
    if randint==1:  
      computer_choise="tails"
    else:
      computer_choise="heads"
  else:
    random_=random.random()
    if random_>=0.5:
      computer_choise="tails"
    else:  
      computer_choise="heads"
  guess=input("Enter your Guess (Heads or Tails)\n ").lower()
  if guess=="heads"or guess=="tails":
    if guess==computer_choise: 
      print("Conngratulations! You won!")
    else:
      print("Sorry, You lost!")
    print(f"The computer's coin toss result was : {computer_choise}")
  else: 
    print("Invalid choise. Please select either Heads or Tails")