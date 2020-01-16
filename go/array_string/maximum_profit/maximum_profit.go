// Package maxprofit contains the implementation of the
// maximum profit algorithm with a time complexity O(n) and
// space complexity of O(1)
package maxprofit

func maxProfit(prices []int) int {
	buyPrice := 1<<63 - 1
	profit := 0

	for _, price := range prices {
		if price < buyPrice {
			buyPrice = price
		} else if p := price - buyPrice; p > profit {
			profit = p
		}
	}

	return profit
}
