#Step 1
#Import the request module and pretty print module
import requests
from pprint import pprint 

#Step 2
#Declare a variable API_key to store our API
API_key = '7ebdfe064f6cc333bb138f9ac5745141'

#Step 3
#Declare avariable city to ask the user to input city and store the input data
city = input ("Enter a city: ")

#Step 4
#Declare a variable base_url to declare our API url 
base_url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

#Step 5
#Decalre a variable weather_data to request and get the base_url which contatins our API
#which will return a JSPN file
weather_data = requests.get(base_url).json()

#Step 6
#Pretty print the data
pprint(weather_data)