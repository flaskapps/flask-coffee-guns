from flask import Flask
from flask import render_template, request
from os import environ
import requests 
from urllib.parse import quote


MAPBOX_TOKEN = environ.get('MAPBOX_ACCESS_TOKEN')
myapp = Flask(__name__)


API_URL = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{p}.json?access_token={t}'

def geocode(place, token=MAPBOX_TOKEN):
    url = API_URL.format(p=quote(place), t=token)
    resp = requests.get(url)
    data = resp.json() 
    features = data['features']
    feat = features[0]
    d = {}
    d['name'] = feat['place_name']
    d['longitude'] = feat['geometry']['coordinates'][0]
    d['latitude'] = feat['geometry']['coordinates'][1]
    return d


@myapp.route("/")
def homepage():
    rawhtml = render_template('homepage.html')
    return rawhtml


@myapp.route("/geocode")
def geocode():
    place = request.args['place']
    rawhtml = render_template('geocode.html', place=place, api_token=MAPBOX_TOKEN)
    return rawhtml


if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
