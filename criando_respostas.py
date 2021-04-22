from gtts import gTTS

tts = gTTS('Bom dia, senhora! Espero que seu dia seja maravilhoso!', lang= 'pt-br')
tts.save('audios/bom_dia.mp3')