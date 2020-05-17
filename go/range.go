package main

import "fmt"

var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}

func main() {
	//遍历切片时，第一个值为当前元素的下标，第二个值为该下标所对应元素的一份副本
	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)
	}

	pow := make([]int, 10)
	for i := range pow {
		pow[i] = 1 << uint(i) // == 2**i
	}
	fmt.Println(pow)
	for _, value := range pow {
		fmt.Printf("%d\n", value)
	}
}
