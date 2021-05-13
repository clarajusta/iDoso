package main

import(
	"fmt"
	"time"
	"github.com/stianeikeland/go-rpio"
)


func main() {	
	fmt.Sprint("Abrindo gpio")
		err := rpio.Open()
		if err != nil {
			panic(fmt.Sprint("Não foi possível conectar com o LED", err.Error()))
		}
		defer rpio.Close()
		pin := rpio.Pin(18)
		pin.Output()
		for x:= 0; x<20; x++{
			pin.Toggle()
			time.Sleep(time.Second / 5)
		}
}