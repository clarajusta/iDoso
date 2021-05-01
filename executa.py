# -*- coding: utf-8 -*-
from ouve import ouvir_microfone
from processa import cria_audio
import main

frase = ouvir_microfone()

cria_audio(frase)

execfile('main.py')