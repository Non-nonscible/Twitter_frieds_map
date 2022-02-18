'''
Lab task 3
'''
import json
import folium
from geopy.geocoders import Nominatim
import fastapi
from fastapi import FastAPI

def read_file():
    '''
    Reads json file and converts it
    into a dict
    '''
    with open(r'C:\Users\Andrea\Programing_basics\Programing_Basics_2022\info.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def find():
    data = read_file()
    location = {}
    data = data['users']
    for user in data:
        username = user["screen_name"]
        loc = user['location'].split(',')[0]
        location[username] = loc
    return location

#print(find())

def location():
    '''
    Finds coordinates of given locations
    Example of outcome:
    {'maaaslenchenko': (41.900983100000005, 12.451167243196632),
    'linndfors': (-24.7761086, 134.755), 'demchvk': (36.7014631,
    -118.755997), 'mrkorchsorch': (51.5073219, -0.1276474)}
    '''
    data = find()
    geolocator = Nominatim(user_agent="friends_map.py")
    for name in data.keys():
        location = geolocator.geocode(data[name])
        data[name] = (location.latitude, location.longitude)
    return data

#print(location())

def create_map():
    '''
    Creates map
    '''
    data = location()
    map = folium.Map(tiles="Stamen Terrain",
    location=(0,0), zoom_start=0)
    layer1 = folium.FeatureGroup(name="Friends")
    for user in data:
        coord = data[user]
        layer1.add_child(folium.Marker(location=coord, popup=user, icon=folium.Icon()))
    map.add_child(layer1)
    map.add_child(folium.LayerControl())
    map.save(r'Lab_2\Lab_task_2-3\templates\Friends_map.html')

create_map()