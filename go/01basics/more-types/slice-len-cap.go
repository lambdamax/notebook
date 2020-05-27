package main

import "fmt"

func main() {
	s := []int{2, 3, 5, 7, 11, 13}
	printSlice(s)

	// 截取切片使其长度为 0
	s = s[:0]
	printSlice(s)

	// 拓展其长度
	s = s[:4]
	printSlice(s)

	// 舍弃前两个值
	s = s[2:]
	printSlice(s)

	//切片的零值是 nil。
	//nil 切片的长度和容量为 0 且没有底层数组。
	var s1 []int
	fmt.Println(s1, len(s1), cap(s1))
	if s1 == nil {
		fmt.Println("nil!")
	}
}

func printSlice(s []int) {
	//len长度,cap容量
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}
