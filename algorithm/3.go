package main

import (
	"fmt"
)

func main() {
	number := 1345679
	output := convertNumber(number)
	for i := len(output)-1; i >= 0; i--{
		fmt.Println(output[i])
	}
}

func convertNumber(number int) ([]int) {
	var zeros int
	var outputs []int
	zeros = 1
	for number > 0 {
		num := number % 10
		outputs = append(outputs, num*zeros)
		number = number / 10
		zeros = zeros * 10
	}
	return outputs
}
