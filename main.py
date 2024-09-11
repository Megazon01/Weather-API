import requests

# Define the API endpoint and parameters
url = ('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/barcelona?unitGroup=us&key'
       '=9CGHPTT9PD4LF8EV7TMELBHWC&contentType=json')
params = {
    'address': 'value1',
    'description': 'value2'
}

# Send a GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Process the JSON response
    data = response.json()
    place = data['address']
    day = data['days'][0]['datetime']
    temp_max = data['days'][0]['tempmax']
    temp_min = data['days'][0]['tempmin']
    temp = data['days'][0]['temp']
    content = (f"Weather in {place} on {day}: Average temperature: {round((temp - 32) * 5 / 9)} degrees, with a high of"
               f" {round((temp_max - 32) * 5 / 9)} degrees and a low of {round((temp_min - 32) * 5 / 9)} degrees.")
    print(content)
else:
    print(f'Error: {response.status_code}')
