# -*- coding: utf-8 -*-
import sys
import speech_recognition as sr
from playsound import playsound

reload(sys)
sys.setdefaultencoding('utf-8')

#Funcao para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuario
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Frase para o usuario dizer algo
        playsound('audios/chamou.mp3')
        print("Diga alguma coisa: ")
        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        
        #Passa a variavel para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        
        #Retorna a frase pronunciada
<<<<<<< HEAD
        print("Voce disse: " + frase)
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Nao entendi")
=======
        
        print("Você disse: " + frase)
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnknownValueError:
        playsound('audios/nao_entendi.mp3')
        frase = "Não entendi"
        print("Não entendi")
>>>>>>> d6d0d30a5b38030077558a63d2c744428a3a5fd9
        
    return frase
