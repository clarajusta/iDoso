# -*- coding: utf-8 -*-
import sys
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime, timedelta


reload(sys)
sys.setdefaultencoding('utf-8')

scopes = ['https://www.googleapis.com/auth/calendar']

#flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
#credentials = flow.run_console()

#pickle.dump(credentials, open("token.pkl", "wb"))
credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)

result = service.calendarList().list().execute()
result['items'][0]
calendar_id = result ['items'][0]['id']
result = service.events().list(calendarId=calendar_id, timeZone='America/Sao_Paulo').execute()
#print(result)

#criando evento
start_time = datetime(2021, 5, 5, 20, 0, 0) #ano, mês, data, hora, minuto, segundo
end_time=start_time + timedelta(hours=4) #acho que aqui é duração
timezone = 'America/Sao_Paulo'
event = {
  'summary': 'ATRÁS DE VOCÊ!',
  'location': 'Casa',
  'description': 'SOE Projeto final',
  'start': {
    'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"), #criando string para datetime e a ordem da data 
    'timeZone': timezone,
  }, #podemos colocar quantas vezes o evento irá se repetir com o uso de "recurrence" e tbm podemos convidar pessoas por email
  'end': {
    'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'reminders': { #lembretes por e-mail e tempo do e-mail
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60}, #notificacao e-mail 24 horas antes do evento
      {'method': 'popup', 'minutes': 10}, #notificacao popup 10min antes do evento 
    ],
  },
}

service.events().insert(calendarId=calendar_id, body=event).execute() 
