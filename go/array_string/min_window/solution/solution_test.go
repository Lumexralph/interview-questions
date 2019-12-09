package solution

import "testing"

func TestMinWindow(t *testing.T) {
	cases := []struct {
		name, mainString, substring, want string
	}{
		{"minimum substring with repeated character", "ADOBECODEBANC", "OBOC", "OBECO"},
		{"minimum substring with unique character", "ADOBECODEBANC", "ABC", "BANC"},
		{"use string input without match", "a", "b", ""},
		{"use empty string inputs", "", "", ""},
		{"give length of substring less than main string", "ABCD", "ADOBECODEBANC", ""},
	}

	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			got := minWindow(tc.mainString, tc.substring)

			if got != tc.want {
				t.Errorf("minWindow(%q, %q) got %q; want %q.", tc.mainString, tc.substring, got, tc.want)
			}
		})
	}
}
