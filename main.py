# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

parameters = {
    "lat" : LAT,
    "lon": LONG,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(url= "https://api.openweathermap.org/data/2.5/forecast", params = parameters)
response.raise_for_status()
data = response.json()["list"]
weather = [day["weather"][0]["id"] for day in data]


umbrella = any(num <700 for num in weather)
if umbrella:
    message = client.messages.create(
        body="Bring an Umbrella!",
        from_=f"whatsapp:{PHONE}",
        to="whatsapp:+16476161716",
    )
    print(message.status)
