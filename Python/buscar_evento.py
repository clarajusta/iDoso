from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
	
scopes = ['https://www.googleapis.com/auth/calendar']
#verificar a ocrrencia de envento em um periodo de 1 min a partir do horário atual
#printar o horário atual e o horário atual + 1min
def main():

    import pickle
   
    credentials = pickle.load(open("token.pkl", "rb"))
    service = build("calendar", "v3", credentials=credentials)

    import datetime
    from datetime import timedelta
    import unicodedata
    import pytz
    tzone = pytz.timezone('America/Sao_Paulo')
    now = datetime.datetime.now(tz=tzone)

    timeMin = now
    timeMin = timeMin.isoformat()
    timeMax = now + timedelta(minutes=1)
    timeMax = timeMax.isoformat()
    #if e else #funcao da checagem e criacao do lembrete funcao diferente
#primeiro checar se em evento no dia
#se tiver, checar na h
    print('Listar data e hora atual e outra data somando 1 min')
    events_result = service.events().list(calendarId='primary', timeMin=timeMin,
                                        timeMax=timeMax, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    print (timeMax)
    print (timeMin)
    print('Verificar a ocorrencia de evento')

    if not events:
        print('Sem evento recente')
    for event in events: 
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary']) 
        #agora eu quero adicionar a saida
        
if __name__ == '__main__':
    main()
