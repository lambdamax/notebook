package main

import (
	"fmt"
	"time"
)

func main() {
	ch1 := make(chan int)

	go func() {
		for i := 0; i <= 10; i++ {
			ch1 <- i
		}
	}()
	for {
		select {
		case n := <-ch1:
			fmt.Println("从ch1中取出", n)
			time.Sleep(1 * time.Second)
			if n == 10 {
				close(ch1)
				return
			}
		}
	}

}
