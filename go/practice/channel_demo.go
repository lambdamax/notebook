package main

import "fmt"

func main() {
	ch := make(chan int, 5)

	go func() {
		for i := 0; i <= 10; i++ {
			fmt.Println("向c推入:", i)
			ch <- i
		}
		close(ch)
	}()

	fmt.Println("begin")
	for v := range ch {
		fmt.Println("从c取出：", v)
	}
	fmt.Println("over")
}
