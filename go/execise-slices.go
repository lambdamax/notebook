package main

import "golang.org/x/tour/pic"

//实现 Pic。它应当返回一个长度为 dy 的切片，其中每个元素是一个长度为 dx，元素类型为 uint8 的切片
func Pic(dx, dy int) [][]uint8 {
	image := make([][]uint8, dy)
	for i := range image {
		image[i] = make([]uint8, dx)
		for j := 0; j < dx; j++ {
			image[i][j] = uint8((i * j))
		}
	}
	return image
}

func main() {
	pic.Show(Pic)
}
