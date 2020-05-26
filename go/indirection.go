package main

import "fmt"

type Vertex struct {
	X, Y float64
}

func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func ScaleFunc(v *Vertex, f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func main() {
	v := Vertex{3, 4}
	//带指针参数的函数必须接受一个指针
	v.Scale(2)
	ScaleFunc(&v, 10)

	p := &Vertex{4, 3}
	//指针为接收者的方法被调用时，接收者既能为值又能为指针
	p.Scale(3)
	ScaleFunc(p, 8)

	fmt.Println(v, p)
}
