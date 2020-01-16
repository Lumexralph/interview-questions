package compress

import "testing"

func TestString(t *testing.T) {
	cases := []struct {
		description, input, want string
	}{
		{"String input is compressed", "aaabbbcccdddAA", "a3b3c3d3A2"},
		{"Input and compressed string with same length", "aabbccdd", "aabbccdd"},
	}

	for _, tc := range cases {
		t.Run(tc.description, func(t *testing.T) {
			got := String(tc.input)

			if tc.want != got {
				t.Errorf("String(%q) got=%q; want=%q", tc.input, got, tc.want)
			}
		})
	}
}
