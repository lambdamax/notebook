package main

import (
	"fmt"
	"reflect"
)

func main() {
	s1 := Student2{"李四", 20, "清华"}

	//通过reflect改变对象的值，前提是数值可以被改变
	fmt.Printf("%T\n", s1) //main.Student2
	p1 := &s1
	fmt.Printf("%T\n", p1) //*main.Student2
	fmt.Println((*p1).Name, p1.Name)

	//改变数值
	value := reflect.ValueOf(&s1)
	if value.Kind() == reflect.Ptr {
		newvalue := value.Elem()
		fmt.Println(newvalue.CanSet())
		f1 := newvalue.FieldByName("Name")
		f1.SetString("李四二")
		f3 := newvalue.FieldByName("School")
		f3.SetString("北大")
	}
	fmt.Println(s1)

	//通过reflect进行方法调用
	s2 := Student2{"王五", 25, "交大"}
	value2 := reflect.ValueOf(s2)
	methodvalue1 := value2.MethodByName("Study")
	fmt.Printf("%s %s\n", methodvalue1.Kind(), methodvalue1.Type()) //Kind()==func 才可以通过reflect调用

	methodvalue1.Call(nil)
	//空切片也可以
	arg1 := make([]reflect.Value, 0)
	methodvalue1.Call(arg1)
	//有值传递
	methodvalue2 := value2.MethodByName("Play")
	arg2 := []reflect.Value{reflect.ValueOf("王者荣耀")}
	methodvalue2.Call(arg2)

	methodvalue3 := value2.MethodByName("Test")
	arg3 := []reflect.Value{reflect.ValueOf("王者荣耀"), reflect.ValueOf(1), reflect.ValueOf(3.14)}
	methodvalue3.Call(arg3)
}

type Student2 struct {
	Name   string
	Age    int
	School string
}

func (s Student2) Study() {
	fmt.Println("学习方法。。")
}

func (s Student2) Play(game string) {
	fmt.Println("玩游戏：", game)
}

func (s Student2) Test(a ...interface{}) {
	for _, v := range a {
		fmt.Println("玩游戏：", v)
	}

}
