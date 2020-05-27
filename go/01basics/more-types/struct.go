package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

var (
	v1 = Vertex{1, 2}  // 创建一个 Vertex 类型的结构体
	v2 = Vertex{X: 1}  // Y:0 被隐式地赋予
	v3 = Vertex{}      // X:0 Y:0
	p1 = &Vertex{1, 2} // 创建一个 *Vertex 类型的结构体（指针）
)

func main() {
	v := Vertex{1, 2}
	p := &v
	p.X = 1e9
	fmt.Println(p.X) //隐式间接引用，等同于(*p).X
	fmt.Println((*p).X)
	fmt.Println(v)

	fmt.Println(v1, p1, v2, v3)
}
