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

func AbsFunc(v Vertex) float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := Vertex{3, 4}
	p := &Vertex{4, 3}

	//而以值为接收者的方法被调用时，接收者既能为值又能为指针
	fmt.Println(v.Abs())
	fmt.Println(p.Abs())
	//接受一个值作为参数的函数必须接受一个指定类型的值
	fmt.Println(AbsFunc(v))
	fmt.Println(AbsFunc(*p))
}
