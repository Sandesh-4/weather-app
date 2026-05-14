import requests

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        print("Weather:", response.text)
    except:
        print("Something went wrong! Check your city name.")

def main():
    print("Welcome to Weather App!")
    print("------------------------")
    city = input("Enter city name: ")
    get_weather(city)

main()