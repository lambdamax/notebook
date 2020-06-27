package main

import (
	"fmt"
)

func main() {
	var t1 T = A{first: 10, last: 5}
	var t2 T = B{first: 15, last: 5}
	//t1.add()
	//t1.sub()
	//t2.add()
	//t2.sub()

	testrun(t1)
	testrun(t2)
}

func testrun(s T) {
	//接口断言
	//方法一
	if ins, ok := s.(A); ok {
		fmt.Println("是A ", ins.first, ins.last)
	} else if ins, ok := s.(B); ok {
		fmt.Println("是B ", ins.first, ins.last)
	}
	//方法二
	switch ins := s.(type) {
	case A:
		fmt.Println("是A ", ins.first, ins.last)
	case B:
		fmt.Println("是B ", ins.first, ins.last)
	}

	fmt.Println(s.add())
	fmt.Println(s.sub())
}

type T interface {
	add() float64
	sub() float64
}

type A struct {
	first, last float64
}

func (p A) add() float64 {
	return p.first + p.last
}
func (p A) sub() float64 {
	return p.first - p.last
}

type B struct {
	first, last float64
}

func (p B) add() float64 {
	return p.first + p.last
}
func (p B) sub() float64 {
	return p.first - p.last
}
