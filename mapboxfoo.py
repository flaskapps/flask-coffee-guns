import requests
from urllib.parse import quote

GEOCODE_API_URL = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{p}.json?access_token={t}'

# https://www.mapbox.com/api-documentation/#static
# https://api.mapbox.com/styles/v1/mapbox/streets-v10/static/url-https%3A%2F%2Fwww.mapbox.com%2Fimg%2Frocket.png(-76.9,38.9)/-76.9,38.9,15/1000x1000?access_token=your-access-token
STATIC_MAP_API_URL = 'https://api.mapbox.com/styles/v1/mapbox/streets-v10/static/url-{iconurl}({lng},{lat})/{lng},{lat},{pitch}/{width}x{height}?access_token={t}'

def geocode(place, token):
    placename = quote(place, safe='')
    url = GEOCODE_API_URL.format(p=placename, t=token)
    resp = requests.get(url)
    data = resp.json()
    features = data['features']
    feat = features[0]
    d = {}
    d['name'] = feat['place_name']
    d['longitude'] = feat['geometry']['coordinates'][0]
    d['latitude'] = feat['geometry']['coordinates'][1]
    return d


ICON_URL = 'https://compciv.github.io/stash/bouncy.png'

def static_map(longitude, latitude, token):
    imgurl = quote(ICON_URL, safe='')
    return STATIC_MAP_API_URL.format(
                            iconurl=imgurl,
                            lng=longitude,
                            lat=latitude,
                            pitch=15,
                            width=800,
                            height=500,
                            t=token)

