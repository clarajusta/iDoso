package main

import "github.com/hegedustibor/htgo-tts"

func main() {
    speech := htgotts.Speech{Folder: "audio", Language: "pt-BR"}
    speech.Speak("Eu quero só passar nessa desgraça. É uma matéria tão legal mas agora já deu")
}
	