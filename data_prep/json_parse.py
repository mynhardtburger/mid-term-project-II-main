"""
Data parsing script

- Script that takes data from file 'nyc_geo.json' and parses it into two DataFrames
- Functions:
    json_prep()

"""

from pandas.io.json import json_normalize
import json
import pandas as pd

def json_prep():

    """
    Returns a parsed dataframe, and a non-parsed dataframe from the nyc_geo.json

        Parameters: 
            None

        Returns:
            df_nyc (pd.DataFrame): Parsed dataframe with borough, neighbourhood, lat+long
            df_org (pd.DataFrame): Non-parsed dataframe with all original components
    """

    dir = ''

    with open(dir+'nyc_geo.json') as json_data:
        data_json = json.load(json_data)

    df_org = pd.json_normalize(data_json['features'])

    lat_long = pd.DataFrame(df_org["geometry.coordinates"].to_list(), columns=['longitude', 'latitude'])
    df_nyc = pd.merge(df_org[['properties.borough', 'properties.name']], lat_long, left_index=True, right_index=True)
    df_nyc = df_nyc.rename(columns={'properties.borough': 'borough', 'properties.name': 'neighbourhood'})

    return df_nyc, df_org
