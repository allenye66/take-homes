/*
2
4
3 -1 1 14
5
9 6 -53 32 16
*/

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	Scanner := bufio.NewScanner(os.Stdin)
	answer := []int{}
	recur(0, 0, Scanner, answer)

}

func find_sum(digits []string) int {

	current_num, err := strconv.Atoi(digits[0])
	if err != nil {
		os.Exit(1)
	}

	current_square := current_num * current_num
	remainder_array := digits[1:]

	if len(remainder_array) == 0 {
		return current_square
	}
	if current_num > 0 {
		return current_square + find_sum(remainder_array)
	} else {
		return 0 + find_sum(remainder_array)
	}

}

func print_arr(arr []int) {
	if len(arr) == 0 {
		return
	}
	fmt.Println(arr[0])
	print_arr(arr[1:])
}

func recur(num int, queries int, Scanner *bufio.Scanner, answer []int) {
	Scanner.Scan()
	input := Scanner.Text()
	if num == 0 {
		i, err := strconv.Atoi(input)
		if err != nil || (err == nil && i == 0) {
			os.Exit(0)
		}
		queries = i
	}

	if num > 0 && num%2 == 0 {
		answer = append(answer, find_sum(strings.Split(input, " ")))
	}

	if queries == num/2 {
		print_arr(answer)
		return
	} else {
		num += 1
		recur(num, queries, Scanner, answer)
	}
	return
}
