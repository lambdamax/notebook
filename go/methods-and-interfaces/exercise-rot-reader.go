package main

import (
	"io"
	"os"
	"strings"
)

type rot13Reader struct {
	r io.Reader
}

func (t rot13Reader) Read(k []byte) (int, error) {
	n, err := t.r.Read(k)
	for i := range k {
		if (k[i] >= 'A' && k[i] <= 'M') || (k[i] >= 'a' && k[i] <= 'm') {
			k[i] = byte(int(k[i]) + 13)
		} else if (k[i] > 'M' && k[i] <= 'Z') || (k[i] > 'm' && k[i] <= 'z') {
			k[i] = byte(int(k[i]) - 13)
		}
	}
	return n, err
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}
