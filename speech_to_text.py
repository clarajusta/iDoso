# -*- coding: utf-8 -*-
import sys
import speech_recognition as sr

#reload(sys)
#sys.setdefaultencoding('utf-8')


while(True):
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
    try:
        #Passa a variavel para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        result = str.encode(frase)
        print(frase)
        sys.stdout.flush()
    except sr.UnknownValueError:
        result = str.encode("...")
        print("...")
        sys.stdout.flush()

