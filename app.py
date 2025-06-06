import streamlit as st
import datetime
import requests
import json

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
with st.form('taxifare-params'):
    pickup_date = st.date_input("pickup date", datetime.date(2019, 7, 6))
    pickup_time = st.time_input('pickup time', datetime.time(8, 45))
    dropoff_date = st.date_input("dropoff date", datetime.date(2019, 7, 6))
    dropoff_time = st.time_input('dropoff time', datetime.time(8, 45))
    pickup_longitude = st.number_input('pickup longitude')
    pickup_latitude = st.number_input('pickup latitude')
    dropoff_longitude = st.number_input('dropoff longitude')
    dropoff_latitude = st.number_input('dropoff latitude')
    passenger_count = st.number_input('passenger count', step=1)
    submit = st.form_submit_button('submit')


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

# dictionary for parameters for the api

if submit:
    pickup_datetime = f'{pickup_date} {pickup_time}'
    dropoff_datetime = f'{dropoff_date} {dropoff_time}'
    passenger_count = int(passenger_count)
    params = dict(
        pickup_datetime=pickup_datetime,
        dropoff_datetime=dropoff_datetime,
        pickup_longitude=pickup_longitude,
        pickup_latitude=pickup_latitude,
        dropoff_longitude=dropoff_longitude,
        dropoff_latitude=dropoff_latitude,
        passenger_count=passenger_count
    )
    # call api using requests package
    # Make the GET request
    response = requests.get(url, params=params)
    response_dict = json.loads(response.text)

    st.write('Your fair is: ', response_dict['fare'])
