package main

import (
	"bufio"
	"fmt"
	"io"
	"os/exec"
)

func main() {
	cmd := exec.Command("python", "speech_to_text.py")
	stdout, err := cmd.StdoutPipe()
	if err != nil {
		panic(err)
	}
	stderr, err := cmd.StderrPipe()
	if err != nil {
		panic(err)
	}
	err = cmd.Start()
	if err != nil {
		panic(err)
	}

	go copyOutput(stdout)
	go copyOutput(stderr)
	cmd.Wait()
}

func copyOutput(r io.Reader) {
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		fmt.Printf("%s\n ", scanner.Text())
	}
}
