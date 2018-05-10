import pandas as pd
from pathlib import Path

ATF_DATA_PATH = Path('static', 'data', 'atf_firearm_dealers.csv')
STARBUCKS_DATA_PATH = Path('static', 'data', 'starbucks.csv')

def get_firearms_dealers():
    df = pd.read_csv(ATF_DATA_PATH,
                     dtype='str',
                     usecols=['Lic Regn', 'Lic Dist', 'Lic Cnty', 'Lic Type', 'License Name',
                                             'Business Name', 'Premise City', 'Premise State', 'Premise Zip Code'])

    return df[df['Lic Type'] == '01'].to_dict('records')

