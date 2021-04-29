# -*- coding: utf-8 -*-
import speech_recognition as sr
import sys
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
        print("Diga alguma coisa: ")
        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:
        
        #Passa a variavel para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')
        
        #Retorna a frase pronunciada
        
        print("Você disse: " + frase)
        
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except LookupError:
        print("Não entendi")
        
    return frase
