package unique

import (
	"testing"
)

func TestIsUnique(t *testing.T) {
	cases := []struct {
		name, words string
		want        bool
	}{
		{"with unique characters", "abcdefghikjlmnopqrstu", true},
		{"with repeated characters", "AAaaBBbbCCcc", false},
	}

	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			if got := isUnique(tc.words); got != tc.want {
				t.Errorf("isUnique(%q) got %v; want %v", tc.words, tc.want, got)
			}
		})
	}
}
