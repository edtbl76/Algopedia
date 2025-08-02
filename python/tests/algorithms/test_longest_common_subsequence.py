import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from algorithms.longest_common_subsequence import (
    lcs_return_length,
    lcs_return_subsequence,
    tabulate_grid
)


class TestLongestCommonSubsequence(unittest.TestCase):

    def test_lcs_return_length_regular_cases(self):
        """Test lcs_return_length with regular cases"""
        # Examples from the docstring
        self.assertEqual(lcs_return_length("ABCDGH", "AEDFHR"), 3)
        self.assertEqual(lcs_return_length("AGGTAB", "GXTXAYB"), 4)
        self.assertEqual(lcs_return_length("ABCDEF", "ACEF"), 4)

        # Additional test cases
        self.assertEqual(lcs_return_length("ABCBDAB", "BDCABA"), 4)  # LCS: "BCBA"
        self.assertEqual(lcs_return_length("XMJYAUZ", "MZJAWXU"), 4)  # LCS: "MJAU"
        self.assertEqual(lcs_return_length("programming", "algorithm"), 3)  # LCS: "orm"

    def test_lcs_return_length_edge_cases(self):
        """Test lcs_return_length with edge cases"""
        # Empty strings
        self.assertEqual(lcs_return_length("", ""), 0)
        self.assertEqual(lcs_return_length("", "ABC"), 0)
        self.assertEqual(lcs_return_length("ABC", ""), 0)

        # Single character strings
        self.assertEqual(lcs_return_length("A", "A"), 1)
        self.assertEqual(lcs_return_length("A", "B"), 0)

        # Identical strings
        self.assertEqual(lcs_return_length("ABCDEF", "ABCDEF"), 6)

        # No common subsequence
        self.assertEqual(lcs_return_length("ABC", "DEF"), 0)

    def test_lcs_return_subsequence_regular_cases(self):
        """Test lcs_return_subsequence with regular cases"""
        # Examples from the docstring
        self.assertEqual(lcs_return_subsequence("ABCDGH", "AEDFHR"), "ADH")
        self.assertEqual(lcs_return_subsequence("AGGTAB", "GXTXAYB"), "GTAB")
        self.assertEqual(lcs_return_subsequence("ABCDEF", "ACEF"), "ACEF")

        # Additional test cases
        self.assertEqual(lcs_return_subsequence("ABCBDAB", "BDCABA"), "BCBA")
        self.assertEqual(lcs_return_subsequence("XMJYAUZ", "MZJAWXU"), "MJAU")
        self.assertEqual(lcs_return_subsequence("programming", "algorithm"), "orm")

    def test_lcs_return_subsequence_edge_cases(self):
        """Test lcs_return_subsequence with edge cases"""
        # Empty strings
        self.assertEqual(lcs_return_subsequence("", ""), "")
        self.assertEqual(lcs_return_subsequence("", "ABC"), "")
        self.assertEqual(lcs_return_subsequence("ABC", ""), "")

        # Single character strings
        self.assertEqual(lcs_return_subsequence("A", "A"), "A")
        self.assertEqual(lcs_return_subsequence("A", "B"), "")

        # Identical strings
        self.assertEqual(lcs_return_subsequence("ABCDEF", "ABCDEF"), "ABCDEF")

        # No common subsequence
        self.assertEqual(lcs_return_subsequence("ABC", "DEF"), "")

    def test_tabulate_grid_regular_cases(self):
        """Test tabulate_grid with regular cases"""
        # Test with a simple example
        grid = tabulate_grid("AC", "BC")
        # Expected grid:
        #    ""  A   C
        # "" 0   0   0
        # B  0   0   0
        # C  0   0   1
        expected_grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]
        self.assertEqual(grid, expected_grid)

        # Test with another example
        grid = tabulate_grid("AB", "AB")
        # Expected grid:
        #    ""  A   B
        # "" 0   0   0
        # A  0   1   1
        # B  0   1   2
        expected_grid = [
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 2]
        ]
        self.assertEqual(grid, expected_grid)

    def test_tabulate_grid_edge_cases(self):
        """Test tabulate_grid with edge cases"""
        # Empty strings
        grid = tabulate_grid("", "")
        expected_grid = [[0]]
        self.assertEqual(grid, expected_grid)

        # One empty string
        grid = tabulate_grid("", "A")
        expected_grid = [[0], [0]]
        self.assertEqual(grid, expected_grid)

        grid = tabulate_grid("A", "")
        expected_grid = [[0, 0]]
        self.assertEqual(grid, expected_grid)

        # Single character strings
        grid = tabulate_grid("A", "A")
        expected_grid = [
            [0, 0],
            [0, 1]
        ]
        self.assertEqual(grid, expected_grid)

        grid = tabulate_grid("A", "B")
        expected_grid = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(grid, expected_grid)

    def test_length_matches_subsequence(self):
        """Test that the length returned by lcs_return_length matches the length of the subsequence"""
        test_cases = [
            ("ABCDGH", "AEDFHR"),
            ("AGGTAB", "GXTXAYB"),
            ("ABCDEF", "ACEF"),
            ("", ""),
            ("", "ABC"),
            ("ABC", ""),
            ("A", "A"),
            ("A", "B"),
            ("ABCDEF", "ABCDEF"),
            ("ABC", "DEF"),
            ("ABCBDAB", "BDCABA"),
            ("XMJYAUZ", "MZJAWXU"),
            ("programming", "algorithm")
        ]

        for string1, string2 in test_cases:
            length = lcs_return_length(string1, string2)
            subsequence = lcs_return_subsequence(string1, string2)
            self.assertEqual(length, len(subsequence), 
                            f"Length mismatch for '{string1}' and '{string2}': {length} != {len(subsequence)}")


if __name__ == '__main__':
    unittest.main()
