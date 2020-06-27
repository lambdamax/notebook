package main

import (
	"errors"
	"fmt"
	"math"
)

func main() {
	fmt.Println(checkNums(19))

	s, err := checkCircle(-1)
	if err != nil {
		if err, ok := err.(*areaError); ok {
			fmt.Println(err)
		} else {
			fmt.Println("其他错误")
		}
		return
	}
	fmt.Println(s)
}

func checkNums(n int) error {
	if n > 10 {
		return errors.New("年龄超过10")
	}
	return nil
}

//自定义错误
type areaError struct {
	msg    string
	radius float64
}

//areaError实现error方法
func (e *areaError) Error() string {
	return fmt.Sprintf("半径 %.2f 不合法", e.radius)
}

func checkCircle(r float64) (float64, error) {
	if r < 0 {
		return 0, &areaError{msg: "非法半径", radius: r}
	}
	return math.Pi * r * r, nil
}
