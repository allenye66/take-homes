package main

import (
	"fmt"
)

func main() {

	var n int

	fmt.Scan(&n)

	for n > 0 {
		var len int
		fmt.Scan(&len)
		arr := make([]int, len)

		for i := 0; i < len; i++ {
			var temp int
			fmt.Scan(&temp)
			arr[i] = temp
		}
		//fmt.Println(arr)

		var sum int
		for i := 0; i < len; i++ {
			if arr[i] > 0 {
				sum += arr[i] * arr[i]
			}
		}
		fmt.Println(sum)

		n--
	}
}
