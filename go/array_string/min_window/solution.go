// package main has the solution for the minimum window
// algorithm implementation using the sliding window technique.
package main

import (
	"fmt"
	"math"
	"strings"
)

func minWindow(mainStr, subStr string) string {
	// validation
	if len(mainStr) == 0 || len(subStr) == 0 || len(subStr) > len(mainStr) {
		return ""
	}
	// using the sliding window technique.
	// create hashmap for required and desired character.
	required := make(map[string]int)
	desired := make(map[string]int)
	// ensure it is the count of the unique keys in desired
	// and not the subStr incase of repeated characters.
	substrCount := 0

	// populate the desired and required hashmaps
	for _, char := range subStr {
		desired[string(char)] = 0

		// create the new hashmap with the count of the required
		// characters in the subStr.
		if _, ok := required[string(char)]; !ok {
			// if the character has not been accounted of.
			substrCount++ // count the unique characters
			required[string(char)] = strings.Count(subStr, string(char))
		}
	}

	var slowPointer, fastPointer uint64
	minWindowRange := []uint64{0, math.MaxUint64}

	// enlarge the window to get the desirable character range
	for fastPointer < uint64(len(mainStr)) {
		// check if there is range match
		char := string(mainStr[fastPointer])

		if _, ok := desired[char]; ok {
			desired[char]++

			// check if the window contains the matching required characters
			desiredValue := desired[char]
			requiredValue := required[char]
			if desiredValue == requiredValue {
				// there is match of part of the characters in the subStr
				// reduce the number of characters we're looking
				substrCount--
			}
		}

		// progress the fast pointer
		fastPointer++

		// shrink the current window by moving the slowPointer.
		for substrCount == 0 {
			// make a check for the smallest or shortest substring window.
			if uint64(fastPointer-slowPointer) < (minWindowRange[1] - minWindowRange[0]) {
				// update the shortest window
				minWindowRange[0] = slowPointer
				minWindowRange[1] = fastPointer
			}

			// we need to check when there is match in the character
			// pointed by the slowPointer, then decrement the value by 1.
			char := string(mainStr[slowPointer])

			if _, ok := desired[char]; ok {
				desired[char]--

				// if the count of desired is less than the count of required
				// means a required character is misssing
				desiredValue := desired[char]
				requiredValue := required[char]

				if desiredValue < requiredValue {
					substrCount++
				}
			}

			// progress the slowPointer
			slowPointer++
		}
	}

	// if there is no match in the window
	if minWindowRange[1] == math.MaxUint64 {
		return ""
	}
	return mainStr[minWindowRange[0]:minWindowRange[1]]
}

func main() {
	fmt.Println(minWindow("ADOBECODEBANC", ""))
}
