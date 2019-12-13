// Package permutation has the implementation of operations
// that has to do do it with strings and permutations
package permutation

func checkPermutation(inputA, inputB string) bool {
	// validation
	if len(inputA) != len(inputB) {
		return false
	}

	inputACharSet := make(map[rune]int)

	for _, char := range inputA {
		inputACharSet[char]++
	}

	for _, char := range inputB {

		if _, ok := inputACharSet[char]; ok {
			if inputACharSet[char] == 0 {
				return false
			}
			inputACharSet[char]--
		} else {
			return false
		}
	}
	return true
}
