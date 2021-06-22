import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textField.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=677ba9dcc6a62ef4306eeeff79be5f92"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']- 273.15)
    mintemp = int(json_data['main']['temp_min'] - 273.15)
    maxtemp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity= json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%H:%M:%S %p', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%H:%M:%S %p', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) +  u"\N{DEGREE SIGN}"+"Celcius"
    final_data = "\n" + "Max Temp: " + str(maxtemp) + "\n" + "Min Temp: " + str(mintemp) + "\n" + "Humidity : " + str(humidity) + "\n" + "Pressure: " + str(pressure) + "\n" + "Wind speed: " + str(wind) + "\n" + "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset)
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f1 = ("poppins", 15, "bold")
f2 = ("poppins", 35, "bold")

textField = tk.Entry(canvas, font = f2)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)


label1 = tk.Label(canvas, font = f2)
label1.pack()
label2 = tk.Label(canvas, font = f1)
label2.pack()

canvas.mainloop()
