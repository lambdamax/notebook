package main

import "fmt"

func main() {
	var i interface{} = "hello"

	s := i.(string)
	fmt.Println(s)

	s, ok := i.(string)
	fmt.Println(s, ok)

	f, ok := i.(float64)
	fmt.Println(f, ok)

	//该语句断言接口值 i 保存了具体类型 T，并将其底层类型为 T 的值赋予变量 t。
	//若 i 并未保存 T 类型的值，该语句就会触发一个恐慌。

	//f = i.(float64) // 报错(panic)
	//fmt.Println(f)
}
