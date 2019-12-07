from unittest import TestCase
from .solution import min_window


class TestMinWindow(TestCase):
    def test_repeated_character(self):
        S = "ADOBECODEBANC"
        T = "OBOC"
        self.assertEqual(min_window(S, T), "OBECO")

    def test_unique_character(self):
        S = "ADOBECODEBANC"
        T = "ABC"
        self.assertEqual(min_window(S, T), "BANC")

    def test_empty_string(self):
        S = ""
        T = "ABC"
        self.assertEqual(min_window(S, T), "")

    def test_empty_string_in_both_inputs(self):
        S = ""
        T = ""
        self.assertEqual(min_window(S, T), "")

    def test_list_inputs(self):
        S = []
        T = ["A"]
        self.assertEqual(min_window(S, T), "")

    def test_dictionary_inputs(self):
        S = {}
        T = {"A"}
        self.assertEqual(min_window(S, T), "")
