package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "os/exec"
    "regexp"
	"strings"
	"time"
	"github.com/goodsign/monday"
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
			exec.Command("/bin/bash", "speech.sh", "Você me chamou?").Output()
			mara = true
            fmt.Println("Chamou? \n     V\n      L('o' )/    \n")
			fmt.Println("Mara_1: ",mara)
        }
		
    }
}

func funcLoop(comando string) {
	fmt.Println("Executando função", comando)
	if strings.Contains(comando, "BOM DIA"){
		exec.Command("/bin/bash", "speech.sh", "Bom dia para você também!").Output()
		fmt.Println("Bom dia para você também *(^-^)*")
	}
	if strings.Contains(comando, "CONTE") && strings.Contains(comando, "PIADA"){
		exec.Command("/bin/bash", "speech.sh", "Aqui está uma piada para você. .Porquê a velhinha não usa relógio? . Porquê ela é senhora!").Output()
		fmt.Println("(/'v')/ TA-DAH!!\n")
	}
	if strings.Contains(comando, "HORAS SÃO"){
		data := time.Now()
		data_en := "Agora são 15:04 do dia 2. de January de 2006"
		data_PtBR := monday.Format(data, data_en,monday.LocalePtBR)
		exec.Command("/bin/bash", "speech.sh", data_PtBR).Output()
		fmt.Println(data_PtBR)
	}
	if strings.Contains(comando, "DIA")&&strings.Contains(comando, "HOJE"){
		data := time.Now()
		data_en := "Hoje é Monday , 2. de January de 2006"
		data_PtBR := monday.Format(data, data_en,monday.LocalePtBR)
		exec.Command("/bin/bash", "speech.sh", data_PtBR).Output()
		fmt.Println(data_PtBR)
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