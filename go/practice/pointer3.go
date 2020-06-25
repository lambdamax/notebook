package main

import "fmt"

func main() {
	/*
		slice map function 函数指针
	*/
	var a func()
	a = fun1 //函数指针：go中的function默认看做一个指针，没有* （fun1的地址赋值给a）
	a()

	b := fun2()
	fmt.Printf("类型：%T  本身地址：%p 值地址：%p  值：%v\n", b, &b, b, b)

	//指针传递
	n := 10
	fun3(n)
	fmt.Println(n) //10

	fun4(&n)
	fmt.Println(n) //100
}

func fun1() {
	fmt.Println("func1()....")
}

func fun2() *[4]int {
	arr := [4]int{1, 2, 3, 4}
	fmt.Printf("arr本身地址：%p\n", &arr)
	return &arr
}

func fun3(n int) {
	fmt.Println(n)
	n = 100
	fmt.Println(n)
}

func fun4(n *int) {
	fmt.Println(*n)
	*n = 100
	fmt.Println(*n)
}
