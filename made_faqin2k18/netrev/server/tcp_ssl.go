package main
//La FLAG es el MD5 del ID xoreado con 8===D
import (
	 "log"
	 "crypto/tls"
	 "crypto/md5"
	 "encoding/hex"
	 "net"
	 "strings"
)

func xor(a, key string)[]byte{
   k := []byte(key)
	 aa := []byte(a)
   for len(k) < len(aa) {
      k = append(k, k...)
   }
   var dst []byte
   for i := 0; i < len(aa); i++ {
      dst = append(dst, aa[i] ^ k[i])
   }
   return dst
}

func handle(conn net.Conn) {
	 defer conn.Close()
	 buf := make([]byte, 64)
	 n, err := conn.Read(buf)
	 if err != nil {
			log.Println("Error reading:", err.Error())
			return
	 }
	 in := string(buf[:n])
	 spl := strings.SplitN(in, "|", 2)
	 log.Println("IP: " + conn.RemoteAddr().String() + "\nData: " + in)
	 if (n > 20) && (in[0:17] == "8==============D|") && (len(spl[1]) == 32){
			hasher := md5.New()
			hasher.Write(xor(spl[1], "8===D"))
			conn.Write(xor("faq1n{" + hex.EncodeToString(hasher.Sum(nil)) + "}", "iPLBEsf6CmvJJbSmrMiQq/E7PxBbXA5DqCk8oL"))
	 }else{
			conn.Write([]byte("¯\\_(ツ)_//¯"))
	 }
}

func main(){
	 cert, err := tls.LoadX509KeyPair("cert.pem", "key.pem")
	 if err != nil {
			log.Fatal("Error loading certificate. ", err)
	 }

	 tlsCfg := &tls.Config{Certificates: []tls.Certificate{cert}}

	 listener, err := tls.Listen("tcp4", "0.0.0.0:15555", tlsCfg)
	 if err != nil {
			log.Fatal(err)
	 }
	 defer listener.Close()

	 log.Println("Waiting for clients")
	 for{
			conn, err := listener.Accept()
			if err != nil {
				 log.Fatal(err)
			}
			go handle(conn)
	 }
}
