import requests
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry('500x500')
root.config(bg='dark slate grey') # background color of the app

location_label = Label(root, text="Enter location: ") # the loction a user wants to check weather for
location_label.place(x=10,y=10)
location_entry= Entry(root)
location_entry.place(x=150,y=10)
if location_entry.get() == " ": # catch the possibility of not entering anything on the screen.
    messagebox.showinfo(title=None, text="Please enter a valid location")

def check_weather():

    response=requests.get("http://api.weatherapi.com/v1/current.json?key=127cf31b9f7c4814aea71157210706&q=" + location_entry.get()+ "&aqi=no")
    data = response.json() # insert the location from user on the api url

    region_label = Label(root, text="Region: ")
    region_label.place(x=10,y=150)
    region_entry = Entry(root)
    region_entry.place(x=100,y=150)
    region_entry.insert(0,data['location']['region']) # extract location by region from the api dictionary

    country_label = Label(root, text="Country: ")
    country_label.place(x=10,y=200)
    country_entry = Entry(root)
    country_entry.place(x=100,y=200)
    country_entry.insert(0,data['location']['country']) # extract location by country from the api

    temp_c = Label(root, text=" Temperature in (C):")
    temp_c.place(x=10, y=250)
    temp_c_enrty=Entry(root)
    temp_c_enrty.place(x=150,y=250)
    temp_c_enrty.insert(0,data['current']['temp_c']) # extract current temperature in C

    temp_f = Label(root, text='Temperature in (F): ')
    temp_f.place(x=10,y=300)
    temp_f_entry= Entry(root)
    temp_f_entry.place(x=150,y=300)
    temp_f_entry.insert(0,data['current']['temp_f']) # extract current temperature in F

    condition_label = Label(root, text="Condition:")
    condition_label.place(x=10,y=350)
    condition_entry = Entry(root)
    condition_entry.place(x=150,y=350)
    condition_entry.insert(0,data['current']['condition']['text']) # extract current condition

    humidity_label=Label(root,text="Humidity")
    humidity_label.place(x=10,y=400)
    humidity_entry = Entry(root)
    humidity_entry.place(x=150,y=400)
    humidity_entry.insert(0,data['current']['humidity']) # extract current humidity

    def clear(): # function to clear all the entries
        region_entry.delete(0,END)
        location_entry.delete(0,END)
        country_entry.delete(0,END)
        temp_c_enrty.delete(0,END)
        temp_f_entry.delete(0,END)
        condition_entry.delete(0,END)
        humidity_entry.delete(0,END)

    exit_btn = Button(root, text="clear", command= clear)
    exit_btn.place(x=150,y=70)


weather_btn = Button(root, text= "Check weather", command=check_weather)
weather_btn.place(x=10,y=70)


root.mainloop()

