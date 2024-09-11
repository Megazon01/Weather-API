# Weather API

Collect the highest, lowest and average temperture in Barcelona for any given day, and email the results to yourself!

## **Features:** 
Once the program runs, it will automatically:
- Scrape temperature data from https://www.visualcrossing.com/weather/weather-data-services
- Email the resurlts to yourself in a well formatted email

### Notes:
- The program can use a different API link to access weather data for any city the user wants
- Depending on the user's email provider, the smpt_port and smpt_server variables in the send_email.py file may need renaming (they are configured for gmail)
- For the password variable in the send_email.py file, the user might need to create an app password from their email provider
