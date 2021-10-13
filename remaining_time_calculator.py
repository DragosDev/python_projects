#Step 1
#Define a variable age type input to ask the user What is the current age

age = input ("What is your current age?")

#Step 2
#Define a variable age_as_int and convert age to and integer by using int
age_as_int = int(age)

#Step 3
#Define a vaiable named years_remaining equal with 90(the age tha we supposed to live) and substract the varibale age_as_int.
years_remaining = 90 - age_as_int

#Step 4
#There are 365 days in a year, 52 weeks and 12 months in one year
#Define three variables to calculate the years_remaining * 360 days , * 52 weeks and 12 months. 
days_remaining = years_remaining * 360
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

#Step 3
#Define a variabled named message and use an f string to add your variables inside of the string
#An f-String in Python is helping to add various variables in our string , in our case days_remaining, weeks_remaining, months_remaining.
message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} month"

print(message)