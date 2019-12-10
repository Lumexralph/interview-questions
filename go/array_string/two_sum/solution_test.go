package solution

import (
	"testing"

	"github.com/google/go-cmp/cmp"
)

func TestTwoSum(t *testing.T) {
	cases := []struct {
		name   string
		input  []int
		target int
		want   []int
	}{
		{"with array elements that match the target", []int{0, 2, 4, 6, 7}, 13, []int{3, 4}},
		{"with array elements that does not sum to target", []int{0, 2, 4, 6, 7}, 20, []int{}},
	}

	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			got := twoSum(tc.input, tc.target)

			if diff := cmp.Diff(got, tc.want); diff != "" {
				t.Errorf("twoSum(%v, %v) mismatch (-want +got):\n%s", tc.input, tc.target, diff)
			}
		})
	}
}
