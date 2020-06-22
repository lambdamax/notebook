package main

import (
	"fmt"
)

func main() {

	f1 := getSum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
	fmt.Println(f1)

	s1 := make([]int, 0)
	s1 = append(s1, 1, 2, 3, 4)
	getSumFromSlice(s1)
	fmt.Println(s1) //切片为引用传递

	s2 := [4]int{1, 2, 3, 4}
	s21 := getSumFromArray(s2)
	fmt.Println(s21)
	fmt.Println(s2) //数组为值传递

	a, b := getSize(5, 6)
	fmt.Println(a, b)

}

func getSum(nums ...int) int {
	fmt.Printf("%T", nums)
	sum := 0
	for _, v := range nums {
		sum += v
	}
	fmt.Println(sum)
	return sum
}

func getSumFromSlice(s []int) []int {
	fmt.Println(s)
	s[1] = 100
	fmt.Println(s)
	return s
}

func getSumFromArray(s [4]int) (a1 [4]int) {
	fmt.Println(s)
	s[1] = 100
	fmt.Println(s)
	a1 = s
	return
}

func getSize(a, b int) (int, int) {
	return a * b, a + b
}
