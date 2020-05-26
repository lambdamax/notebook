package main

import "fmt"

type I interface {
	M()
}

type T struct {
	S string
}

// 此方法表示类型 T 实现了接口 I，但我们无需显式声明此事。
func (t T) M() {
	fmt.Println(t.S)
}

func main() {
	//隐式调用，等同于var i I
	//				i = T{"hello"}
	var i I = T{"hello"}
	i.M()
}
