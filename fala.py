import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#Funcao responsavel por falar 
def cria_audio(audio):
    # mostrando a string de áudio que foi criada quando você falou
    tts = gTTS(audio,lang='pt-br')

    #Salva o arquivo de audio com a string que foi falada (caso seja útil)
    #tts.save('audios/hello.mp3')

    print("Estou aprendendo o que você disse...")
    #Da play ao audio
    playsound('audios/bom_dia.mp3')
    
#tts = gTTS('Oi, eu sou a Rosie', lang= 'pt-br')
#tts.save('audios/hello.mp3')
