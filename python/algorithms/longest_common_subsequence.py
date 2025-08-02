# TAGS: Dynamic Programming, Backtracking, Tabulation
"""
=== Longest Common Subsequence (LCS) Implementation ===

The Longest Common Subsequence problem is a classic dynamic programming problem that finds
the longest sequence of characters that appear in the same relative order in two strings,
but not necessarily adjacent.

Problem Definition:
Given two strings, find the length of their longest common subsequence. A subsequence is
a sequence that can be derived from another sequence by deleting some or no elements
without changing the order of the remaining elements.

Key Properties:
- Characters in the subsequence maintain their relative order from both original strings
- Characters do not need to be contiguous/adjacent in either string
- The empty string is a valid subsequence of any string
- If one string is empty, the LCS length is 0

Examples:
- LCS("ABCDEF", "ACEF") = "ACEF" (length 4)
- LCS("AGGTAB", "GXTXAYB") = "GTAB" (length 4)
- LCS("ABCDGH", "AEDFHR") = "ADH" (length 3)
- LCS("ABC", "DEF") = "" (length 0)

Algorithm Approach:
This implementation uses dynamic programming with a bottom-up tabulation approach:
1. Create a 2D grid where grid[i][j] represents the LCS length between the first i 
   characters of string2 and the first j characters of string1
2. Fill the grid using the recurrence relation:
   - If characters match: grid[i][j] = grid[i-1][j-1] + 1
   - If characters don't match: grid[i][j] = max(grid[i-1][j], grid[i][j-1])
3. The bottom-right cell contains the final LCS length

Complexity:
- Time Complexity: O(m × n) where m and n are the lengths of the input strings
- Space Complexity: O(m × n) for the dynamic programming grid

Applications:
- Bioinformatics (DNA sequence alignment)
- Version control systems (diff algorithms)
- Text comparison and similarity analysis
- Data compression algorithms
"""



def lcs_return_length(string1: str, string2: str) -> int:
    """
    Calculate the length of the Longest Common Subsequence (LCS) between two strings.
    
    This function computes the LCS length using dynamic programming by building a 2D grid
    where each cell represents the optimal solution for substrings, then returns the value
    from the bottom-right cell which contains the complete LCS length.
    
    Args:
        string1 (str): First input string to compare
        string2 (str): Second input string to compare
        
    Returns:
        int: The length of the longest common subsequence between the two strings
        
    Example:
        >>> lcs_return_length("ABCDGH", "AEDFHR")
        3
        >>> lcs_return_length("AGGTAB", "GXTXAYB")
        4
        >>> lcs_return_length("", "ABC")
        0
        
    Time Complexity: O(m * n) where m and n are the lengths of string1 and string2
    Space Complexity: O(m * n) for the dynamic programming grid storage
    
    Note:
        This function delegates the grid construction to build_lcs_grid() and extracts
        the final result from the bottom-right cell of the completed DP table.
    """
    return tabulate_grid(string1, string2)[-1][-1]


def lcs_return_subsequence(string1: str, string2: str) -> str:
    """
    Reconstruct the actual Longest Common Subsequence (LCS) string between two input strings.
    
    This function first builds the dynamic programming grid using our helper function, then
    performs backtracking through the grid to reconstruct the actual LCS characters.
    The backtracking process traces the optimal path that led to the maximum LCS length.
    
    Args:
        string1 (str): First input string to compare
        string2 (str): Second input string to compare
        
    Returns:
        str: The actual longest common subsequence as a string. Returns empty string
             if no common subsequence exists.
             
    Example:
        >>> lcs_return_subsequence("ABCDGH", "AEDFHR")
        "ADH"
        >>> lcs_return_subsequence("AGGTAB", "GXTXAYB")
        "GTAB"
        >>> lcs_return_subsequence("ABC", "DEF")
        ""
        
    Time Complexity: O(m * n) where m and n are the lengths of string1 and string2
        - Grid construction: O(m * n)
        - Backtracking: O(m + n) in worst case (traversing from bottom-right to top-left)
        - Overall: O(m * n) since grid construction dominates
        
    Space Complexity: O(m * n) for the dynamic programming grid storage
        - Grid space: O(m * n)
        - Subsequence list: O(min(m, n)) in worst case (LCS can't be longer than shorter string)
        - Overall: O(m * n) since grid storage dominates
        
    Backtracking Algorithm:
        The backtracking process reconstructs the LCS by tracing through the DP grid:
        
        1. Start at bottom-right cell grid[m][n] (contains final LCS length)
        2. At each cell grid[i][j], check three conditions:
           
           a) If string1[j-1] == string2[i-1]: 
              - Characters match, so this character is part of the LCS
              - Add character to subsequence and move diagonally (i-1, j-1)
              
           b) If grid[i-1][j] > grid[i][j-1]:
              - LCS came from excluding current char from string2
              - Move up (i-1, j) without adding any character
              
           c) Otherwise:
              - LCS came from excluding current char from string1  
              - Move left (i, j-1) without adding any character
              
        3. Continue until reaching a boundary (i=0 or j=0)
        4. Reverse the collected characters (since we built backwards)
        
        Why Backtracking Works:
        - Each cell contains the optimal LCS length for its corresponding substrings
        - By following the path that led to each optimal value, we reconstruct the
          actual characters that formed the LCS
        - Moving diagonally means both characters matched (part of LCS)
        - Moving up/left means one character was skipped (not part of LCS)
    
    Note:
        This function depends on build_lcs_grid() to provide the properly constructed
        DP grid. The backtracking assumes the grid follows the standard LCS DP convention
        where grid[i][j] represents LCS length between string2[:i] and string1[:j].
    """
    # Build the dynamic programming grid containing LCS lengths for all subproblems
    grid = tabulate_grid(string1, string2)

    # Initialize backtracking from the bottom-right corner of the grid
    # This cell contains the length of the complete LCS between both full strings
    subsequence = []                # List to collect LCS characters (built in reverse order)
    row = len(grid) - 1            # Start at last row (corresponds to full string2)
    col = len(grid[0]) - 1         # Start at last column (corresponds to full string1)

    # Backtrack through the grid to reconstruct the actual LCS characters
    # Continue until we reach a boundary (empty string comparison)
    while row > 0 and col > 0:
        # Get the current characters being compared at this grid position
        # Subtract 1 because grid indices are offset by 1 from string indices
        char1 = string1[col - 1]   # Character from string1 at current column position
        char2 = string2[row - 1]   # Character from string2 at current row position
        
        # Case 1: Characters match - this character is part of the LCS
        if char1 == char2:
            subsequence.append(char1)  # Add matching character to our LCS
            row -= 1                   # Move diagonally up-left in the grid
            col -= 1                   # (both strings contributed to this LCS character)
            
        # Case 2: Characters don't match - determine which direction the optimal value came from
        elif grid[row - 1][col] > grid[row][col - 1]:
            # The optimal LCS value came from the cell above (excluding current char from string2)
            row -= 1                   # Move up (skip current character in string2)
            
        else:
            # The optimal LCS value came from the cell to the left (excluding current char from string1)
            # This also handles the case where grid[row - 1][col] == grid[row][col - 1]
            col -= 1                   # Move left (skip current character in string1)

    # Reverse the subsequence since we built it backwards during backtracking
    # (We started from the end result and worked backwards to the beginning)
    subsequence.reverse()
    
    # Convert list of characters back to a single string and return
    return "".join(subsequence)


def tabulate_grid(string1: str, string2: str) -> list[list[int]]:
    """
    Build a dynamic programming grid for computing the Longest Common Subsequence (LCS).
    
    This is a helper function that creates a 2D grid where each cell [i][j] represents the length of the LCS
    between the first i characters of string2 and the first j characters of string1.
    
    Grid Structure:
    - Columns represent characters from string1 (plus one extra column for empty string)
    - Rows represent characters from string2 (plus one extra row for empty string)
    - grid[0][j] and grid[i][0] are initialized to 0 (base cases for empty strings)
    
    Example:
        For string1 = "AC" and string2 = "BC", the resulting grid would be:
        
        Grid layout:
                   ""  A   C
               ""   0   0   0
               B    0   0   0
               C    0   0   1
        
        Step-by-step construction:
        - Row 0, Col 0-2: Base case (empty string), all 0s
        - Col 0, Row 0-2: Base case (empty string), all 0s  
        - Row 1, Col 1: B ≠ A, max(0,0) = 0
        - Row 1, Col 2: B ≠ C, max(0,0) = 0
        - Row 2, Col 1: C ≠ A, max(0,0) = 0
        - Row 2, Col 2: C = C, diagonal + 1 = 0 + 1 = 1
        
        The LCS length is 1 (bottom-right cell), and the LCS is "C".
    
    Args:
        string1 (str): First input string to compare
        string2 (str): Second input string to compare
        
    Returns:
        list[list[int]]: 2D grid where grid[i][j] contains the length of LCS between
                        string2[:i] and string1[:j]. The bottom-right cell contains
                        the length of the complete LCS.
                        
    Variables Explained:
        GRID_OFFSET: Constant (1) representing the extra row/column for empty string base case
        grid_width: Total columns in grid (len(string1) + 1)
        grid_height: Total rows in grid (len(string2) + 1)
        row: Current row index in grid (corresponds to string2 character at index row-1)
        col: Current column index in grid (corresponds to string1 character at index col-1)
        char1: Character from string1 at position (col - GRID_OFFSET)
        char2: Character from string2 at position (row - GRID_OFFSET)
    
    Algorithm:
        For each cell, if characters match: take diagonal value + 1
        If characters don't match: take maximum of left or top cell

    Complexity Analysis:
    - Each cell in the (m+1) × (n+1) grid is computed exactly once
    - Each cell computation involves O(1) operations (character comparison, max function)
    - Total operations: O((m+1) × (n+1)) = O(m × n)
    - Space is dominated by the grid storage: O(m × n)
    """
    # Grid offset: extra row and column for empty string base case
    GRID_OFFSET = 1

    # Calculate grid dimensions (original string lengths + offset for empty string)
    grid_width = len(string1) + GRID_OFFSET     # Columns --> string1 chars
    grid_height = len(string2) + GRID_OFFSET    # Rows    --> string2 chars

    # Initialize grid with zeros - base cases are already handled (empty string comparisons = 0)
    grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]

    # Fill the grid using dynamic programming approach
    # Start from (1,1) since (0,x) and (x,0) represent base cases (empty strings)
    for row in range(GRID_OFFSET, grid_height):
        for col in range(GRID_OFFSET, grid_width):

            # Extract current characters being compared (more concise / simple logic later)
            # Subtract GRID_OFFSET because grid indices are offset by 1 from string indices
            char1 = string1[col - GRID_OFFSET]  # Character from string1
            char2 = string2[row - GRID_OFFSET]  # Character from string2

            # Matching / Comparison Logic
            if char1 == char2:
                # Characters match: LCS length increases by 1 from the diagonal predecessor
                # This represents extending the LCS found in both substrings (excluding current chars)
                grid[row][col] = grid[row - GRID_OFFSET][col - GRID_OFFSET] + GRID_OFFSET
            else:
                # Characters don't match: take the maximum LCS length from either:
                # - Excluding current character from string2 (cell above)
                # - Excluding current character from string1 (cell to the left)
                grid[row][col] = max(grid[row - GRID_OFFSET][col], grid[row][col - GRID_OFFSET])

    return grid