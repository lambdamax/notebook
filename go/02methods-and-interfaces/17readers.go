package main

import (
	"fmt"
	"io"
	"strings"
)

func main() {
	//io.Reader 接口有一个 Read 方法：
	//func (T) Read(b []byte) (n int, err error)
	r := strings.NewReader("Hello, Reader!")

	//每次 8 字节的速度读取它的输出
	b := make([]byte, 8)
	for {
		n, err := r.Read(b)
		fmt.Printf("n = %v err = %v b = %v\n", n, err, b)
		fmt.Printf("b[:n] = %q\n", b[:n])
		//在遇到数据流的结尾时，它会返回一个 io.EOF 错误。
		if err == io.EOF {
			break
		}
	}
}
