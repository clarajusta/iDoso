package main

import (
    "fmt"
    "strings"
)

func between(value string, a string, b string) string {
    // Get substring between two strings.
    posFirst := strings.Index(value, a)
    if posFirst == -1 {
        return ""
    }
    posLast := strings.Index(value, b)
    if posLast == -1 {
        return ""
    }
    posFirstAdjusted := posFirst + len(a)
    if posFirstAdjusted >= posLast {
        return ""
    }
    return value[posFirstAdjusted:posLast]
}

func before(value string, a string) string {
    // Get substring before a string.
    pos := strings.Index(value, a)
    if pos == -1 {
        return ""
    }
    return value[0:pos]
}

func after(value string, a string) string {
    // Get substring after a string.
    pos := strings.LastIndex(value, a)
    if pos == -1 {
        return ""
    }
    adjustedPos := pos + len(a)
    if adjustedPos >= len(value) {
        return ""
    }
    return value[adjustedPos:len(value)]
}

func main() {
    // Example string to parse.
    test := "9 de agosto as 17 horas e 15 minutos"

    // Test between func.
    //hour = hourInt(between(test, "as", "horas"))
   // fmt.Println(hour)
   fmt.Println(between(test, "as", "horas"))
   
    // Test before func.
   fmt.Println(before(test, "minutos"))

    // Test after func.
    fmt.Println(after(test, "as"))
}
