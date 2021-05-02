# -*- coding: utf-8 -*-
import os
from twilio.rest import Client
#from credenciais import Account_SID, Auth_Token, Telefone_que_envia, Telefone_que_recebe
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

account_sid = Account_SID
auth_token = Auth_Token
client = Client(account_sid, auth_token)

def enviar_sms():
    message = client.messages \
        .create(
            body='Número de emergência ativado!',
            from_='Telefone_que_envia',
            to='Telefone_que_recebe'
        )

    print(message.sid)
    print("Mensagem enviada!")
