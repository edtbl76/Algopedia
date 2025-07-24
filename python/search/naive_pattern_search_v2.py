"""
Case-Sensitive Pattern Search Implementations
============================================

This module extends naive_pattern_search.py by adding case sensitivity support to all search algorithms.

Key Enhancements:
----------------
1. Case sensitivity control via optional parameter
2. Helper function for character comparison
3. Detailed implementation notes comparing algorithm approaches
4. Improved bounds checking and early termination optimizations

Implementation Notes:
-------------------
Each algorithm represents a different approach to pattern searching with its own strengths:
- character: Uses optimistic character-by-character comparison with early termination
- counting: Counts matching characters with a clearer decomposition of work
- safe_bounds: Uses explicit bounds checking for greater portability
- slice: Leverages Python's built-in string slicing for chunk-by-chunk comparison
- tunable: Adaptively selects optimal strategy based on pattern length

These variations highlight the nuances and tradeoffs in pattern matching algorithms.


(AI-generated doc string header. I'm not sure I like this or not. Feedback appreciated)
"""


def _chars_match(text_char: str, pattern_char: str, case_sensitive: bool = True) -> bool:
    """
    Compare two characters, respecting case sensitivity setting.

    If case_sensitive is False, characters are converted to lowercase before comparison.
    This is an implementation choice - uppercase comparison would work equally well.

    Args:
        text_char: Character from the text being searched
        pattern_char: Character from the pattern being matched
        case_sensitive: Whether to perform case-sensitive comparison

    Returns:
        True if characters match according to case sensitivity setting
    """
    if case_sensitive:
        return text_char == pattern_char
    return text_char.lower() == pattern_char.lower()


def naive_pattern_search_character(text: str, pattern: str, case_sensitive: bool = True) -> list[int]:
    """
    Find all occurrences of a pattern in text using character-by-character comparison
    with early termination.

    This algorithm compares characters one by one and stops comparing as soon as
    a mismatch is found, which can be more efficient than slice-based comparison
    when mismatches are common.

    Time Complexity: O(n*m) - where n is text length and m is pattern length.
                    Best case is O(n) when characters usually mismatch early.
    Space Complexity: O(k) - where k is the number of matches found.

    Args:
        text: The text to search in
        pattern: The pattern to search for
        case_sensitive: Whether the search should be case sensitive (default: True)

    Returns:
        A list of indices where the pattern was found
    """
    # Handle edge cases
    if not pattern:
        return []
    if not text or len(pattern) > len(text):
        return []

    # Variable setup (after short circuit to avoid unnecessary memory allocation)
    # max_search_position provides bounds checking by finding the last valid starting position
    # where the pattern could potentially match, preventing unnecessary comparison attempts
    matches = []
    text_length = len(text)
    pattern_length = len(pattern)
    max_search_position = text_length - pattern_length + 1

    # Main search loop - optimistically assume matches and disprove via mismatch
    for start_position in range(max_search_position):
        match_found = True
        for offset in range(pattern_length):
            if not _chars_match(
                    text[start_position + offset],
                    pattern[offset],
                    case_sensitive
            ):
                # Early termination on first mismatch for efficiency
                match_found = False
                break

        # Record match position if all characters matched
        if match_found:
            matches.append(start_position)

    return matches


def naive_pattern_search_counting(text: str, pattern: str, case_sensitive: bool = True) -> list[int]:
    """
    Find all occurrences of a pattern in text by counting matching characters.

    This algorithm counts the number of matching characters at each position
    and considers it a match when all characters match. This approach breaks
    on the first mismatch found.

    Key Difference From Character Approach:
    While both use character comparison, the character method uses a boolean flag,
    whereas this counting approach provides a clearer decomposition of the matching work
    by explicitly tracking the match length.

    Time Complexity: O(n*m) - where n is text length and m is pattern length.
                    Best case is O(n) when mismatches are found early.
    Space Complexity: O(k) - where k is the number of matches found.

    Args:
        text: The text to search in
        pattern: The pattern to search for
        case_sensitive: Whether the search should be case sensitive (default: True)

    Returns:
        A list of indices where the pattern was found
    """
    # Handle edge cases
    if not pattern:
        return []
    if not text or len(pattern) > len(text):
        return []

    # Variable setup (after short circuit to avoid unnecessary memory allocation)
    matches = []
    text_length = len(text)
    pattern_length = len(pattern)
    max_search_position = text_length - pattern_length + 1

    # Main search loop with counting approach
    # This differs from the previous algorithm by counting matches rather than using a boolean flag
    for text_index in range(max_search_position):
        match_count = 0

        for pattern_index in range(pattern_length):
            if _chars_match(
                text[text_index + pattern_index],
                pattern[pattern_index],
                case_sensitive=case_sensitive,
            ):
                match_count += 1
            else:
                # Early termination on first mismatch for efficiency
                break

        # Length comparison to determine full match
        if match_count == pattern_length:
            matches.append(text_index)

    return matches



def naive_pattern_search_safe_bounds(text: str, pattern: str, case_sensitive: bool = True) -> list[int]:
    """
    Find all occurrences of a pattern in text with explicit bounds checking.

    This version is similar to the character-by-character approach but adds
    explicit bounds checking to handle edge cases safely.

    Implementation Note:
    The short-circuit approach (using max_search_position) is generally preferred over
    explicit bounds checking as it:
    1. Avoids unnecessary iterations
    2. Is more "Pythonic"
    3. Prevents even considering positions where a match isn't possible

    However, explicit bounds checking is more portable across languages and may be
    more readable to programmers unfamiliar with Python idioms.

    Time Complexity: O(n*m) - where n is text length and m is pattern length.
    Space Complexity: O(k) - where k is the number of matches found.

    Args:
        text: The text to search in
        pattern: The pattern to search for
        case_sensitive: Whether the search should be case sensitive (default: True)

    Returns:
        A list of indices where the pattern was found
    """
    # Handle edge cases
    if not pattern:
        return []
    if not text or len(pattern) > len(text):
        return []

    # Variable setup (after short circuit to avoid unnecessary memory allocation)
    matches = []
    text_length = len(text)
    pattern_length = len(pattern)

    # Main search loop with explicit bounds checking
    for text_index in range(text_length):
        # Explicit bounds checking rather than precalculating max search position
        if text_index + pattern_length > text_length:
            break

        # Character-by-character comparison
        pattern_index = 0
        while pattern_index < pattern_length:
            if _chars_match(
                    text[text_index + pattern_index],
                    pattern[pattern_index],
                    case_sensitive):
                pattern_index += 1
            else:
                break

        # Check for complete pattern match
        if pattern_index == pattern_length:
            matches.append(text_index)

    return matches



def naive_pattern_search_slice(text: str, pattern: str, case_sensitive: bool = True) -> list[int]:
    """
    Find all occurrences of a pattern in text using string slicing.

    This approach leverages Python's built-in string slicing for more idiomatic
    and potentially more efficient "chunk-by-chunk" comparison rather than
    character-by-character comparison.

    Implementation Details:
    - Uses Python's native string slicing capabilities which are implemented in C
    - Performs a direct substring comparison at each potential starting position
    - Pre-calculates maximum search bounds to avoid unnecessary comparisons
    - Handles case sensitivity by conditionally converting both text and pattern
    - Employs a list comprehension for concise, optimized pattern matching

    Performance Characteristics:
    This is a more Pythonic implementation that can be more efficient when:
    1. The pattern/text is structured or contains repetitive subpatterns
    2. There are fewer expected mismatches in typical inputs
    3. Native string operations are optimized at the C level in the Python interpreter
    4. The pattern is relatively short (slice operation overhead is minimal)
    5. Memory locality is important (slice operations have good cache behavior)


    Time Complexity: O(n*m) - where n is text length and m is pattern length.
                    In worst case, we need to check each character of the pattern
                    at each position of the text.
    Space Complexity: O(k) - where k is the number of matches found.

    Args:
        text: The text to search in
        pattern: The pattern to search for
        case_sensitive: Whether the search should be case sensitive (default: True)

    Returns:
        A list of indices where the pattern was found
    """
    # Handle edge cases
    if not pattern:
        return []
    if not text or len(pattern) > len(text):
        return []

    # Calculate bounds
    pattern_length = len(pattern)
    max_search_position = len(text) - pattern_length + 1

    # Handle case sensitivity with more idiomatic Python approach
    search_text = text if case_sensitive else text.lower()
    search_pattern = pattern if case_sensitive else pattern.lower()

    # Use list comprehension for a more concise, Pythonic implementation
    # This performs chunk-by-chunk comparison via string slicing
    #
    # The expression generates indices where the pattern matches in a single pass:
    # 1. Iterates through all possible starting positions up to max_search_position
    # 2. For each position i, extracts a substring of length pattern_length
    # 3. Compares the extracted substring with the pattern in a single operation
    # 4. Returns the index i only when the substring matches the pattern exactly
    # 5. Handles case sensitivity through the preprocessed search_text/search_pattern
    return [i for i in range(max_search_position)
            if search_text[i:i + pattern_length] == search_pattern]


def naive_pattern_search_tunable(text: str, pattern: str, case_sensitive: bool = True, slice_threshold: int = 4) -> list[int]:
    """
    Find all occurrences of a pattern in text using an adaptive approach.

    This algorithm represents the most sophisticated implementation, combining
    the strengths of multiple approaches based on pattern characteristics.

    Key Features:
    - Adaptively selects strategy based on pattern length
    - Uses slicing for short patterns (more efficient for small patterns)
    - Uses character comparison with early termination for longer patterns
    - Implements proper bounds checking
    - Handles case sensitivity efficiently

    Time Complexity: O(n*m) - where n is text length and m is pattern length.
                    Best case approaches O(n) with early termination on mismatches.
    Space Complexity: O(k) - where k is the number of matches found.

    Args:
        text: The text to search in
        pattern: The pattern to search for
        case_sensitive: Whether the search should be case sensitive (default: True)
        slice_threshold: The threshold for using slice vs. character comparison (default: 4)

    Returns:
        A list of indices where the pattern was found
    """
    # Handle edge cases
    if not pattern:
        return []
    if not text or len(pattern) > len(text):
        return []

    # Variable setup (after short circuit to avoid unnecessary memory allocation)
    matches = []
    text_length = len(text)
    pattern_length = len(pattern)

    # If case-insensitive, convert both text and pattern to lowercase
    if not case_sensitive:
        search_text = text.lower()
        search_pattern = pattern.lower()
    else:
        search_text = text
        search_pattern = pattern

    # Threshold for using slice vs. character comparison (can be tuned)
    SLICE_THRESHOLD = slice_threshold

    # Adaptive strategy selection based on pattern length
    if pattern_length <= SLICE_THRESHOLD:
        # For short patterns, use efficient string slicing
        for i in range(text_length - pattern_length + 1):
            if search_text[i:i + pattern_length] == search_pattern:
                matches.append(i)
    else:
        # For longer patterns, character comparison with early termination
        for i in range(text_length - pattern_length + 1):
            is_match = True
            for j in range(pattern_length):
                if search_text[i + j] != search_pattern[j]:
                    is_match = False
                    break
            if is_match:
                matches.append(i)

    return matches






