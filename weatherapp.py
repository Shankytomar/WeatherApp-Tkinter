from tkinter import *
import tkinter as tk
from datetime import datetime
import pytz
import requests
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim

root=Tk()
root.title('Weather App')
root.geometry('900x500+300+200')
root.resizable(True,True)


def getlocation():
    print('triggered')
    
    city=textfield.get()

    geolocator = Nominatim(user_agent='geoapiExercises')
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    print(result)
    '''Asia/Kolkata
        {
        'coord': {'lon': 78.6667, 'lat': 27.6333},
        'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}],
        'base': 'stations',
        'main': {'temp': 303.85, 'feels_like': 309.13, 'temp_min': 303.85,
                 'temp_max': 303.85,'pressure': 1002, 'humidity': 67,
                 'sea_level': 1002, 'grnd_level': 983},
        'visibility': 10000,
        'wind': {'speed': 4, 'deg': 83, 'gust': 7.54},
        'clouds': {'all': 100},
        'dt': 1659628988,
        'sys': {'country': 'IN', 'sunrise': 1659571793, 'sunset': 1659619979},
        'timezone': 19800,
        'id': 1271992,
        'name': 'Etah',
        'cod': 200
        }
 triggered '''
    
    '''
    home=pytz.timezone(result)
    local_time =datetime.now(home)
    current_time = local_time.strftime('%I %M %p')
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
    print(home)'''
    
    #api
    api='https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=4e9d74b1687ba160e83b80ab5c07c83e'  
    json_data = requests.get(api).json()
    print(json_data)
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp))
    c.config(text=(condition,'|','FEELS','LIKE',temp))
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)
#search box
Search_image = PhotoImage(file ='resouces\search.png')
myimage = Label(image=Search_image)
myimage.place(x=20,y=10)

textfield = tk.Entry(root,justify = 'center', width=17,font=('poppins',25,'bold'),fg='white',bg='#404040',border=0)
textfield.place(x=50,y=25)
textfield.focus()

Search_icon = PhotoImage(file='\resouces\search_icon.png')
myimage_icon = Button(image=Search_icon,command=getlocation,borderwidth=0,cursor='hand2',bg='#404040')
myimage_icon.place(x=390,y=24)

#logo
Logo_image = PhotoImage(file='resouces/logo.png')
logo = Label(image=Logo_image)
logo.place(x=150,y=100)

#Bottom box
Frame_image = PhotoImage(file='resouces/box.png')
frame_myimage = Label(image=Frame_image)
#frame_myimage.pack(padx=5,pady=5,side=BOTTOM)
frame_myimage.place(x=50,y=380)

#label
l1= Label(root,text='WIND',font=('Helvetica',15,'bold'),bg='#1ab5ef',fg='white')
l1.place(x=120,y=400)

l2= Label(root,text='HUMIDITY',font=('Helvetica',15,'bold'),bg='#1ab5ef',fg='white')
l2.place(x=250,y=400)

l3= Label(root,text='DESCRIPTION',font=('Helvetica',15,'bold'),bg='#1ab5ef',fg='white')
l3.place(x=430,y=400)

l4= Label(root,text='PRESSURE',font=('Helvetica',15,'bold'),bg='#1ab5ef',fg='white')
l4.place(x=650,y=400)

t=Label(font=('arial',70,'bold'),fg='#ee666d')
t.place(x=400,y=150)
c=Label(font=('arial',15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=('arial',20,'bold'),bg="#1ab5ef")
w.place(x=127,y=430)
h=Label(text="...",font=('arial',20,'bold'),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=('arial',12,'bold'),bg="#1ab5ef")
d.place(x=455,y=430)
p=Label(text="...",font=('arial',20,'bold'),bg="#1ab5ef")
p.place(x=670,y=430)


