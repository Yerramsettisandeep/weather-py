import requests, json

apiKey = "8fde9b7583fc60dab81c1a7c050a8daa"

baseURL = "https://api.openweathermap.org/data/2.5/weather?q="

cityName = input("Enter your city : ")

completeURL = baseURL + cityName + "&appid=" + apiKey

response = requests.get(completeURL)

data = response.json()

print(data)

print("current Temperature ",data["main"]["temp"])
print("current Temperature feels ",data["main"]["temp"])
print("maximum Temperature ",data["main"]["temp"])
print("minimum Temperature ",data["main"]["temp"])
