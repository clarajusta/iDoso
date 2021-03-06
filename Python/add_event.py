from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
	
scopes = ['https://www.googleapis.com/auth/calendar']


import pickle

credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)

result = service.calendarList().list().execute()
result['items'][0]
calendar_id = result ['items'][0]['id']
result = service.events().list(calendarId=calendar_id, timeZone='America/Sao_Paulo').execute()

#criando evento
from datetime import datetime, timedelta
start_time = datetime(2021, 5, 5, 20, 0, 0) #ano, mês, data, hora, minuto, segundo #aqui terão que ser strings
end_time=start_time + timedelta(hours=4) #duracao
timezone = 'America/Sao_Paulo'
event = {
  'summary': 'Primeiro evento com codigo!',
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

#import datefinder 
#matches = datefinder.find_dates ("5 may 9 PM")
#print (list(matches))

