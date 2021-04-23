
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
# Não é recomendado colocar essas informações no GitHub
account_sid = "AC5f01dba03bc1b76b23f6a96b464dc5c2"
auth_token = "cebb094e8bd48499a83a0a036d6b7ece"
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
