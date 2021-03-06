package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"

	"golang.org/x/net/context"
	"golang.org/x/oauth2"
	"golang.org/x/oauth2/google"
	"google.golang.org/api/calendar/v3"
)

//slice mapeando mes

var MONTHS = []string{"janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"}

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

func main() {
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

	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Escreva a frase com a data de início: ")
	startText, _ := reader.ReadString('\n')
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
		fmt.Println(word)
		dayInt, err := strconv.Atoi(word)
		if err == nil {
			day = dayInt
		}
	}

	if day != -1 && month != -1 {
		fmt.Println(month, day)
		date := time.Date(year, time.Month(month), day, 0, 0, 0, 0, time.Local)
		fmt.Println(date)
		return date
	}

	return time.Now()

}

//return datetime.date(month, day, year)
//date = datetime.datetime.combine(day, datetime.datetime.min.time())
//fmt.Println(date)
