package main

import (
	 "crypto/tls"
	 "io"
	 "fmt"
	 "log"
)

func xor(a []byte)string{
	 k := []byte("iPLBEsf6CmvJJbSmrMiQq/E7PxBbXA5DqCk8oL")
	 for len(k) < len(a) {
			k = append(k, k...)
	 }
	 dst := ""
	 for i := 0; i < len(a); i++ {
			dst += string(a[i] ^ k[i])
	 }
	 return dst
}

func check(err error){
	 if err != nil {
			log.Fatalf("Error: %s", err)
	 }
}

func main() {
	 config := tls.Config{InsecureSkipVerify: true}
	 conn, err := tls.Dial("tcp4", "wopr.rocks:15555", &config)
	 check(err)
	 defer conn.Close()

	 //fmt.Println("client: connected to: ", conn.RemoteAddr())

	 _, err = io.WriteString(conn,
    "8==============D|AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
	 check(err)
	 reply := make([]byte, 64)
	 n, _ := conn.Read(reply)
	 //fmt.Printf("client: read %q (%d bytes)\n", string(reply[:n]), n)
    res := xor(reply[:n])
    res = res + ""
	 fmt.Println("Ups! Wrong data printed...")
}
