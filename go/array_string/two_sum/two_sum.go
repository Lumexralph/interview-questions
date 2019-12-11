// Package twosum contains the implementation of
// the two sum algorithm solution with O(n) complexity
// and also an amortized O(1) complexity.
package twosum

func searchIndex(nums []int, target int) []int {
	// we need to keep a record of element visited
	// and their index, to avoid iterating the nums
	// array multiple times so as to find a match with target
	visited := make(map[int]int)

	for i, num := range nums {
		// check if the remaining value is among visited elements
		if index, ok := visited[target - num]; ok {
			return []int{index, i}
		}

		// update the visited record
		visited[num] = i
	}

	return nil
}