package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	z := float64(1)
	num := float64(0)
	for {
		z -= (z*z-x)/(2*z)
		if math.Abs(num-z) < 1e-10 {
			return num
		}
		num = z
	}
}

func main() {
	fmt.Println(Sqrt(2))
	fmt.Println(math.Sqrt(2))
}
