package main

import "fmt"

func main() {
	var p1 Person
	p1.Name = "Max"
	p1.Age = 20
	p1.Sex = "male"
	p1.Addr = "Shanghai"
	fmt.Println(p1)

	p2 := Person{}
	p2.Name = "Max"
	p2.Age = 20
	p2.Sex = "male"
	p2.Addr = "Shanghai"
	fmt.Println(p2)

	//结构体指针，实现浅拷贝
	var p3 *Person
	p3 = &p2
	fmt.Println(p2)
	p3.Name = "Mike"
	fmt.Println(p2)

	//new()，专门用于创建某种类型的指针的函数, 返回值为指针，默认值指针，非nil
	//与make不同，make ->slice map channel 返回值非指针
	p4 := new(Person)
	fmt.Println(p4)
	p4 = p3
	fmt.Println(p4)
	//方法，需指定调用者
	p3.work()
	p3.rest()

	//子类访问父类方法
	s1 := Student{p2, "北大"}
	s1.work()
	s1.rest()
}

type Person struct {
	Name string
	Age  int
	Sex  string
	Addr string
}

func (p Person) work() {
	fmt.Println(p.Name, "在工作")
}

func (p *Person) rest() {
	fmt.Println(p.Name, "在休息")
}

type Student struct {
	Person
	school string
}
