package main

import "fmt"

type Rect struct {
	width  float64
	height float64
}

func (r *Rect) size() float64 {
	return r.width * r.height
}

func main() {
	//&是取地址符号, 取到Rect类型对象的地址
	fmt.Println(&Rect{100, 100})

	//*可以表示一个变量是指针类型(r是一个指针变量)
	var r *Rect = &Rect{100, 100}

	//.*也可以表示指针类型变量所指向的存储单元 ,也就是这个地址所指向的值
	fmt.Println(*r)

	//查看这个指针变量的地址 , 基本数据类型直接打印地址
	fmt.Println(&r)
}
