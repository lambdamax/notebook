package main

import "fmt"

func main() {
	arr1 := [4]int{1, 2, 3, 4}
	fmt.Println(arr1)
	fmt.Printf("arr1本身的地址:%p\n", &arr1)
	//数组指针
	var p1 *[4]int
	p1 = &arr1
	fmt.Println(p1)
	fmt.Printf("p1值的地址:%p\n", p1)
	fmt.Printf("p1自己的地址:%p\n", &p1)
	//访问数组指针中的元素
	(*p1)[0] = 100
	fmt.Println(arr1)

	p1[0] = 200 //简化
	fmt.Println(arr1)

	//数组指针
	a := 0
	b := 1
	c := 2
	arr2 := [3]int{a, b, c}
	arr3 := [3]*int{&a, &b, &c}
	fmt.Println(arr2)
	fmt.Println(arr3)
	arr2[0] = 100  //值传递
	fmt.Println(a) //未改变
	*arr3[0] = 200 //引用传递
	fmt.Println(a) //a的值被改变
}
