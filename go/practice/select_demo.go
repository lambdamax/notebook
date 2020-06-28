package main

import (
	"fmt"
	"time"
)

func main() {
	ch1 := make(chan int)
	ch2 := make(chan int)

	go func() {
		time.Sleep(1 * time.Second)
		for i := 0; i <= 10; i++ {
			ch1 <- i
		}
	}()

	go func() {
		time.Sleep(1 * time.Second)
		for i := 10; i > 0; i-- {
			ch2 <- i
		}
	}()

	select {
	case n := <-ch1:
		fmt.Println("从ch1中取出", n)
	case n, ok := <-ch2:
		if !ok {
			fmt.Println("ch2关闭")
		} else {
			fmt.Println("从ch2中取出", n)
		}
	}
}
