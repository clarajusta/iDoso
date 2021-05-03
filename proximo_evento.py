from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
	
scopes = ['https://www.googleapis.com/auth/calendar']
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

    events_result = service.events().list(calendarId='primary', timeMin=timeMin,
                                        maxResults=1, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('Você não tem eventos futuros')
    else:
        #print(f"You have {len(events)} events on this day.")
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            start_time = str(start.split("T")[1].split("-")[0])
            print(event["summary"] + " as " + start_time)

if __name__ == '__main__':
    main()
