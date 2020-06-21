package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	//var name string
	//name = "我"
	var name = "我"
	fmt.Printf("%T %s %p", name, name, &name)
	fmt.Println()

	name = "我2"
	fmt.Printf("%T %s %p", name, name, &name)
	fmt.Println()

	const (
		a = iota
		b
	)
	fmt.Println(a, b)

	var c = 3.16
	fmt.Printf("%T,%v,%.1f\n", c, c, c)

	var d = `3.16`
	fmt.Printf("%T,%v\n", d, d)

	var e = int(c)
	fmt.Printf("%T,%v\n", e, e)

	f := false && true
	fmt.Printf("%T,%t\n", f, f)

	g := 60
	h := 13
	fmt.Printf("%d,%b\n", g, g)
	fmt.Printf("%d,%b\n", h, h)

	fmt.Printf("%b\n", g^h)

	//var i int
	//fmt.Println("输入数字")
	//fmt.Scanln(&i)
	//fmt.Println(i)

	rand.Seed(time.Now().Unix())
	fmt.Println(rand.Intn(1000) + 1000)

	var arr1 [4]int
	fmt.Println(arr1)
	arr2 := [4]int{1, 2, 3, 4}
	fmt.Println(arr2)
	arr3 := [4]int{1: 100, 3: 100}
	fmt.Println(arr3)

	for _, v := range arr3 {
		fmt.Println(v)
	}

	var arr4 [3][4]int
	fmt.Println(arr4)
	fmt.Printf("%p %p", &arr4, &arr4[1])

	arr5 := [3][4]int{{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}}
	for _, arr := range arr5 {
		for _, v := range arr {
			fmt.Println(v)
		}
	}

	s1 := make([]int, 5, 20)
	s1 = append(s1, 2, 5)
	fmt.Println(s1)
	fmt.Printf("%p\n", &s1) //指向slice本身地址
	fmt.Printf("%p\n", s1)  //指向slice内数组的地址 等同于 &s1[0]
	fmt.Printf("%p\n", s1[:1])
	fmt.Printf("%p\n", s1[1:])

}
