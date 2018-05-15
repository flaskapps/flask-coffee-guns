import pandas as pd
from pathlib import Path
from math import sin, cos, sqrt, atan2, radians
EARTH_RADIUS_IN_KM = 6373.0


ATF_DATA_PATH = Path('static', 'data', 'atf_firearm_dealers.csv')
STARBUCKS_DATA_PATH = Path('static', 'data', 'starbucks.csv')

def calc_geo_distance(longitude_1, latitude_1, longitude_2, latitude_2):
    # explanation
    # https://github.com/compciv/project-stanford-quakebot/tree/master/steps/calc_geo_distance


    lat1 = radians(latitude_1)
    lon1 = radians(longitude_1)
    lat2 = radians(latitude_2)
    lon2 = radians(longitude_2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = EARTH_RADIUS_IN_KM * c
    return distance


def get_starbucks():
    df = pd.read_csv(STARBUCKS_DATA_PATH)
    return df.to_dict('records')


def get_starbucks_by_zip(zipcode):
    mylist = []
    for s in get_starbucks():
        if zipcode in s['Postal Code']:
            mylist.append(s)
    return mylist


def get_starbucks_by_state(state):
    mylist = []
    starbucks = get_starbucks()
    for s in starbucks:
        if state in s['Country Subdivision']:
            mylist.append(s)
    return mylist


def get_nearest_starbucks(mylng, mylat):
    starbucks = get_starbucks()
    return sorted(starbucks, key=lambda x: calc_geo_distance(mylng, mylat, x['Longitude'], x['Latitude']))


def get_firearms_dealers():
    df = pd.read_csv(ATF_DATA_PATH,
                     dtype='str',
                     usecols=['Lic Regn', 'Lic Dist', 'Lic Cnty', 'Lic Type', 'License Name',
                              'Business Name', 'Premise City', 'Premise State', 'Premise Zip Code'])

    df = df[df['Lic Type'] == '01']
    return df.to_dict('records')




