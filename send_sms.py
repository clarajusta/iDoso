
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
# Não é recomendado colocar essas informações no GitHub
account_sid = "account_sid"
auth_token = "_account_token"
client = Client(account_sid, auth_token)

def enviar_sms():
    message = client.messages \
        .create(
            body='Número de emergência ativado!',
            from_='+12053016152',
            to='+5561986044291'
        )

    print(message.sid)
    return print("Mensagem enviada!")
