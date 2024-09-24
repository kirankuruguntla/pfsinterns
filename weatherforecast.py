import requests
import json
import tkinter
 
API_KEY = 'd26e8139afe0475ca10185046241001'
 
def fetch_weather_data(city):
    base_url = 'https://api.weatherapi.com/v1/current.json'
    complete_url = f"{base_url}?key={API_KEY}&q={city}"
    response = requests.get(complete_url)

    return response.json()
 
def display_weather_data():

    input_city = input_field.get()
    weather_data = fetch_weather_data(input_city)

    if "error" in weather_data:
        weather_label.config(text=f"No matching location found.")
        return

    input_value = input_field.get()

    weather_label.config(
        text=f"City: {
            weather_data["location"]["name"]
            }\nTemperature: {
                weather_data["current"]["temp_f"]}\u00B0F/{weather_data["current"]["temp_c"]
                }\u00B0C\nHumidity: {weather_data["current"]["humidity"]}%\nWind speed: {weather_data["current"]["wind_mph"]}mph/{weather_data["current"]["wind_kph"]}kph")

root = tkinter.Tk(screenName=None,  baseName=None,  className='Weather forecast',  useTk=1)

root.title("Weather Forecasting App")
root.geometry("400x200")

input_label = tkinter.Label(root, text="Enter city:")
input_label.pack()

input_field = tkinter.Entry(root)
input_field.pack()

submit_button = tkinter.Button(root, text="Get Weather", command=display_weather_data)
submit_button.pack()

weather_label = tkinter.Label(root, text="")
weather_label.pack()

root.mainloop();