"""
API Call Functions

- API Calls for Google
- to be done, FourSquare, Yelp
- Functions:
    google_api()

"""

def google_api(df, num_neighbourhoods):
    """
    Google API Call returns a concatenated payload DataFrame from n # of neighbhourhoods
    Built specifically to work with output from json_prep() in json_parse.py
    Google API Call only returns 20 records, but has an option for loading 2 more 'pages'
    This gives a total of 60 records per API call, but functionality is not made yet
    next_page_token is fed into the api call, as seen below in the commented out code

        Parameters:
            df (DataFrame): DataFrame with categories 'borough', 'neighbourhood', 'latitude', 'longitude'
            num_neighbourhoods (int): Interger which runs API call n time for the n top rows from the dataframe

        Returns:
            payload_list (DataFrame): Concatenated dataframe with all runs stacked vertically
    """

    payload_list = []
    address = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'

    for n in range(num_neighbourhoods):
        
        payload = {}
        headers = {}

        # lat and long pulled from the parsed df_nyc file
        # location names are collected to append to end of DataFrame
        lat = df['latitude'][n]
        long = df['longitude'][n]
        neighbourhood = df['neighbourhood'][n]
        borough = df['borough'][n]

        # can consider parameters to input here, change type (restaurant) or radius (1500m)
        # maybe move these outside the api call as parameters?
        location = f'location={lat}%2C{long}'
        radius = '&radius=1500'
        place_type = '&type=restaurant'
        
        # change api key to your key
        api_key = f'&key={os.environ["gmaps_api"]}'

        append = location+radius+place_type
        search = address+append+api_key

        response = requests.request("GET", search, headers=headers, data=payload)
        payload = response.json()

        # payload is normalized and has location data appended onto results as extra columns
        df_payload = pd.json_normalize(payload['results'])
        df_payload['neighbourhood'] = neighbourhood
        df_payload['borough'] = borough
        payload_list.append(pd.DataFrame(df_payload))
    
        print(response.status_code)

        # np_token = payload['next_page_token']
        
    # if payload['next_page_token'] != None:
    #     search = f'{address}pagetoken={np_token}{api_key}'
    #     response = requests.request("GET", search, headers=headers, data=payload)
    #     payload = response.json()
    #     np_token = payload['next_page_token']
    #     df_payload = pd.json_normalize(payload['results'])
    
    # final payload list is converted to a stacked DataFrame
    payload_df = pd.concat(payload_list, ignore_index=True)

    return payload_df