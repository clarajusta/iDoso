# -*- coding: utf-8 -*-
import threading
import multiprocessing as mp
import sys, pyaudio, os
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
from datetime import datetime
from respostas_datetime import data, horas
from agenda import agenda

reload(sys)
sys.setdefaultencoding('utf-8')

# TODO: adicionar a thread do calendário para ocorrer de maneira paralela às threads
agora = datetime.now()
frase = []
mara = False
lembrete = False

def processa_funcao(audio):
    global mara
    global agora
    global lembrete
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
    if ("criar um lembrete" in audio.lower()):
        lembrete = True
        print("NOVO VALOR DE LEMBRETE:", lembrete)

    mara = False
    print("MARA terminou de processar: ", mara)
    main_task()

def frases(lock):
    global frase
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
                playsound ('audios/nao_entendi.mp3')
                mara = False
                print("MARA sendo processada(com error): ", mara)

            else:
                print("...")

    lock.release()

def lembrete_func(lock):
    global lembrete
    lock.acquire()
    print("Executando função para criar um lembrete")
    # chama a função agenda para salvar o novo áudio falando os lembretes do dia
    agenda()
    # Executa o áudio com o nome X, criado em agenda
    lembrete = False
    lock.release()

def main_task():
    global mara
    global lembrete
    lock = threading.Lock()

    escutando = threading.Thread(target=frases, args=(lock,)) # procurar "Mara"
    funcao = threading.Thread(target=frases, args=(lock,)) # ouvir a função
    lembrando = threading.Thread(target=lembrete_func, args=(lock,)) # função de agenda ativada

    print("______Lembrete",lembrete)
    if(lembrete is True):
        playsound('audios/lembrete_passo1.mp3')
        lembrando.start()
        lembrando.join()

    if(mara is False):
        print("modo escuta")
        escutando.start()
        escutando.join()
    if(mara is True):
        print("iniciando a funcao")
        playsound('audios/chamou.mp3')
        funcao.start()
        funcao.join()


if __name__ == "__main__":
    main_task()