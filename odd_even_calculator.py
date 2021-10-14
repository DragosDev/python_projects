#Step 1
#Ask the user to input the number and store it into a variable #called number
message =("Welcome to our Odd - Even Number Checker")
print(message)
number = int(input("Which number do you want to check? \n"))

#Step 2
#Define the conditional usign the modulo % to divide by 2 and #check if the number is equal to an even number 0. 
if number % 2 == 0:
#Step 3
#Use the f string to display the number result into the string.  
   print(f"{number} is a even number.")
else:
  print(f"{number} is an odd number.")