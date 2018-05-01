from flask import Flask
from flask import render_template, request
from os import environ

MAPBOX_TOKEN = environ.get('MAPBOX_ACCESS_TOKEN')

myapp = Flask(__name__)

def parse_geocode_response(txt):
    """
    Return a dictionary
    """


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
