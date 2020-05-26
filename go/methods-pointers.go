package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

//若不使用指针则会对原始Vertex值的副本进行操作
func (v Vertex) Scale1(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

//使用指针类型可以修改接受者指向的值
func (v *Vertex) Scale2(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func main() {
	v := Vertex{3, 4}
	v.Scale1(10)
	fmt.Println(v.Abs())
	v.Scale2(10)
	fmt.Println(v.Abs())
}
