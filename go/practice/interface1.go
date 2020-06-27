package main

import "fmt"

func main() {
	m1 := Mouse{Name: "罗技鼠标"}
	k1 := Keyboard{Name: "逻辑键盘"}

	testusb(m1)
	testusb(k1)
	var usb USB
	usb = m1
	usb.begin()

	//空接口
	slice1 := make([]interface{}, 0, 10)
	slice1 = append(slice1, "string", 10, 3.14, map[string]int{"a1": 1, "a2": 2})
	fmt.Println(slice1)

}

type USB interface {
	begin()
	end()
}

type Mouse struct {
	Name string
}
type Keyboard struct {
	Name string
}

func (p Mouse) begin() {
	fmt.Println(p.Name, "鼠标开始")
}

func (p Mouse) end() {
	fmt.Println(p.Name, "鼠标结束")
}
func (p Keyboard) begin() {
	fmt.Println(p.Name, "键盘开始")
}

func (p Keyboard) end() {
	fmt.Println(p.Name, "键盘结束")
}

func testusb(usb USB) {
	usb.begin()
	usb.end()
}
