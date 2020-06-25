package main

import (
	"fmt"
)

func main() {
	fmt.Printf("%T\n", f1)
	fmt.Println(f1)
	var b func(int) int
	b = f1
	fmt.Println(b)
	fmt.Println(b(2))

	//匿名函数
	func(n int) {
		fmt.Println(n)
	}(3)
	c := func(n int) {
		fmt.Println(n)
	}
	c(4)

	//回调函数
	add(10, 20)
	oper(100, 200, add)

	//闭包
	d := increment()
	fmt.Println(d)
	fmt.Printf("%p %d\n", d, d())
	fmt.Printf("%p %d\n", d, d())
}

func f1(n int) int {
	fmt.Println(n)
	return n
}

func f2(n int) int {
	a := 2
	defer f1(a) //2传入，延迟执行
	a++
	defer f1(a) //3传入，延迟执行
	fmt.Println(n)
	return n
}

func add(a, b int) int {
	fmt.Println(a, b)
	return a + b
}

func oper(a, b int, fun func(int, int) int) int {
	fmt.Println(a, b, fun)
	fmt.Println(fun(a, b))
	return 0
}

func increment() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}
