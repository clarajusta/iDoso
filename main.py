# -*- coding: utf-8 -*-
from ouve import ouvir_microfone
from processa import cria_audio
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

frase = ouvir_microfone()

cria_audio(frase)