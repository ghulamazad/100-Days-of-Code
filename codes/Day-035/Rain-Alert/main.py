import requests
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
api_key = os.environ['API_KEY']
FROM_NUMBER = os.environ['FROM_NUMBER']
TO_NUMBER = os.environ['TO_NUMBER']

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 20.593683,
    "lon": 78.962883,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:11]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, Remember to bring an ☂",
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )

    print(message.status)
