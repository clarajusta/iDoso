# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def agenda():
    # é ativada, não recebe variável externa
    # cria a string para ela falar os lembretes do dia 
    # salva a string em um áudio com um nome X (que nem em respostas_datetime)
    print("agenda sendo executada")

    i = 0
    while(i < 10):
        print("\n Checando o calendário...\n")
        i += 1
        print(i)
    
    print("Função executada")

