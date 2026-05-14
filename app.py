import requests

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        print("------------------------")
        print("Weather:", response.text)
        print("------------------------")
    except:
        print("Something went wrong! Check your city name.")

def main():
    print("=============================")
    print("   Sandesh's Weather App 🌤️  ")
    print("=============================")
    
    while True:
        city = input("Enter city name (or 'quit' to exit): ")
        if city.lower() == "quit":
            print("Goodbye!")
            break
        get_weather(city)

main()