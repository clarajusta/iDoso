
from gtts import gTTS
import sys

# -*- coding: utf-8 -*-
#reload(sys)
#sys.setdefaultencoding('utf-8')

# Frases curtas:
tts = gTTS('Entendido', lang= 'pt-br')
tts.save('audios/entendido.mp3')

tts = gTTS('Correto?', lang= 'pt-br')
tts.save('audios/correto_q.mp3')

# Para o restante das strings"
tts = gTTS('Não entendi.', lang= 'pt-br')
tts.save('audios/nao_entendi.mp3')

# Para a String "Bom dia!"
tts = gTTS('Bom dia, senhora! Espero que seu dia seja maravilhoso!', lang= 'pt-br')
tts.save('audios/bom_dia.mp3')

# Para a criacao de um lembrete:
# passo 1:
tts = gTTS('Ativando a função do lembrete', lang= 'pt-br')
tts.save('audios/lembrete_passo1.mp3')

# Para a String "Conte uma piada"
tts = gTTS('Você sabe por que a velhinha não usa relógio? É porque ela é sem hora', lang= 'pt-br')
tts.save('audios/piada.mp3')

#Enviando mensagem para contato de emergencia
tts = gTTS('Enviando mensagem para seu contato de emergência', lang= 'pt-br')
tts.save('audios/emergencia.mp3')

#Chamou?
tts = gTTS('Chamou?', lang= 'pt-br')
tts.save('audios/chamou.mp3')

#Quem é você?
tts = gTTS('Eu sou a Ágata, a sua assistente pessoal. Estou aqui para te ajudar no que puder!', lang= 'pt-br')
tts.save('audios/mara.mp3')

#Tudo bem com você?
tts = gTTS('Eu estou Maravilhosa, e você, como está?', lang= 'pt-br')
tts.save('audios/estou_bem.mp3')

#Eu estou bem
tts = gTTS('Isso é muito bom!', lang= 'pt-br')
tts.save('audios/muito_bom.mp3')
