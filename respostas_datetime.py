# -*- coding: utf-8 -*-
from gtts import gTTS
from datetime import datetime
import sys
import urllib3

#Retirar os avidos de erro de https (por causa do datetime)
urllib3.disable_warnings()

#habilitar os caracteres especiais nas strings
#reload(sys)
#sys.setdefaultencoding('utf-8')

# para as funcoes que dependem da data atual
def horas(agora):
    # Para a String "Que horas sao"
    horas = agora.strftime("%H")
    minutos = agora.strftime("%M")
    horario = "No momento são " + horas + " horas e " + minutos + " minutos"
    print(horario)
    tts = gTTS(horario, lang= 'pt-br')
    tts.save('audios/horario.mp3')


def data(agora):
    # Para dizer "que dia e hoje?":
    # TODO: acrescetar dia da semana
    dia = agora.strftime("%d")
    mes_num = agora.strftime("%m")
    mes_ext = {1: 'Janeiro', 2 : 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
    mes = mes_ext[int(mes_num)]
    ano = agora.strftime("%Y")
    data_hoje = "Hoje é o dia " + dia + " de " + mes + " do ano de " + ano
    print(data_hoje)
    tts = gTTS(data_hoje, lang= 'pt-br')
    tts.save('audios/data_hoje.mp3')

