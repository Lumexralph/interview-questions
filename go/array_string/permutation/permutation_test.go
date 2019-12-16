package permutation

import "testing"

func TestCheckPermutation(t *testing.T) {
	cases := []struct {
		name, inputA, inputB string
		want                 bool
	}{
		{"with inputs of same character and different order", "abcd", "dcba", true},
		{"with inputs of different character", "abcg", "dcbf", false},
		{"with inputs of different length", "abcdanfb", "dcba", false},
		{"with inputs of repeated same characters", "abcdb", "bdcba", true},
	}

	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			got := checkPermutation(tc.inputA, tc.inputB)

			if got != tc.want {
				t.Errorf("checkPermutation(%q, %q) got %v; want %v", tc.inputA, tc.inputB, got, tc.want)
			}
		})
	}
}
