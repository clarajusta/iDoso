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
	"github.com/stianeikeland/go-rpio"
)

var frase string = "..."
var mara bool = false

func upper(data string) string {

    return strings.ToUpper(data)
}

func main() {

	//Inicializando o led
	err := rpio.Open()
	if err != nil {
		panic(fmt.Sprint("Não foi possível conectar com o LED", err.Error()))
	}
	defer rpio.Close()
	pin := rpio.Pin(18)
	pin.Output()

	// Loop contínuo principal
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

		//Encontrando a palavra-chave MARA -> INICIA ROTINA DE FUNÇÕES
        matched, err := regexp.MatchString("MARA", frase)
        if matched{
			exec.Command("/bin/bash", "speech.sh", "Você me chamou?").Output()
			mara = true 
			// Liga o Led (dá sinal de vida)
			pin.High()
			// no próximo loop a Mara já vai estar te ouvindo
            fmt.Println("Chamou? \n     V\n      L('o' )/    \n")
			fmt.Println("Mara_1: ",mara)
        }
		//Encontrando a palavra-chave OK -> VOLTA A FICAR SÓ ESCUTANDO
        if strings.Contains(frase, "OK"){
			exec.Command("/bin/bash", "speech.sh", "Ok, qualquer coisa é só chamar!").Output()
			mara = false
			// Desliga o led
			pin.Low()
			// no próximo loop a Mara já vai estar te ouvindo
            fmt.Println("Ok... \n     V\n      _(-.-)_    \n")
			fmt.Println("Mara_1: ",mara)
        }

		// Rotina da Mara ----
		if mara{
			// Liga o led (dá sinal de vida)
			if strings.Contains(frase, "LEMBRETE"){
				fmt.Println("Indo para a função do lembrete\n")
				calendarLoop(frase)
				break
			} else{
				fmt.Printf("indo para a funcao geral\n")
				funcLoop(frase)
				break				
			}
		}else{
			// Desliga o led  caso ele esteja ligado
			pin.Low()
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
		data_en := "Agora são 15:04"
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
	if (strings.Contains(comando, "TEMPERATURA")||strings.Contains(comando, "CLIMA")){
		out, err := exec.Command("/bin/bash", "weather.sh").Output()

		if err != nil {
			log.Fatal(err)
		}
	
		fmt.Println(string(out))
		exec.Command("/bin/bash", "speech.sh", string(out)).Output()
	}
	//pARA PEGAR TEMPERATURA: curl -H "Accept-Language: pt-br" wttr.in/Lago+Sul?format="%C+%t"
	main()
}

func calendarLoop(comando string){
	fmt.Println("Executando função", comando)
	fmt.Println("Função do calendário!![#]")
	mara = false
	main()
}