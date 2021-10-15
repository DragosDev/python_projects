#Ticket Calculator
#Step 1
#Print a welcome message on the screen
print("Welcome to the rollercoaster")
#Printing the emoji smile face 5 times
print("\U0001f600 "*5)

#Step 2
#Ask the user what is the weight and store it into a variable
#named height of type int(integer)
height = int(input("What is your height? \n"))

#Step 3
#If the user is less than 120 cm they will not be allowed to go 
#on the rollercoaster
if height >= 120:
  print("You can ride the rollercoaster")

#Step 4 
#If the height of the user is 120 or more then ask if they want to #buy the ticket with an Y or N choice and store the answer into a 
#variable called question
  question = input("Do you want to buy a ticket (Y or N) ?\n")

#Step 5
#Add a nested if statement and if question is Y then procees to #ask What is your age , if the question is N the stop the #execution of the program and print Thanks on the screen
  if question == "Y":
      age = int(input("What is your age? \n"))
#Step 6
#If the age is less than 12 the user will pay 5
      if age < 12:
        print("You need to pay 5.")
        print("Enjoy your ride.")
#Step 6
#Here we are using the nested statement elif the age is less or 
#equal to 18 the user need to pay 7.
#In this way we are covering the payment amount for the age #between 12 and 18.       
      elif age <= 18:
        print("You need to pay 7.")
        print("Enjoy your ride.")
#Step 7
#Else if the user is more than 18 they need to pay 12.        
      else:
        print("You need to pay 12") 
        print("Enjoy your ride.")
  elif question == "N":
    print("Thanks")
  
else:
  print("Sorry you are not allowed to ride the rollercoaster")  