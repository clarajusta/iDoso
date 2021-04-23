
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
# Não é recomendado colocar essas informações no GitHub
account_sid = "Account_SID"
auth_token = "Auth_Token"
client = Client(account_sid, auth_token)

def enviar_sms():
    message = client.messages \
        .create(
            body='Número de emergência ativado!',
            from_='Telefone_que_envia',
            to='Telefone_que_recebe'
        )

    print(message.sid)
    return print("Mensagem enviada!")
