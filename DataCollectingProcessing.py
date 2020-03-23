import os
import requests
from datetime import datetime
import json


# Global Parameters
LANG = 'hr'

# DarkSky.net API Parameters
DS_API_HOST = 'https://api.darksky.net/forecast'
DS_API_KEY = os.environ.get('DS_API_KEY')
DS_UNITS = 'si'
#DS_API_KEY = "846d7f1fd2a1f43bcc9d3e0bc87e10de"

# Google Maps Geocoding API Parameters
GM_ENDPOINT = 'https://maps.google.com/maps/api/geocode/json'
GM_API_KEY = os.environ.get('GM_API_KEY')
#GM_API_KEY = "AIzaSyBxOP6J5EdNYKw2SPS5UiN2OL5WOUvgWZw"

def convert_dates(dates):

    for i in range(len(dates)):
         dates[i] = dates[i].rstrip()
    return dates

def make_list(file):
    the_list = file.readlines()
    return the_list

def make_get_request(uri: str, payload):
    """
    Function to make a GET request to API Endpoint
    :param uri:
    :param payload:
    :return:
    """
    response = requests.get(uri, payload)
    if response.status_code != 200:
        return None
    else:
        return response.json()


def get_geo_data(address: str):
    """ Function to get coordinates from Google Maps Geocoding API
    :param address:
    :return:
    """
    payload = {'address': address, 'language': LANG, 'key': GM_API_KEY}
    response = make_get_request(GM_ENDPOINT, payload)

    if not response:
        return None
    #print(response)
    data = response['results'][0]
    formatted_address = data['formatted_address']
    lat = data['geometry']['location']['lat']
    lng = data['geometry']['location']['lng']

    return {'lat': lat, 'lng': lng, 'formatted_address': formatted_address}


def get_history_data(lat: str, lng: str, time:str):
    """ Function to get Forecast data from DarkSky.net API
    :param lat:
    :param lng:
    :return:
    """


    uri = DS_API_HOST + '/' + DS_API_KEY + '/' + str(lat) + ',' + str(lng) + ',' + time
    payload = {'lang': LANG, 'units': DS_UNITS}
    response = make_get_request(uri, payload)

    if not response:
        return None

    return response['daily']


def print_history(geo, forecast,weather_file):
    """
    Function to print daily weather forecast information
    :param geo:
    :param forecast:
    """
    print('Getting history for: ' + geo['formatted_address'])
    #print('Weekly Summary: ' + forecast['summary'])
    print()

    for day in forecast['data']:
        date = datetime.fromtimestamp(day['time'])


        #day_name = date.strftime("%A")

        summary = day['summary']
        temperature_min = str(round(day['temperatureMin'])) + 'ºC'
        temperature_max = str(round(day['temperatureMax'])) + 'ºC'
        icon = str(day["icon"])
        humidity = str(round(day['humidity']))
        pressure = str(round(day['pressure']))
        cloud_cover = str(round(day['cloudCover']))
        visibility = str(round(day['cloudCover']))
        uv_index = str(round(day["uvIndex"]))
        info = (geo["formatted_address"],date.strftime('%d/%m/%Y'))
        weather = {
            "city": {
            "info": info,
            "data":
            {
            "summary": summary,
            "temp_min": temperature_min,
            "temp_max": temperature_max,
            "icon": icon,
            "humidity": humidity,
            "pressure": pressure,
            "cloud_cover": cloud_cover,
            "visibility": visibility,
            "uv_index": uv_index
        } } }
        json.dump(weather, weather_file, ensure_ascii=False,indent=2)
        #print(
            #date.strftime('%d/%m/%Y') + ' (' + day_name + '): '  +  " " + temperature_min + ' - ' + temperature_max + " " + "with UV index:" + " " + uv_index
        #)
        #print()


def print_header():
    print('---------------------------------')
    print('     WEATHER HISTORY 1.O       ')
    print('---------------------------------')
    print()


def main():
    """
    Main Function
    """
    if DS_API_KEY is None:
        exit('Error: no location or env vars found')

    file = open("gradovi_izlaz.txt","r")
    cities = make_list(file)
    file.close()
    print_header()

    file = open("dates.txt", "r")
    dates = convert_dates(make_list(file))
    file.close()

    weather_file = open('weather_file.json', 'w') # writing JSON object

    for i in range(len(cities)):
        geo_data = get_geo_data(cities[i])

        if not geo_data:
            exit('Error: Address not found or invalid response')

        for j in range(len(dates)):

            history_data = get_history_data(geo_data['lat'], geo_data['lng'],dates[j])
            #print(history_data)

            if not history_data:
                exit('Error: Forecast not found or invalid response')

    # Print Output History information

            print_history(geo_data, history_data,weather_file)


if __name__ == '__main__':
    main()

