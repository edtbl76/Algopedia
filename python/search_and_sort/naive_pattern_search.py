"""
There are a lot of different ways to search for a pattern in a text.

What are the things we need to consider when designing a pattern search algorithm?
- What is the length of the pattern?
- What is the length of the text?
- What is the expected runtime complexity?
- What is the expected space complexity?
- What are the best and worst-case scenarios?
- What are the edge cases?
- How do we handle edge cases?
- How do we handle multiple matches?
"""
from _ast import pattern


def naive_pattern_search_character(text: str, pattern: str, replacement: str = None) -> list[int] | str:
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

    Returns:
        A list of indices where the pattern was found
    """
    if not pattern:
        return []

    matches = []
    text_length = len(text)
    pattern_length = len(pattern)
    max_start_pos = text_length - pattern_length + 1

    for text_index in range(max_start_pos):
        pattern_index = 0
        # Compare characters one by one until mismatch or end of pattern
        while (pattern_index < pattern_length and
               text_index + pattern_index < text_length and
               text[text_index + pattern_index] == pattern[pattern_index]):
            pattern_index += 1
        # If we've matched the entire pattern
        if pattern_index == pattern_length:
            matches.append(text_index)

    return matches


def naive_pattern_search_counting(text: str, pattern: str, replacement: str = None) -> list[int] | str:
    """
    Find all occurrences of a pattern in text by counting matching characters.

    This algorithm counts the number of matching characters at each position
    and considers it a match when all characters match. This approach always
    checks every character in the pattern, even after a mismatch is found.

    Time Complexity: O(n*m) - where n is text length and m is pattern length.
                    Always checks all characters in pattern at each position.
    Space Complexity: O(k) - where k is the number of matches found.

    Args:
        text: The text to search in
        pattern: The pattern to search for

    Returns:
        A list of indices where the pattern was found
    """
    if not pattern:
        return []

    matches = []
    text_length = len(text)
    pattern_length = len(pattern)
    max_start_pos = text_length - pattern_length + 1

    for text_index in range(max_start_pos):
        match_count = 0

        # This is more or less the same functionality of a character by character search that is short circuited
        # based on mismatch.
        for pattern_index in range(pattern_length):
            if text_index + pattern_index < text_length and text[text_index + pattern_index] == pattern[pattern_index]:
                match_count += 1
            else:
                break  # Performance optimization: stop counting on first mismatch

        # This loop isolates the bounds check for pattern length.
        # I personally like this isolation because it separates and ID's the composite nature of the algorithm
        # because it supports "single responsibility".
        if match_count == pattern_length:
            matches.append(text_index)

    return matches


def naive_pattern_search_safe_bounds(text: str, pattern: str, replacement: str = None) -> list[int] | str:
    """
    Find all occurrences of a pattern in text with explicit bounds checking.

    This version is similar to the character-by-character approach but adds
    explicit bounds checking to handle edge cases safely.

    Time Complexity: O(n*m) - where n is text length and m is pattern length.
    Space Complexity: O(k) - where k is the number of matches found.

    Args:
        text: The text to search in
        pattern: The pattern to search for

    Returns:
        A list of indices where the pattern was found
    """
    if not pattern:
        return []

    matches = []
    text_length = len(text)
    pattern_length = len(pattern)

    # This is approach to bounds checking is more portable, as we are avoiding the use of
    # Pythonic slicing.
    for text_index in range(text_length):
        # Skip if remaining text is shorter than pattern
        if text_index + pattern_length > text_length:
            break

        # We've established this code block as the
        # "matcher" function of the pattern matcher.
        pattern_index = 0
        while (pattern_index < pattern_length and
               text[text_index + pattern_index] == pattern[pattern_index]):
            pattern_index += 1

        # We've established this code block as the bounds (length) check for the algorithm
        if pattern_index == pattern_length:
            matches.append(text_index)

    if replacement is None:
        return matches

    # Perform replacements from end to start to avoid index shifting
    result = list(text)
    for idx in reversed(matches):
        result[idx:idx + len(pattern)] = replacement

    return ''.join(result)


def naive_pattern_search_slice(text: str, pattern: str, replacement: str = None) -> list[int] | str:
    """
    Find all occurrences of a pattern in text using string slicing. This is slightly faster than character-by-character
    comparison.

    Chunk-by-chunk comparison is more efficient than character-by-character comparison in most cases. I perceive this as
    a change in the ordering of the algorithm. By preceding the length of the pattern with the starting position of the
    pattern, we can skip over the characters that are not part of the pattern. This is especially useful when the pattern is
    a substring of the text.

    This algorithm uses Python's built-in string slicing to check for pattern matches
    at each possible starting position in the text.

    Time Complexity: O(n*m) - where n is text length and m is pattern length.
                    In worst case, we need to check each character of the pattern
                    at each position of the text.
    Space Complexity: O(k) - where k is the number of matches found.

    Args:
        text: The text to search in
        pattern: The pattern to search for

    Returns:
        A list of indices where the pattern was found
    """
    if not pattern:
        return []

    matches = []

    # short circuit our max search position based on the length of the pattern.
    # (i.e. if the pattern is 10 characters long, we can stop searching once we
    # don't need to continue to search past the 10th character from the end of the
    # text)
    max_start_pos = len(text) - len(pattern) + 1


    for i in range(max_start_pos):
        # the slicing approach is Pythonic, allowing us to match the entire substring from each
        # "start position".
        #
        # This allows chunk comparison rather than character comparison.
        if text[i:i + len(pattern)] == pattern:
            matches.append(i)

    # This supports multiple matches, rather than looking only for the first match.
    return matches




def naive_pattern_search_tunable(text: str, pattern: str, replacement: str = None, slice_threshold: int = 4) -> list[
                                                                                                                    int] | str:
    """
    Find all occurrences of a pattern in text using an optimized approach.

    This algorithm combines the best aspects of the above approaches:
    - Uses slicing for short patterns (more Pythonic and often faster for small patterns)
    - Uses character-by-character comparison with early termination for longer patterns
    - Implements proper bounds checking
    - Uses pattern length caching for performance

    Time Complexity: O(n*m) - where n is text length and m is pattern length.
                    Best case approaches O(n) with early termination on mismatches.
    Space Complexity: O(k) - where k is the number of matches found.

    Args:
        text: The text to search in
        pattern: The pattern to search for
        slice_threshold: The threshold for using slice vs. character comparison (default: 4)
    Returns:
        A list of indices where the pattern was found

    """
    if not pattern:
        return []

    matches = []
    text_length = len(text)
    pattern_length = len(pattern)

    # Edge case: pattern longer than text
    if pattern_length > text_length:
        return []

    # Threshold for using slice vs. character comparison (can be tuned)
    SLICE_THRESHOLD = slice_threshold

    # For very short patterns, slicing may be more efficient
    if pattern_length <= SLICE_THRESHOLD:
        for i in range(text_length - pattern_length + 1):
            if text[i:i + pattern_length] == pattern:
                matches.append(i)
    else:
        # For longer patterns, character comparison with early termination
        for i in range(text_length - pattern_length + 1):
            is_match = True
            for j in range(pattern_length):
                if text[i + j] != pattern[j]:
                    is_match = False
                    break
            if is_match:
                matches.append(i)

    return matches


