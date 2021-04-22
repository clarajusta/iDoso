from gtts import gTTS

# Para o restante das strings"
tts = gTTS('Não entendi.', lang= 'pt-br')
tts.save('audios/nao_entendi.mp3')

# Para a String "Bom dia!"
tts = gTTS('Bom dia, senhora! Espero que seu dia seja maravilhoso!', lang= 'pt-br')
tts.save('audios/bom_dia.mp3')

# Para a String "Conte uma piada"
tts = gTTS('Por que a velhinha não usa relógio? Porque ela é sem hora', lang= 'pt-br')
tts.save('audios/piada.mp3')