package main

import (
	"fmt"
	"log"
	"net/http"
)

type String string

type Struct struct {
	Greeting string
	Punct    string
	Who      string
}

func (s String) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, String("I'm a frayed knot."))
}

func (s *Struct) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	rs := &Struct{"Hello", ":", "Gophers!"}
	fmt.Fprint(w, rs)
}

func main() {
	var s1 String
	var s2 Struct
	// your 03http.Handle calls here
	http.Handle("/string", http.HandlerFunc(s1.ServeHTTP))
	http.Handle("/struct", http.HandlerFunc(s2.ServeHTTP))
	log.Fatal(http.ListenAndServe("localhost:9090", nil))
}
