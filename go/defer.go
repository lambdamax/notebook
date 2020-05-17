package main

import "fmt"

func main() {
	//延迟调用
	defer fmt.Println("world")

	fmt.Println("hello")

	//defer栈 按后进先出顺序
	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}
}
