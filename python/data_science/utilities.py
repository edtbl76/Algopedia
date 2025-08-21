"""
This is just a generic utilities file for helper functions.

- Calculate Probability

"""
from typing import Set, Any


def calculate_probability(event: Set[Any], state_space: Set[Any]) -> float:
    """
    Calculate probability of an event in a discrete uniform probability space.

    Assumes all outcomes in the state space are equally likely, so probability
    is calculated as the ratio of favorable outcomes to total outcomes.

    Time Complexity: O(1) - uses built-in len() which is constant time for sets
    Space Complexity: O(1) - only stores scalar values

    Args:
        event (Set[Any]): Set of favorable outcomes
        state_space (Set[Any]): Complete set of all possible outcomes

    Returns:
        float: Probability of the event (number between 0 and 1)

    Raises:
        ValueError: If state_space is empty (division by zero prevention)

    Note:
        This function assumes a uniform distribution where each outcome
        has equal probability of 1/|state_space|.
    """
    if len(state_space) == 0:
        raise ValueError("State space cannot be empty")

    # Classical probability: favorable outcomes / total outcomes
    return len(event) / len(state_space)