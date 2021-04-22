import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from datetime import datetime
from respostas_datetime import datas

agora = datetime.now()

#Funcao responsavel por falar 
def cria_audio(audio):
    # mostrando a string de áudio que foi criada quando você falou
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
    if (audio == "Conte uma piada"):
        playsound ('audios/piada.mp3')
    else:
        playsound('audios/nao_entendi.mp3')

    
#tts = gTTS('Oi, eu sou a Rosie', lang= 'pt-br')
#tts.save('audios/hello.mp3')
