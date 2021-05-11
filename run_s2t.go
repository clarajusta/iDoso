package main

import (
    "fmt"
    "io/ioutil"
    "log"
    "os/exec"
    "strings"
)

func upper(data string) string {

    return strings.ToUpper(data)
}

func main() {
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

    fmt.Printf("%s\n", upper(string(data)))
}