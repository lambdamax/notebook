package main

import "fmt"

func main() {
	//匿名函数捕获panic，使程序recover
	defer func() {
		if msg := recover(); msg != nil {
			fmt.Println(msg)
		}
	}()
	fmt.Println("MAIN开始")
	C()
	D()
	fmt.Println("MAIN结束")
}

func C() {
	defer fmt.Println("C开始")
	defer fmt.Println("C结束")
}

func D() {
	defer fmt.Println("D开始")
	for _, v := range [4]int{1, 2, 3, 4} {
		if v > 3 {
			panic("v不能大于3")
		}
		fmt.Println(v)
	}
	defer fmt.Println("D结束")
}
