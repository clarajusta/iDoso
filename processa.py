# -*- coding: utf-8 -*-
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from datetime import datetime
from respostas_datetime import datas
from send_sms import enviar_sms
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

agora = datetime.now()

#Funcao responsavel por falar 
def cria_audio(audio):
    # mostrando a string de audio que foi criada quando você falou
    tts = gTTS(audio,lang='pt-br')

    #Salva o arquivo de audio com a string que foi falada (caso seja útil)
    #tts.save('audios/hello.mp3')

    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    if(audio == "Bom dia"):
        playsound('audios/bom_dia.mp3')
    if(audio == "Que horas são"):
        datas(agora)
        playsound('audios/horario.mp3')
    if(audio == "Que dia é hoje"):
        playsound('audios/data_hoje.mp3')
    if (audio == "conte uma piada"):
        playsound ('audios/piada.mp3')
    if (audio == "ativar contato de emergência"):
        playsound ('audios/emergencia.mp3')
        enviar_sms()

    
#tts = gTTS('Oi, eu sou a Rosie', lang= 'pt-br')
#tts.save('audios/hello.mp3')
