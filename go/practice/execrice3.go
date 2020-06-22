package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	m1 := make(map[string]string)
	m1["name"] = "姓名"
	m1["age"] = "12"
	m1["addr"] = "上海"
	m1["sex"] = "male"
	fmt.Println(m1)
	m2 := make(map[string]string)
	m2["name"] = "姓名2"
	m2["age"] = "12"
	m2["addr"] = "上海2"
	m2["sex"] = "male2"
	fmt.Println(m2)

	s1 := make([]map[string]string, 0)
	s1 = append(s1, m1, m2)
	fmt.Printf("len:%d cap:%d \n", len(s1), cap(s1))
	s1 = append(s1, m1, m2)
	fmt.Printf("len:%d cap:%d \n", len(s1), cap(s1))

	m3 := make(map[string]map[string]string)
	m31 := make(map[string]string)
	m31["name"] = "李四"
	m31["age"] = "30"
	m3["第一个人"] = m31
	m32 := make(map[string]string)
	m32["name"] = "李四"
	m32["age"] = "30"
	m3["第二个人"] = m31
	fmt.Println(m3)

	m4 := m3
	fmt.Printf("%p %p\n", m3, m4)

	str1 := "abcabsghijk.txt"
	fmt.Println(strings.ContainsAny(str1, "adef"))
	fmt.Println(strings.Count(str1, "ab"))
	fmt.Println(strings.HasPrefix(str1, "ab"))
	fmt.Println(strings.HasSuffix(str1, ".txt"))
	fmt.Println(strings.Index(str1, "b"))
	fmt.Println(strings.Index(str1, "bcd"))

	str2 := "true"
	r2, err := strconv.ParseBool(str2)
	if err == nil {
		fmt.Println(r2)
	}
	str3 := "100"
	r3, err := strconv.ParseInt(str3, 10, 64)
	if err == nil {
		fmt.Println(r3)
	}

}
