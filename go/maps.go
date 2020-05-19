package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m = map[string]Vertex{
	"Bell Labs": Vertex{
		40.68433, -74.39967,
	},
	"Google": Vertex{
		37.42202, -122.08408,
	},
}

//若顶级类型只是一个类型名，你可以在文法的元素中省略它。
var m1 = map[string]Vertex{
	"Bell Labs": {40.68433, -74.39967},
	"Google":    {37.42202, -122.08408},
}

func main() {
	fmt.Println(m)
	fmt.Println(m["Google"].Long)
	fmt.Println(m1)

	//修改map
	m := make(map[string]int)

	m["Answer"] = 42
	fmt.Println("The value:", m["Answer"])

	m["Answer"] = 48
	fmt.Println("The value:", m["Answer"])

	//若 key 在 m 中，ok 为 true ；否则，ok 为 false。
	//若 key 不在映射中，那么 elem 是该映射元素类型的零值。
	//同样的，当从映射中读取某个不存在的键时，结果是映射的元素类型的零值。
	v, ok := m["Answer"]
	fmt.Println("The value:", v, "Present?", ok)

	delete(m, "Answer")
	fmt.Println("The value:", m["Answer"])

	v, ok = m["Answer"]
	fmt.Println("The value:", v, "Present?", ok)
}
