

import os

from requests_html import HTML, HTMLSession
from twilio.rest import Client

#with open('simpleweb2.html') as html_file:
#    source = html_file.read()
#    html = HTML(html=source)
#
#print(html.text)
#forecast = html.find('div.forecast', first=True)
#headline = forecast.find('h2', first=True).text
#Summary = html.find('p', first=True).text
#
#print(headline)
#print(Summary)

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