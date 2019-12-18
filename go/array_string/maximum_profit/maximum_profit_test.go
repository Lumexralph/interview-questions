package maxprofit

import (
	"testing"
)

func TestMaximumProfit(t *testing.T) {
	cases := []struct{
		name string
		prices []int
		want int
	}{
		{"with prices that has maximum profit", []int{7,1,5,3,6,4}, 5},
		{"with another set of prices", []int{2, 4, 1}, 2},
		{"with prices that has no maximum profit", []int{7,6,4,3,1}, 0},
	}

	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T){
			got := maxProfit(tc.prices)

			if got != tc.want {
				t.Errorf("maxProfit(%v) got=%d; want=%d", tc.prices, got, tc.want)
			}
		})
	}

}
