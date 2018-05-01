from flask import Flask
from flask import abort, render_template, request
from os import environ
import requests
from urllib.parse import quote


MAPBOX_TOKEN = environ.get('MAPBOX_ACCESS_TOKEN')
myapp = Flask(__name__)


API_URL = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{p}.json?access_token={t}'

def geocode_foo(place, token=MAPBOX_TOKEN):
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
    if not MAPBOX_TOKEN:
        abort(428)

    q = request.args['query']
    rawhtml = render_template('geocode.html',
                               query=q,
                               result=geocode_foo(q),
                               api_token=MAPBOX_TOKEN)
    return rawhtml



@myapp.errorhandler(428)
def mapbox_token_env_not_set(err):
    return """
    <h1>Error: Need Mapbox API Key</h1>

    <p>This app requires you to have a Mapbox account and to
    get a Mapbox API key, and then to define the following
    variable in your <code>.bash_profile</code>:</p>

    export MAPBOX_ACCESS_TOKEN='pk.blahblah'
    """


if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
