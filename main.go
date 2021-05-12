package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "os/exec"
    "regexp"
	"strings"
)

var frase string = "..."
var mara bool = false

func upper(data string) string {

    return strings.ToUpper(data)
}

func main() {	
	for {

        fmt.Println("Escutando...")
        cmd := exec.Command("/bin/bash", "s2t.sh", "out.wav", "16000", "1")
    
        stdout, err := cmd.StdoutPipe()
    
        if err != nil {
            log.Fatal(err)
        }
    
        if err := cmd.Start(); err != nil {
            log.Fatal(err)
        }
    
        data, err := ioutil.ReadAll(stdout)
    
        if err != nil {
            log.Fatal(err)
        }
    
        if err := cmd.Wait(); err != nil {
            log.Fatal(err)
        }
        frase := upper(string(data))
        fmt.Printf("%s\n", frase)

		if mara{
			if strings.Contains(frase, "LEMBRETE"){
				fmt.Println("Indo para a função do lembrete\n")
				calendarLoop(frase)
				break
			} else{
				fmt.Printf("indo para a funcao geral\n")
				funcLoop(frase)
				break				
			}

		}

		//Encontrando a palavra-chave MARA
        matched, err := regexp.MatchString("MARA", frase)
        if matched{
			mara = true
            fmt.Println("Chamou? \n     V\n      L('o' )/    \n")
			fmt.Println("Mara_1: ",mara)
        }
		
    }
}

func funcLoop(comando string) {
	fmt.Println("Executando função", comando)
	if strings.Contains(comando, "BOM DIA"){
		fmt.Println("Bom dia para você também *(^-^)*")
	}
	mara = false
	main()
}

func calendarLoop(comando string){
	fmt.Println("Executando função", comando)
	fmt.Println("Função do calendário!![#]")
	mara = false
	main()
}