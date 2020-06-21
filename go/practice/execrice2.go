package main

import "fmt"

func main() {

out:
	for i := 1; i < 10; i++ {
		for j := 1; j <= i; j++ {
			fmt.Printf("%d*%d=%d\t", i, j, i*j)
			break out
		}
		fmt.Println()
	}
}
