import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import ttkbootstrap as tb

root = tb.Window(themename="morph")
root.title("Breeze: A Weather App")
root.geometry("400x400")

API_key = "c5f14d156c50ba4dca84020be3bdffbd"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error","City not Found")
        return None

    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temp = weather['main']['temp'] - 273.15
    desc = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url,temp,desc,city,country)
    


def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return 

    icon_url, temp, desc, city, country = result
    loc_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url,stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon
 

    temp_label.configure(text=f"Temperature: {temp:.2f}°C")
    desc_label.configure(text=f"Description: {desc}")
    


city_entry = tb.Entry(root,font="Helvetica,18")
city_entry.pack()

we_button = tb.Button(root,text="Search",command=search,bootstyle="warning")
we_button.pack()

loc_label = tb.Label(root,font="Helvetica,25")
loc_label.pack()

icon_label = tb.Label(root)
icon_label.pack()

temp_label = tb.Label(root,font="Helvetica,20")
temp_label.pack()

desc_label = tb.Label(root,font="Helvetica,20")
desc_label.pack()

root.mainloop()

