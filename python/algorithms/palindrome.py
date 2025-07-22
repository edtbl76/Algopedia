def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome using iterative two-pointer approach.

    This algorithm uses two pointers starting from opposite ends of the string,
    moving inward and comparing characters until they meet in the middle.

    Time Complexity: O(n) - where n is the length of the string.
                    We examine at most n/2 characters.
    Space Complexity: O(1) - only uses constant additional space regardless
                     of input size.

    Args:
        text: The string to check for palindrome property

    Returns:
        True if the string is a palindrome, False otherwise

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("")
        True
    """


    text_length: int = len(text)
    middle_idx: int = text_length // 2

    for front_index in range(0, middle_idx):
        back_index: int = text_length - front_index - 1

        if text[front_index] != text[back_index]:
            return False

    return True

def is_palindrome_quadratic(text: str) -> bool:
    """
    Check if a string is a palindrome using string slicing approach.

    This algorithm repeatedly creates new string slices by removing the first
    and last characters until the string has length <= 1.

    Time Complexity: O(n²) - where n is the length of the string.
                    String slicing creates new strings, and we do this n/2 times.
    Space Complexity: O(n²) - due to creating multiple string slices during execution.

    Args:
        text: The string to check for palindrome property

    Returns:
        True if the string is a palindrome, False otherwise

    Examples:
        >>> is_palindrome_quadratic("racecar")
        True
        >>> is_palindrome_quadratic("hello")
        False
    """

    while len(text) > 1:
        if text[0] != text[-1]:
            return False
        text = text[1:-1]
    return True

def is_palindrome_recursive_optimized(text: str) -> bool:
    """
    Check if a string is a palindrome using an optimized recursive approach with indices.

    This is a BETTER SOLUTION than the basic recursive approach above because it avoids
    creating new string slices at each recursive call, instead using indices to track
    the current substring boundaries.

    Time Complexity: O(n) - where n is the length of the string.
                    We examine at most n/2 characters, similar to the iterative approach.
    Space Complexity: O(n) - due to the call stack depth (n/2 recursive calls).

    This approach is superior to the basic recursive version because:
    1. No string slicing overhead - avoids O(n) string creation at each level
    2. Reduces time complexity from O(n²) to O(n)
    3. Reduces space complexity from O(n²) to O(n)
    4. Maintains the elegance of recursion while achieving optimal performance

    Args:
        text: The string to check for palindrome property

    Returns:
        True if the string is a palindrome, False otherwise

    Examples:
        >>> is_palindrome_recursive_optimized("racecar")
        True
        >>> is_palindrome_recursive_optimized("hello")
        False
        >>> is_palindrome_recursive_optimized("")
        True
        >>> is_palindrome_recursive_optimized("a")
        True
    """

    """ 
        Helper function to check if a pair of characters at indices left and right is a palindrome. 
        This allows us to retain the method signature without having to pass indices around.    
    """
    def _helper(left: int, right: int) -> bool:
        # Base case: pointers have crossed or met
        if left >= right:
            return True

        # If characters don't match, not a palindrome
        if text[left] != text[right]:
            return False

        # Recursively check the next inner pair
        return _helper(left + 1, right - 1)

    return _helper(0, len(text) - 1)


def is_palindrome_recursive_quadratic(text: str) -> bool:
    """
    Check if a string is a palindrome using recursive divide-and-conquer approach.

    This algorithm recursively checks if the first and last characters match,
    then recursively processes the substring between them.

    Time Complexity: O(n²) - where n is the length of the string.
                    Each recursive call creates a new string slice O(n),
                    and we make O(n) recursive calls.
    Space Complexity: O(n²) - O(n) call stack depth plus O(n) space for each
                     string slice created at each recursive level.

    Base Case:
        - Empty string or single character (len <= 1) is always a palindrome

    Recursive Step:
        - Compare first and last characters
        - If they don't match, return False
        - If they match, recursively check the substring excluding first and last chars

    Args:
        text: The string to check for palindrome property

    Returns:
        True if the string is a palindrome, False otherwise

    Examples:
        >>> is_palindrome_recursive_quadratic("racecar")
        True
        >>> is_palindrome_recursive_quadratic("hello")
        False
        >>> is_palindrome_recursive_quadratic("a")
        True
    """

    # Base case: strings of length 0 or 1 are palindromes
    if len(text) <= 1:
        return True

    # Base case: if first and last characters don't match, not a palindrome
    if text[0] != text[-1]:
        return False

    # Recursive step: check the substring excluding first and last characters
    return is_palindrome_recursive_quadratic(text[1:-1])



