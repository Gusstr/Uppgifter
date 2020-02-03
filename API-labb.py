import requests

first = requests.get("http://api.open-notify.org/astros.json")

number = str(first.json()['number'])
name = (first.json()['people'])

print("Hej och välkommen till denna sida. Just nu beffiner sig " + number + " personer i rymden:")

for x in name:
    person = x['name']
    location = x['craft']
    print(person + " befinner sig just nu på " + location)