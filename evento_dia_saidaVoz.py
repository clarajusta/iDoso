from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import pyttsx3
import speech_recognition as sr
import pytz
from gtts import gTTS
import playsound

SCOPES = ['https://www.googleapis.com/auth/calendar']
#MONTHS = {'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4,  'mai': 5,  'jun': 6,
#          'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12}
MONTHS = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
DAYS = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]

def speak(text):
    tts = gTTS(text=text, lang="pt-br")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language = 'pt-BR')
            print(said)

        except Exception as e:
            print ("Exception: " +str(e))

    return said

#text = get_audio()

#if "olá" in text:
#    speak("oi clarinha")

def authenticate_google():
    credentials = pickle.load(open("token.pkl", "rb"))
    service = build("calendar", "v3", credentials=credentials)

    return service

def get_events(day, service):
    date = datetime.datetime.combine(day, datetime.datetime.min.time()) #começo do dia
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time()) #fim do dia
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)
    #now = datetime.datetime.utcnow().isoformat() + 'Z'
    #print(f'Mostrando {n} eventos')

    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        speak('Nenhum evento encontrado')
    else:
        speak(f"Você temm {len(events)} eventos nesse dia")

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0]) #hora que o evento comeca, pois ele é sseparado pelo T, na saida do terminal
            if int(start_time.split(":")[0]) < 12:
                start_time = start_time + "da manhã" #talvez de pra retirar
            else:
                start_time = str(int(start_time.split(":")[0])-12)
                start_time = start_time + "da tarde" #periodo tarde

            speak(event["summary"] + " as " + start_time) #nome evento + as horario

#passaremos a string dita pelo usuario aqui: 
def get_date(text):
    text = text.lower()
    today = datetime.date.today()

    #se ele falar a palavra hoje, iremos retorar a data de hoje
    if text.count ("hoje") > 0:
        return today #today ta logo no inicio da funcao, depois verificar se preciso colocar fusohoaraio

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split(): #Dividindo as palavras ditas a partir de espacos
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit(): #se encontrarmos um digito dito, para o caso da pessoa falar 8 de agosto
            day = int(word)

    if month < today.month and month != -1:
        year=year+1

    if day < today.day and month == -1 and day != 1: #se o usario nao falar mes e dia da semana, so a data
        month = month + 1

    if month == -1 and day == -1 and day_of_week != -1: #se so falarmos dia da semana "segunda", Terca..
        current_day_of_week = today.weekday() #obter data de hoje
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("proximo") >= 1: #somar dias , proxima segunda
                dif += 7

        return today + datetime.timedelta(dif)
    
    #se não encontrarmos
    if month == -1 or day ==1:
        return None
    if day != -1:  
        return datetime.date(month=month, day=day, year=year)

service = authenticate_google()
text = get_audio().lower()
get_events(get_date(text), service)
#print(get_date(text),)
