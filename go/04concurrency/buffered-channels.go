package main

import "fmt"

func main() {
	//为 make 提供第二个参数作为缓冲长度来初始化一个缓冲 channel
	c := make(chan int, 2)
	c <- 1
	c <- 2
	fmt.Println(<-c)
	c <- 3
	fmt.Println(<-c)
	fmt.Println(<-c)
}
