// Package compress contains implementation of compression algorithms
package compress

import (
	"strconv"
	"strings"
)

// String - compresses the input and return it
func String(input string) string {
	// use string builder to avoid memory allocation
	// required to join new and old string
	var output strings.Builder
	charCount := make(map[string]int)

	for i := 0; i < len(input); i++ {
		// collate the occurrence of the bytes
		charCount[string(input[i])]++
		// look ahead index
		if next := i + 1; next < len(input) {
			if input[i] != input[next] {
				// do a clean up and build the string
				output.WriteString(string(input[i]))
				count := strconv.Itoa(charCount[string(input[i])])
				output.WriteString(count)

				// reset the charCount
				delete(charCount, string(input[i]))
			}
		} else {
			// get the last byte result
			output.WriteString(string(input[i]))
			count := strconv.Itoa(charCount[string(input[i])])
			output.WriteString(count)
		}
	}

	if len(output.String()) == len(input) {
		return input
	}
	return output.String()
}
