from flask import Flask
from flask import abort, render_template, request
from os import environ
import mapboxfoo as foo

MAPBOX_TOKEN = environ.get('MAPBOX_ACCESS_TOKEN')
myapp = Flask(__name__)



@myapp.route("/")
def homepage():
    rawhtml = render_template('homepage.html')
    return rawhtml

@myapp.route("/zip/<zipcode>")
def by_zipcode(zipcode):
    starbucks=get_starbucks_by_zip(zipcode)
    rawhtml = render_template('zipcode.html', starbucks=starbucks)
    return rawhtml

# @myapp.route("/map")
# def geocode_map():
#     if not MAPBOX_TOKEN:
#         abort(428)

#     q = request.args['q']
#     result = foo.geocode(q, token=MAPBOX_TOKEN)
#     rawhtml = render_template('map.html',
#                                query=q,
#                                mapmode=request.args['mapmode'],
#                                result=result,
#                                api_token=MAPBOX_TOKEN)
#     return rawhtml

# @myapp.route("/map-static")
# def geocode_staticmap():
#     if not MAPBOX_TOKEN:
#         abort(428)

#     q = request.args['query']
#     result = foo.geocode(q, token=MAPBOX_TOKEN)
#     mapimg = foo.static_map(longitude=result['longitude'],
#                             latitude=result['latitude'],
#                             token=MAPBOX_TOKEN)



#     rawhtml = render_template('map-static.html',
#                                query=q,
#                                mapimg=mapimg,
#                                result=result,)
#     # api token is generated and embedded in mapurl for now
#     # but probably not best practice


#     return rawhtml


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
