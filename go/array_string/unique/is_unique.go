// Package unique contains the implementation of
// an algorithm that  checks the characters of a
// string are unique with time complexity of O(n)
// and space complexity amortized O(1) - O(n)
// if the whole string is an ASCII, we'll be dealing
// with 128 characters and if it is Unicode, it will be more.
package unique

func isUnique(words string) bool {
	visited := make(map[rune]bool)

	for _, char := range words {
		if _, ok := visited[char]; ok {
			return false
		}
		visited[char] = true
	}
	return true
}
