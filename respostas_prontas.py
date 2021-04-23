from gtts import gTTS

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

# Para a criação de um lembrete:
# passo 1:
tts = gTTS('Muito bem, do que você deseja se lembrar?', lang= 'pt-br')
tts.save('audios/lembrete_passo1.mp3')
# passo 2:
tts = gTTS('Para quando é esse bilhete?', lang= 'pt-br')
tts.save('audios/lembrete_passo2.mp3')
