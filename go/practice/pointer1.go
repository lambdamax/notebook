package main

import "fmt"

func main() {
	a := 10
	fmt.Println("a的数值:", a)
	fmt.Printf("a的类型:%T\n", a)
	fmt.Printf("a的地址:%p\n", &a)

	fmt.Println("————————————————————————————")

	var p1 *int
	fmt.Println("p1的数值:", p1)
	p1 = &a
	fmt.Printf("p1数值（a的地址）:%p\n", p1)
	fmt.Printf("p1自己的地址:%p\n", &p1)
	fmt.Println("p1数值（a）的值:", *p1)

	fmt.Println("————————————————————————————")

	var p2 **int
	fmt.Println("p2的数值:", p2)
	p2 = &p1
	fmt.Printf("p2的数值（p1的地址）:%p\n", p2)
	fmt.Printf("p2自己的地址:%p\n", &p2)
	fmt.Println("p2数值（p1）的值:", *p2)
	fmt.Println("p2数值（p1）的值（a）的值:", **p2)
}
