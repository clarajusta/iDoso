import threading
import sys, pyaudio, os
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
from datetime import datetime
from respostas_datetime import data, horas
# -*- coding: utf-8 -*-

#reload(sys)
#sys.setdefaultencoding('utf-8')

# TODO: adicionar a thread do calendário para ocorrer de maneira paralela às threads
agora = datetime.now()
mara = False

def processa_funcao(audio):
    global mara
    global agora
    # mostrando a string de audio que foi criada quando você falou
    tts = gTTS(audio,lang='pt-br')

    print("MARA chegou no processo: ", mara)
    #Da play ao audio
    if("bom dia" in audio.lower()):
        playsound('audios/bom_dia.mp3')
    if("que horas são" in audio.lower()):
        horas(agora)
        playsound('audios/horario.mp3')
    if("que dia é hoje" in audio.lower()):
        data(agora)
        playsound('audios/data_hoje.mp3')
    if ("conte uma piada" in audio.lower()):
        playsound ('audios/piada.mp3')
    if (audio == "ativar contato de emergência"):
        playsound ('audios/emergencia.mp3')
        #enviar_sms()
    if ("quem é você" in audio.lower()):
        playsound ('audios/mara.mp3')
    if ("como você está" in audio.lower()):
        playsound ('audios/estou_bem.mp3')

    mara = False
    print("MARA terminou de processar: ", mara)
    main_task()

def frases(lock):
    global mara
    lock.acquire()
    print("MARA(frases): ", mara)
    while(True):
        print("Estou te ouvindo")
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            #Chama um algoritmo de reducao de ruidos no som
            microfone.adjust_for_ambient_noise(source)
            #Armazena o que foi dito numa variavel
            audio = microfone.listen(source)
        try:
            #Passa a variavel para o algoritmo reconhecedor de padroes
            frase = microfone.recognize_google(audio,language='pt-BR')
            print(frase)
            if "Mara" in frase:
                mara = True
                print("MARA foi encontrada: ", mara)
                break
            if(mara is True):
                print("MARA sendo processada: ", mara)
                processa_funcao(frase)
                break

        except sr.UnknownValueError:
            if(mara is True):
                print("MARA sendo processada(com error): ", mara)
                playsound ('audios/nao_entendi.mp3')
                mara = False
                break

            else:
                print("...")

    lock.release()

def main_task():
    lock = threading.Lock()

    escutando = threading.Thread(target=frases, args=(lock,)) # procurar "Mara"
    funcao = threading.Thread(target=frases, args=(lock,)) # ouvir a função
    if(mara is False):
        print("mobo escuta")
        escutando.start()
        escutando.join()
    if(mara is True):
        print("iniciando a funcao")
        playsound('audios/chamou.mp3')
        funcao.start()
        funcao.join()

if __name__ == "__main__":
    main_task()