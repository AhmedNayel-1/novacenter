# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client



account_sid = "ACd9c1171a2f222163a125b83bc79a088d"
auth_token = "10e4e67fb0e9a29da0ed13cacbcda6cb"
client = Client(account_sid, auth_token)
def send_whatsapp_messages(body,to):
    message = client.messages.create(
            #media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
            from_='whatsapp:+14155238886',
            body=body,
            to= f'whatsapp:{to}'
        )

    print(message.sid)





from nexmo import Sms

NEXMO_API_KEY="2a456ef0"
NEXMO_API_SECRET="F4AG4ieSVrbd4yka"
sms = Sms(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)
def send_sms_messages(to):
    sms.send_message({
                "from": "NEXMO_BRAND_NAME",
                "to": to,
                "text": "A text message sent using the Nexmo SMS API",
    })



import nexmo

client = nexmo.Client(key='45833284', secret='rUfMuKUv2Y0KPnWe')
def send_sms_messages_auto(body,to):
    client.send_message({
        'from': 'Vonage APIs',
        'to': to,
        'text': body,
        'type': 'unicode',
    })   