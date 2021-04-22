from gtts import gTTS
from datetime import datetime

# para as funções que dependem da data atual
def datas(agora):
    # Para a String "Que horas são"
    horas = agora.strftime("%H")
    minutos = agora.strftime("%M")
    horario = "No momento são " + horas + " horas e " + minutos + "minutos"
    tts = gTTS(horario, lang= 'pt-br')
    tts.save('audios/horario.mp3')

    # Para dizer "que dia é hoje?":
    # TODO: acrescetar dia da semana
    dia = agora.strftime("%d")
    mes_num = agora.strftime("%m")
    mes_ext = {1: 'Janeiro', 2 : 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
    mes = mes_ext[int(mes_num)]
    ano = agora.strftime("%Y")
    data_hoje = "Hoje é o dia " + dia + " de " + mes + "do ano de " + ano
    tts = gTTS(data_hoje, lang= 'pt-br')
    tts.save('audios/data_hoje.mp3')
