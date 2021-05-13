package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "os/exec"
    "strings"
    "regexp"
)

func upper(data string) string {

    return strings.ToUpper(data)
}

func main() {
    for{
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

        matched, err := regexp.MatchString("MARA", frase)
        if matched{
            fmt.Println("Chamou? \n     V\n      L('o' )/    \n")
            //Chamar aqui para executar a função de outro arquivo
        }
    }
}