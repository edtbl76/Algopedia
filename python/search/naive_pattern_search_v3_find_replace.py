
def _chars_match(text_char: str, pattern_char: str, case_sensitive: bool = True) -> bool:
    """
    Compare two single characters, respecting case sensitivity setting.
    If case_sensitive is False, characters are converted to lowercase before comparison.
    Args:
        text_char: Single character from the text being searched
        pattern_char: Single character from the pattern being matched
        case_sensitive: Whether to perform case-sensitive comparison (default: True)
    Returns:
        True if characters match according to case sensitivity setting
    Raises:
        TypeError: If inputs are not strings
        ValueError: If inputs are not single characters
    """
    # Type checking for more robust behavior
    if not isinstance(text_char, str) or not isinstance(pattern_char, str):
        raise TypeError("Both arguments must be strings")

    # Length validation to ensure single characters
    if len(text_char) != 1 or len(pattern_char) != 1:
        raise ValueError("Both arguments must be single characters")


    # Simple case - case-sensitive matching
    if case_sensitive:
        return text_char == pattern_char

    # Case-insensitive matching
    return text_char.lower() == pattern_char.lower()


def _handle_edge_cases(text: str, pattern: str) -> tuple[bool, str]:
    """
    Handle common edge cases for find-replace operations.

    Returns:
        (should_return_early, return_value): If should_return_early is True,
        the calling function should return return_value immediately.
    """
    if not pattern or len(pattern) > len(text):
        return True, text
    if not text:
        return True, ""
    return False, ""


def _handle_single_char_replacement(text: str, pattern: str, replacement: str, case_sensitive: bool) -> tuple[
    bool, str]:
    """
    Handle optimized single character replacement using built-in methods.

    Returns:
        (should_return_early, return_value): If should_return_early is True,
        the calling function should return return_value immediately.
    """
    if len(pattern) == 1:
        if case_sensitive:
            return True, text.replace(pattern, replacement)
        else:
            result_parts = []
            for char in text:
                if char.lower() == pattern.lower():
                    result_parts.append(replacement)
                else:
                    result_parts.append(char)
            return True, ''.join(result_parts)
    return False, ""


def _setup_replacement_variables(text: str, pattern: str, case_sensitive: bool) -> tuple[str, str, int, int, int]:
    """
    Set up common variables needed for pattern replacement.

    Returns:
        (search_text, search_pattern, text_length, pattern_length, max_search_position)
    """
    text_length = len(text)
    pattern_length = len(pattern)
    max_search_position = text_length - pattern_length + 1

    if case_sensitive:
        search_text = text
        search_pattern = pattern
    else:
        search_text = text.lower()
        search_pattern = pattern.lower()

    return search_text, search_pattern, text_length, pattern_length, max_search_position

def _add_remaining_characters(result_parts: list[str], text: str, position: int, text_length: int) -> None:
    """Add any remaining characters from the original text to result_parts."""
    if position < text_length:
        result_parts.append(text[position:])


def naive_find_replace_character(text: str, pattern: str, replacement: str, case_sensitive: bool = True) -> str:
    """
    Find and replace all occurrences of a pattern in text using character-by-character comparison.

    This algorithm searches through the text character by character, comparing each position
    with the pattern and replacing matches with the replacement string. It uses early termination
    on the first character mismatch for efficiency.

    Key Implementation Features:
    - Character-by-character comparison with early termination on mismatches
    - Optimized string building using list accumulation instead of concatenation
    - Pre-calculated bounds checking to avoid unnecessary iterations
    - Case sensitivity support via helper function
    - Explicit position tracking for clear control flow

    Performance Optimization - List vs String Concatenation:
    This implementation uses a list to accumulate result parts instead of string concatenation.
    String concatenation in Python creates new string objects each time (strings are immutable),
    resulting in O(n²) complexity for building the result. Using a list and joining once at
    the end achieves O(n) complexity:
    - String concatenation: result += char creates new string each time
    - List approach: result_parts.append(char) + ''.join(result_parts) at end
    For large texts, this can be 10-100x faster.

    Time Complexity: O(n*m + r) - where n is text length, m is pattern length, and r is result length.
                    Pattern matching: O(n*m) with early termination improving average case.
                    String building: O(r) for list operations + final join.
    Space Complexity: O(r) - where r is the length of the result string.

    Args:
        text: The text to search in
        pattern: The pattern to search for
        replacement: The string to replace matching patterns with
        case_sensitive: Whether the search should be case sensitive (default: True)

    Returns:
        The text with all occurrences of pattern replaced by replacement

    Examples:
        >>> naive_find_replace_character("hello world", "world", "python")
        'hello python'
        >>> naive_find_replace_character("Hello World", "world", "Python", case_sensitive=False)
        'Hello Python'
        >>> naive_find_replace_character("ababab", "ab", "XY")
        'XYXYXY'
    """
    # Handle edge cases
    should_return, result = _handle_edge_cases(text, pattern)
    if should_return:
        return result

    # Handle single character optimization
    should_return, result = _handle_single_char_replacement(text, pattern, replacement, case_sensitive)
    if should_return:
        return result

    # Setup common variables
    search_text, search_pattern, text_length, pattern_length, max_search_position = _setup_replacement_variables(
        text, pattern, case_sensitive)


    result_parts = []
    position = 0
    # Main search and replace loop
    while position < max_search_position:
        match_found = True
        for offset in range(pattern_length):
            if not _chars_match(
                    text[position + offset],
                    pattern[offset],
                    case_sensitive
            ):
                match_found = False
                break

        if match_found:
            # Pattern found - add replacement and skip past the matched pattern
            result_parts.append(replacement)
            position += pattern_length
        else:
            # No match - copy current char and advance by one
            result_parts.append(text[position])
            position += 1

    # Handle remaining chars
    _add_remaining_characters(result_parts, text, position, text_length)

    return ''.join(result_parts)



def naive_find_replace_counting(text: str, pattern: str, replacement: str, case_sensitive: bool = True) -> str:
    """
    Replace all occurrences of pattern in text with replacement using counting approach.

    This algorithm searches through the text by counting matching characters at each position
    and replaces complete pattern matches with the replacement string. It provides a clear
    decomposition of the matching work by explicitly tracking match progress, making the
    algorithm logic more transparent than boolean flag approaches.

    Key Implementation Features:
    - Match counting approach with explicit progress tracking
    - Early termination on first character mismatch for efficiency
    - While loop control for precise index management after replacements
    - List-based string building for optimal performance
    - Case sensitivity support via helper function
    - Non-overlapping replacement strategy (skips past entire replaced patterns)

    Performance Optimization - List vs String Concatenation:
    This implementation uses a list to accumulate result parts instead of string concatenation.
    Python strings are immutable, so concatenation operations like `result += char` create
    entirely new string objects each time, leading to O(n²) time complexity for building
    the final result. The list approach achieves O(n) complexity:

    String concatenation approach (INEFFICIENT):
    - Each `result += part` creates a new string copying all previous content
    - For n operations: 1 + 2 + 3 + ... + n = O(n²) total character copies
    - Memory fragmentation from many intermediate string objects

    List accumulation approach (EFFICIENT):
    - `result_parts.append(part)` is O(1) - just adds reference to list
    - Final `''.join(result_parts)` is O(n) - single pass through all content
    - Total complexity: O(n) with much better memory locality
    - For large texts with many replacements, can be 10-100x faster

    Algorithm Distinction - Counting vs Boolean Flag:
    While functionally similar to character-by-character approaches, the counting method
    provides clearer algorithmic decomposition by explicitly tracking match progress.
    This makes debugging easier and the matching logic more transparent, though with
    minimal performance difference due to early termination on mismatches.

    Time Complexity: O(n*m + r) - where n is text length, m is pattern length, r is result length.
                    Pattern matching: O(n*m) worst case, better average case with early termination
                    String building: O(r) for list operations + final join
    Space Complexity: O(r) - where r is the length of the result string stored in the list

    Args:
        text: The text to search in and perform replacements on
        pattern: The pattern to search for and replace
        replacement: The string to replace matching patterns with
        case_sensitive: Whether the search should be case sensitive (default: True)

    Returns:
        The text with all occurrences of pattern replaced by replacement

    Examples:
        >>> naive_find_replace_counting("hello world", "world", "python")
        'hello python'
        >>> naive_find_replace_counting("Hello World", "world", "Python", case_sensitive=False)
        'Hello Python'
        >>> naive_find_replace_counting("abcabc", "abc", "XY")
        'XYXY'
        >>> naive_find_replace_counting("overlapping", "pp", "XX")
        'overlaXXing'
    """
    # Handle edge cases
    should_return, result = _handle_edge_cases(text, pattern)
    if should_return:
        return result

    # Handle single character optimization
    should_return, result = _handle_single_char_replacement(text, pattern, replacement, case_sensitive)
    if should_return:
        return result

    # Setup common variables
    search_text, search_pattern, text_length, pattern_length, max_search_position = _setup_replacement_variables(
        text, pattern, case_sensitive)

    result_parts = []

    # Main search and replace loop using while loop for precise index control
    # While loop allows us to skip ahead by pattern_length after matches,
    # avoiding overlapping replacements and improving efficiency
    position = 0
    while position < max_search_position:
        match_count = 0

        for pattern_index in range(pattern_length):
            if _chars_match(
                    text[position + pattern_index],
                    pattern[pattern_index],
                    case_sensitive=case_sensitive,
            ):
                match_count += 1
            else:
                break

        # Check if we found a complete pattern match
        if match_count == pattern_length:
            # Pattern found - add replacement and skip past the matched pattern
            result_parts.append(replacement)
            position += pattern_length
        else:
            # No match - copy current char and advance by one
            result_parts.append(text[position])
            position += 1

    # Handle remaining chars
    _add_remaining_characters(result_parts, text, position, text_length)

    return ''.join(result_parts)


def naive_find_replace_safe_bounds(text: str, pattern: str, replacement: str, case_sensitive: bool = True) -> str:
    """
    Find and replace all occurrences of a pattern in text using explicit bounds checking.

    This algorithm implements a robust find-and-replace operation that searches through text
    character by character with explicit bounds checking rather than pre-calculating the
    maximum search position. It uses proper loop control flow and handles case sensitivity
    through a helper function for character comparison.

    Algorithm Strategy:
    1. Handles edge cases first (empty inputs, pattern longer than text)
    2. Uses optimized built-in replace() for single-character patterns
    3. Employs explicit bounds checking during iteration for safety
    4. Performs character-by-character pattern matching with early termination
    5. Uses list-based string building for optimal performance (O(n) vs O(n²))
    6. Implements non-overlapping replacement strategy

    Performance Optimizations:
    - List accumulation instead of string concatenation prevents O(n²) complexity
    - Early termination on character mismatch improves average-case performance
    - Single join operation at the end is more efficient than repeated concatenation
    - Short-circuit evaluation for single characters uses built-in optimized methods

    Time Complexity: O(n*m + r) - where n is text length, m is pattern length, r is result length
                    Pattern matching: O(n*m) worst case, better average case with early termination
                    String building: O(r) for list operations + final join
    Space Complexity: O(r) - where r is the length of the result string

    Args:
        text: The input text to search within
        pattern: The pattern string to find and replace
        replacement: The string to replace each occurrence of the pattern
        case_sensitive: Whether pattern matching should be case sensitive (default: True)

    Returns:
        New string with all non-overlapping occurrences of pattern replaced by replacement

    Examples:
        >>> naive_find_replace_safe_bounds("hello world", "world", "python")
        'hello python'
        >>> naive_find_replace_safe_bounds("Hello World", "world", "Python", case_sensitive=False)
        'Hello Python'
        >>> naive_find_replace_safe_bounds("abcabc", "abc", "XY")
        'XYXY'

    Raises:
        No exceptions - handles all edge cases happily by returning appropriate values
    """
    # Handle edge cases
    should_return, result = _handle_edge_cases(text, pattern)
    if should_return:
        return result

    # Handle single character optimization
    should_return, result = _handle_single_char_replacement(text, pattern, replacement, case_sensitive)
    if should_return:
        return result

    # Setup common variables
    search_text, search_pattern, text_length, pattern_length, max_search_position = _setup_replacement_variables(
        text, pattern, case_sensitive)

    result_parts = []

    # Main search and replace loop with proper control flow
    position = 0
    while position < text_length:
        # Explicit bounds checking: ensure we have enough characters left for a complete pattern
        if position + pattern_length > text_length:
            result_parts.append(text[position:])
            # No need to call _add_remaining_characters since we've already added the remaining text
            position = text_length
            break

        # Pattern matching phase: character-by-character comparison with early termination
        pattern_index = 0
        while pattern_index < pattern_length:
            if _chars_match(
                    text[position + pattern_index],
                    pattern[pattern_index],
                    case_sensitive):
                pattern_index += 1
            else:
                break

        # Determine action based on match results
        if pattern_index == pattern_length:
            # Pattern found - add replacement and skip past the matched pattern
            result_parts.append(replacement)
            position += pattern_length
        else:
            # No match - copy current char and advance by one
            result_parts.append(text[position])
            position += 1

    # Only add remaining chars if we didn't already add them in the bounds checking block
    if position < text_length:
        _add_remaining_characters(result_parts, text, position, text_length)

    return ''.join(result_parts)



def naive_find_replace_slice(text: str, pattern: str, replacement: str, case_sensitive: bool = True) -> str:
    """
    Find and replace all occurrences of a pattern in text using string slicing.

    This algorithm leverages Python's built-in string slicing for more idiomatic
    and potentially more efficient "chunk-by-chunk" comparison rather than
    character-by-character comparison. It uses Python's native string slicing
    capabilities which are implemented in C for better performance on shorter patterns.

    Algorithm Strategy:
    1. Handles edge cases first (empty inputs, pattern longer than text)
    2. Uses optimized built-in replace() for single-character patterns
    3. Employs string slicing for pattern matching (more Pythonic approach)
    4. Uses list-based string building for optimal performance (O(n) vs O(n²))
    5. Handles case sensitivity through text preprocessing
    6. Implements non-overlapping replacement strategy

    Performance Characteristics:
    This slice-based approach can be more efficient when:
    - The pattern is relatively short (slice operation overhead is minimal)
    - Native string operations benefit from C-level optimization in Python interpreter
    - Memory locality is important (slice operations have good cache behavior)
    - There are fewer expected mismatches in typical inputs

    Performance Optimizations:
    - List accumulation instead of string concatenation prevents O(n²) complexity
    - String slicing leverages optimized C implementations for comparison
    - Single join operation at the end is more efficient than repeated concatenation
    - Short-circuit evaluation for single characters uses built-in optimized methods
    - Case sensitivity handled through preprocessing to avoid repeated conversions

    Time Complexity: O(n*m + r) - where n is text length, m is pattern length, r is result length
                    Pattern matching: O(n*m) worst case, better average with slice optimization
                    String building: O(r) for list operations + final join
    Space Complexity: O(r) - where r is the length of the result string

    Args:
        text: The input text to search within
        pattern: The pattern string to find and replace
        replacement: The string to replace each occurrence of the pattern (can be empty)
        case_sensitive: Whether pattern matching should be case sensitive (default: True)

    Returns:
        New string with all non-overlapping occurrences of pattern replaced by replacement

    Examples:
        >>> naive_find_replace_slice("hello world", "world", "python")
        'hello python'
        >>> naive_find_replace_slice("Hello World", "world", "Python", case_sensitive=False)
        'Hello Python'
        >>> naive_find_replace_slice("abcabc", "abc", "XY")
        'XYXY'

    Raises:
        No exceptions - handles all edge cases HAPPILY by returning appropriate values
    """
    # Handle edge cases
    should_return, result = _handle_edge_cases(text, pattern)
    if should_return:
        return result

    # Handle single character optimization
    should_return, result = _handle_single_char_replacement(text, pattern, replacement, case_sensitive)
    if should_return:
        return result

    # Setup common variables
    search_text, search_pattern, text_length, pattern_length, max_search_position = _setup_replacement_variables(
        text, pattern, case_sensitive)


    result_parts = []
    position = 0

    # Main search and replace loop using string slicing
    while position < max_search_position:

        # Use string slicing for pattern matching - leverages Python's optimized C implementation
        # This performs "chunk-by-chunk" comparison which can be more efficient than
        # character-by-character comparison for shorter patterns
        if search_text[position:position + pattern_length] == search_pattern:
            # Pattern match found - add replacement and skip past entire pattern
            # This implements non-overlapping replacement strategy
            result_parts.append(replacement)
            position += pattern_length
        else:
            # No match at current position - copy single character from original text
            # Use original text (not search_text) to preserve original case in result
            result_parts.append(text[position])
            position += 1

    # Handle remaining chars
    _add_remaining_characters(result_parts, text, position, text_length)

    return ''.join(result_parts)


def naive_find_replace_tunable(text: str, pattern: str, replacement: str, case_sensitive: bool = True,
                               slice_threshold: int = 4) -> str:
    """
    Find and replace all occurrences of a pattern in text using an adaptive approach.

    This algorithm combines the strengths of multiple pattern replacement strategies by
    adaptively selecting the most appropriate approach based on pattern characteristics.
    It represents a hybrid solution that maximizes performance across different input
    scenarios while maintaining code maintainability through strategy delegation.

    Algorithm Strategy Selection:
    The function dynamically chooses between two optimized strategies:

    1. Slice Strategy (for patterns <= slice_threshold):
       - Leverages Python's C-implemented string slicing operations
       - More efficient for shorter patterns due to reduced overhead
       - Benefits from native string comparison optimizations
       - Ideal when slice operation cost is minimal relative to pattern length

    2. Character Strategy (for patterns > slice_threshold):
       - Uses character-by-character comparison with early termination
       - More efficient for longer patterns when mismatches are common
       - Reduces unnecessary character comparisons through early exit
       - Better cache locality for large pattern matching

    Performance Characteristics:
    This adaptive approach provides optimal performance by:
    - Avoiding one-size-fits-all performance penalties
    - Selecting strategy based on empirically-determined thresholds
    - Leveraging Python's native optimizations where most beneficial
    - Providing tunable threshold for specific use case optimization

    The slice_threshold parameter can be tuned based on:
    - Average pattern lengths in your data
    - Expected mismatch frequency
    - Hardware characteristics (cache size, memory bandwidth)
    - Python implementation (CPython vs PyPy optimizations)

    Edge Case Handling:
    - Empty pattern: Returns original text unchanged
    - Empty text: Returns empty string immediately
    - Pattern longer than text: Returns original text (impossible to match)
    - Empty replacement: Performs deletion (replaces with nothing)
    - Single character patterns: Uses optimized built-in replace() method

    Time Complexity: O(n*m + r) - where n is text length, m is pattern length, r is result length
                    Strategy selection: O(1)
                    Pattern matching: O(n*m) worst case, better average with early termination
                    String building: O(r) via helper function optimizations
    Space Complexity: O(r) - where r is the length of the result string

    Args:
        text: The input text to search within and perform replacements on
        pattern: The pattern string to find and replace (cannot be empty)
        replacement: The string to replace each occurrence of the pattern with (can be empty for deletion)
        case_sensitive: Whether pattern matching should be case sensitive (default: True)
        slice_threshold: Threshold for strategy selection - patterns <= this length use slicing,
                        longer patterns use character comparison (default: 4, tunable for optimization)

    Returns:
        New string with all non-overlapping occurrences of pattern replaced by replacement

    Examples:
        >>> naive_find_replace_tunable("hello world", "world", "python")
        'hello python'
        >>> naive_find_replace_tunable("Hello World", "world", "Python", case_sensitive=False)
        'Hello Python'
        >>> naive_find_replace_tunable("abcabc", "abc", "XY")
        'XYXY'
        >>> naive_find_replace_tunable("remove this", "this", "")
        'remove '
        >>> naive_find_replace_tunable("test", "longpattern", "replacement")
        'test'

    Note:
        This function serves as a high-level interface that delegates to specialized
        helper functions. The slice_threshold parameter allows performance tuning
        for specific use cases and can be adjusted based on empirical testing.
    """
    # Handle edge cases
    should_return, result = _handle_edge_cases(text, pattern)
    if should_return:
        return result

    # Handle single character optimization
    should_return, result = _handle_single_char_replacement(text, pattern, replacement, case_sensitive)
    if should_return:
        return result

    # Setup common variables
    search_text, search_pattern, text_length, pattern_length, max_search_position = _setup_replacement_variables(
        text, pattern, case_sensitive)

    # Adaptive strategy selection based on pattern length and empirically-determined threshold
    # The threshold represents the crossover point where slice overhead becomes
    # less significant than the benefits of native string operations
    if pattern_length <= slice_threshold:
        # Use slice-based strategy for shorter patterns
        # Benefits from Python's C-implemented string slicing and comparison operations
        return _replace_using_slice_strategy(text, search_text, search_pattern, replacement,
                                             max_search_position, pattern_length)
    else:
        # Use character-based strategy for longer patterns
        # Benefits from early termination when mismatches occur frequently
        return _replace_using_character_strategy(text, search_text, search_pattern, replacement,
                                                 max_search_position, pattern_length)



def _replace_using_slice_strategy(text: str, search_text: str, search_pattern: str,
                                  replacement: str, max_search_position: int, pattern_length: int) -> str:
    """
    Replace using efficient string slicing for short patterns.

    This helper function implements the slice-based replacement strategy optimized
    for shorter patterns. It leverages Python's built-in string slicing capabilities
    which are implemented in C for better performance on pattern matching.

    Algorithm Strategy:
    1. Uses list accumulation for O(n) string building performance
    2. Employs string slicing for pattern matching (leverages C-level optimization)
    3. Implements proper non-overlapping replacement logic
    4. Uses original text for character copying to preserve case

    Performance Characteristics:
    This slice-based approach is more efficient when:
    - Pattern length is relatively short (slice operation overhead is minimal)
    - Native string slicing operations benefit from C-level optimization
    - Memory locality is important (slice operations have good cache behavior)

    Time Complexity: O(n*m) - where n is search length, m is pattern length
                    Pattern matching via slicing can be faster than character comparison
    Space Complexity: O(r) - where r is the result length (list accumulation)

    Args:
        text: Original input text (used for character copying to preserve case)
        search_text: Preprocessed text for pattern matching (may be case-normalized)
        search_pattern: Preprocessed pattern for matching (may be case-normalized)
        replacement: String to replace each pattern occurrence
        max_search_position: Maximum valid starting position for pattern search
        pattern_length: Length of the pattern (cached for performance)

    Returns:
        New string with all non-overlapping pattern occurrences replaced

    Note:
        This is a helper function designed to work with preprocessed inputs
        from the main find-replace functions. Input validation should be
        performed by the calling function.
    """
    # Use list for efficient string building - critical performance optimization
    # Python strings are immutable, so concatenation creates new objects each time.
    # List accumulation with final join is O(n) vs O(n²) for repeated concatenation
    result_parts = []
    position = 0

    # Main replacement loop with slice-based pattern matching
    while position < max_search_position:
        # Use string slicing for pattern matching - leverages Python's optimized C implementation
        # This performs "chunk-by-chunk" comparison which can be more efficient than
        # character-by-character comparison for shorter patterns
        if search_text[position:position + pattern_length] == search_pattern:
            # Pattern match found - add replacement and advance past entire pattern
            # This implements non-overlapping replacement strategy
            result_parts.append(replacement)
            position += pattern_length
        else:
            # No match at current position - copy single character from original text
            # Use original text (not search_text) to preserve original case in result
            result_parts.append(text[position])
            position += 1

    # Handle remaining chars
    _add_remaining_characters(result_parts, text, position, len(text))

    return ''.join(result_parts)


def _replace_using_character_strategy(text: str, search_text: str, search_pattern: str,
                                      replacement: str, max_search_position: int, pattern_length: int) -> str:
    """
    Replace using character comparison with early termination for longer patterns.

    This helper function implements the character-by-character replacement strategy
    optimized for longer patterns. It uses early termination on character mismatch
    to improve average-case performance when mismatches are common.

    Algorithm Strategy:
    1. Uses list accumulation for O(n) string building performance
    2. Employs character-by-character comparison with early termination
    3. Implements proper non-overlapping replacement logic
    4. Uses original text for character copying to preserve case

    Performance Characteristics:
    This character-based approach is more efficient when:
    - Pattern length is relatively long (reduces slice operation overhead)
    - Early termination can skip many character comparisons
    - Mismatches are common in the input data (benefits from early exit)

    Time Complexity: O(n*m) - where n is search length, m is pattern length
                    Best case approaches O(n) with early termination on mismatches
    Space Complexity: O(r) - where r is the result length (list accumulation)

    Args:
        text: Original input text (used for character copying to preserve case)
        search_text: Preprocessed text for pattern matching (may be case-normalized)
        search_pattern: Preprocessed pattern for matching (may be case-normalized)
        replacement: String to replace each pattern occurrence
        max_search_position: Maximum valid starting position for pattern search
        pattern_length: Length of the pattern (cached for performance)

    Returns:
        New string with all non-overlapping pattern occurrences replaced

    Note:
        This is a helper function designed to work with preprocessed inputs
        from the main find-replace functions. Input validation should be
        performed by the calling function.
    """
    # Use list for efficient string building - critical performance optimization
    # Python strings are immutable, so concatenation creates new objects each time.
    # List accumulation with final join is O(n) vs O(n²) for repeated concatenation
    result_parts = []
    position = 0

    # Main replacement loop with character-by-character pattern matching
    while position < max_search_position:
        # Pattern matching phase: character-by-character comparison with early termination
        pattern_index = 0
        while pattern_index < pattern_length:
            if search_text[position + pattern_index] == search_pattern[pattern_index]:
                pattern_index += 1
            else:
                # Early termination: stop comparing on first mismatch for efficiency
                break

        # Determine action based on match results
        if pattern_index == pattern_length:
            # Complete pattern match found - add replacement and advance past entire pattern
            # This implements non-overlapping replacement strategy
            result_parts.append(replacement)
            position += pattern_length
        else:
            # No match at current position - copy single character from original text
            # Use original text (not search_text) to preserve original case in result
            result_parts.append(text[position])
            position += 1

    # Handle remaining chars
    _add_remaining_characters(result_parts, text, position, len(text))

    return ''.join(result_parts)
