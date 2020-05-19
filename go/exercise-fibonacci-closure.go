package main

import "fmt"

// 实现一个 fibonacci 函数，它返回一个函数（闭包），该闭包返回一个斐波纳契数列 `(0, 1, 1, 2, 3, 5, ...)`。
// 闭包实现
func fibonacci() func() int {
	b1, b2 := 0, 1
	return func() int {
		b1, b2 = b2, b1+b2
		return b1
	}
}

// 递归实现
func fibonacci2(n int) int {
	if n < 2 {
		return n
	} else {
		return fibonacci2(n-2) + fibonacci2(n-1)
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
		fmt.Println(fibonacci2(i))
	}
}
