
import os

from requests_html import HTML, HTMLSession
from twilio.rest import Client

twilio_num = os.environ['TWILIO_NUMBER']
personal_num = os.environ['MY_NUMBER']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

def send_goodtimes():
    def send_forecast():
        session = HTMLSession()
        r = session.get('http://www.bom.gov.au/act/forecasts/canberra.shtml')
        forecast = r.html.find('div.day.main', first=True)
        return(forecast.text)
    message = client.messages \
            .create(
                body=send_forecast(),
                from_=twilio_num,
                to=personal_num
            )
    print(message.sid)
