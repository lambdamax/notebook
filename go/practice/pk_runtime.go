package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Println("Go root:", runtime.GOROOT())
	fmt.Println("OS:", runtime.GOOS)
	fmt.Println("逻辑CPU数量:", runtime.NumCPU())
}
