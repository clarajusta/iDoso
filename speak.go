package main

import (
    "fmt"
    "log"
    "os/exec"
)

func main() {

    out, err := exec.Command("/bin/bash", "weather.sh").Output()

    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(string(out))
    exec.Command("/bin/bash", "speech.sh", string(out)).Output()
}