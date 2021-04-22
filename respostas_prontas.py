from gtts import gTTS

# Para o restante das strings"
tts = gTTS('Não entendi.', lang= 'pt-br')
tts.save('audios/nao_entendi.mp3')

# Para a String "Bom dia!"
tts = gTTS('Bom dia, senhora! Espero que seu dia seja maravilhoso!', lang= 'pt-br')
tts.save('audios/bom_dia.mp3')
