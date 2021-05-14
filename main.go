package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "os/exec"
    "regexp"
	"strings"
	"time"
	"encoding/json"
	"net/http"
	"os"
	"strconv"

	"github.com/goodsign/monday"
	"github.com/stianeikeland/go-rpio"
	"golang.org/x/net/context"
	"golang.org/x/oauth2"
	"golang.org/x/oauth2/google"
	"google.golang.org/api/calendar/v3"
)

var frase string = "..."
var mara bool = false

var MONTHS = []string{"janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"}


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
				//calendarLoop(frase)
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
	if strings.Contains(comando, "EMERGÊNCIA"){
		exec.Command("/bin/bash", "speech.sh", "Enviando mensagem para seu contato de emergência!").Output()
		fmt.Println("+___EMERGÊNCIA ATIVADA___+")
		fmt.Println("Enviando mensagem para seu contato de emergência!!")
		exec.Command("/bin/bash", "send-sms.sh",).Output()
	}
	if strings.Contains(comando, "QUEM É VOCÊ"){
		exec.Command("/bin/bash", "speech.sh", "Me chamo Mara, sou sua assistente pessoal e estou aqui para te ajudar com o que puder!").Output()
		fmt.Println("(' v')/ Oi, me eu sou a Mara!")
	}
	// Clara: rotina de criação de evento/lembrete:
	if (strings.Contains(comando, "CRIAR")&&(strings.Contains(comando, "EVENTO")||strings.Contains(comando, "LEMBRETE"))){
		listagem:= strings.ToLower(comando) 
		fmt.Println(listagem)
		b, err := ioutil.ReadFile("credentials.json")
		if err != nil {
			log.Fatalf("Unable to read client secret file: %v", err)
		}
	
		// If modifying these scopes, delete your previously saved token.json.
		config, err := google.ConfigFromJSON(b, calendar.CalendarScope)
		if err != nil {
			log.Fatalf("Unable to parse client secret file to config: %v", err)
		}
		client := getClient(config)
	
		srv, err := calendar.New(client)
		if err != nil {
			log.Fatalf("Unable to retrieve Calendar client: %v", err)
		}

	
		fmt.Print("Escreva a frase com a data de início: ")
		startText := listagem
		//fmt.Print("Escreva a frase com a data de fim: ")
		//endText, _ := reader.ReadString('\n')
		startDate := getDateFromString(startText, MONTHS)
		//endDate := getDateFromString(endText, MONTHS)
		endDate := startDate.Add(time.Minute * 1)
	
		//t := time.Now().Format(time.RFC3339)
		//events, err := srv.Events.List("primary").ShowDeleted(false).
		event := &calendar.Event{
			Summary:     "Teste DATA String",
			Location:    "800 Howard St., San Francisco, CA 94103",
			Description: "A chance to hear more about Google's developer products.",
			Start: &calendar.EventDateTime{
				DateTime: startDate.Format(time.RFC3339),
				TimeZone: "America/Sao_Paulo",
			},
			End: &calendar.EventDateTime{
	
				DateTime: endDate.Format(time.RFC3339),
				TimeZone: "America/Sao_Paulo",
			},
			//Recurrence: []string{"RRULE:FREQ=DAILY;COUNT=2"},
		}
	
		calendarId := "primary"
		event, err = srv.Events.Insert(calendarId, event).Do()
		if err != nil {
			log.Fatalf("Unable to create event. %v\n", err)
		}
		fmt.Printf("Event created: %s\n", event.HtmlLink)
		
	}
	// Clara: rotina listagem dos eventos/lembretes do dia
	if strings.Contains(comando, "EVENTO"){
		if strings.Contains(comando, "HOJE"){
			//Pegar o dia de hoje
			data := time.Now()
			fmt.Println(data)
		}else if strings.Contains(comando, "DIA"){
			//Encontrar números na string
			//entrada = re,FindAllString(comando)
			entrada := strings.ToLower(comando) //-> deixa tudo em minusculo
			ss := strings.Split(entrada, "dia")
			s := ss[len(ss)-1] // corta logo após o "dia" -> exemplo: " 21 De Janeiro"
			fmt.Println(s)

			b, err := ioutil.ReadFile("credentials.json")
			if err != nil {
				log.Fatalf("Unable to read client secret file: %v", err)
			}
		
			// If modifying these scopes, delete your previously saved token.json.
			config, err := google.ConfigFromJSON(b, calendar.CalendarScope)
			if err != nil {
				log.Fatalf("Unable to parse client secret file to config: %v", err)
			}
			client := getClient(config)
		
			srv, err := calendar.New(client)
			if err != nil {
				log.Fatalf("Unable to retrieve Calendar client: %v", err)
			}
		
			startText:= s

			startDate := getDateFromString(startText, MONTHS)
			endDate := startDate.Add(time.Hour * 24)

			events, err := srv.Events.List("primary").ShowDeleted(false).
				SingleEvents(true).TimeMin(startDate.Format(time.RFC3339)).TimeMax(endDate.Format(time.RFC3339)).OrderBy("startTime").Do()
			if err != nil {
				log.Fatalf("Unable to retrieve next ten of the user's events: %v", err)
			}
			fmt.Println("Eventos do dia")
			if len(events.Items) == 0 {
				fmt.Println("Sem eventos no dia")
			} else {
				for _, item := range events.Items {
					date := item.Start.DateTime
					if date == "" {
						date = item.Start.Date
					}
					fmt.Printf("%v (%v)\n", item.Summary, date)
				}
			}

		}

	}
	main()
}

// Retrieve a token, saves the token, then returns the generated client.
func getClient(config *oauth2.Config) *http.Client {
	// The file token.json stores the user's access and refresh tokens, and is
	// created automatically when the authorization flow completes for the first
	// time.
	tokFile := "token.json"
	tok, err := tokenFromFile(tokFile)
	if err != nil {
		tok = getTokenFromWeb(config)
		saveToken(tokFile, tok)
	}
	return config.Client(context.Background(), tok)
}

// Request a token from the web, then returns the retrieved token.
func getTokenFromWeb(config *oauth2.Config) *oauth2.Token {
	authURL := config.AuthCodeURL("state-token", oauth2.AccessTypeOffline)
	fmt.Printf("Go to the following link in your browser then type the "+
		"authorization code: \n%v\n", authURL)

	var authCode string
	if _, err := fmt.Scan(&authCode); err != nil {
		log.Fatalf("Unable to read authorization code: %v", err)
	}

	tok, err := config.Exchange(context.TODO(), authCode)
	if err != nil {
		log.Fatalf("Unable to retrieve token from web: %v", err)
	}
	return tok
}

// Retrieves a token from a local file.
func tokenFromFile(file string) (*oauth2.Token, error) {
	f, err := os.Open(file)
	if err != nil {
		return nil, err
	}
	defer f.Close()
	tok := &oauth2.Token{}
	err = json.NewDecoder(f).Decode(tok)
	return tok, err
}

// Saves a token to a file path.
func saveToken(path string, token *oauth2.Token) {
	fmt.Printf("Saving credential file to: %s\n", path)
	f, err := os.OpenFile(path, os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0600)
	if err != nil {
		log.Fatalf("Unable to cache oauth token: %v", err)
	}
	defer f.Close()
	json.NewEncoder(f).Encode(token)
}

func stringInSlice(a string, list []string) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}

func getDateFromString(text string, list []string) time.Time {
	//considerando que o usuario sempre irá falar um numero representando o dia e um mes
	day := -1
	month := -1
	year := time.Now().Year()
	for idx, monthName := range list {
		if strings.Contains(text, monthName) {
			month = idx + 1
			break
		}
	}

	words := strings.Fields(text)
	for _, word := range words {
		//fmt.Println(word)
		dayInt, err := strconv.Atoi(word)
		if err == nil {
			day = dayInt
		}
	}

	if day != -1 && month != -1 {
		//fmt.Println(month, day)
		date := time.Date(year, time.Month(month), day, 0, 0, 0, 0, time.Local)
		//fmt.Println(date)
		return date
	}

	return time.Now()

}
