# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def agenda():
    print("agenda sendo executada")

    i = 0
    while(i < 10):
        print("\n Checando o calendário...\n")
        i += 1
        print(i)
    
    print("Função executada")