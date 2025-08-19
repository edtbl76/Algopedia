"""
Addition Rule for Probability Calculations

This module implements the addition rule for probability theory, which calculates
the probability of the union of two events. The addition rule states that:
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

This fundamental rule prevents double-counting elements that appear in both events
by subtracting the probability of their intersection.

State Space:
The state space (also called sample space) is the set of all possible outcomes
of a probability experiment. It represents every outcome that could potentially
occur. For example:
- Rolling a die: state space = {1, 2, 3, 4, 5, 6}
- Flipping a coin: state space = {heads, tails}
- Drawing a card: state space = {all 52 cards in a deck}

Events are subsets of the state space representing specific outcomes of interest.
For instance, "rolling an even number" would be the event {2, 4, 6} within
the die rolling state space.

The implementation assumes a discrete uniform probability space where all outcomes
in the state space are equally likely (each outcome has probability 1/|state_space|).
"""

from typing import Any, Set

def addition_rule_probability(event_a: Set[Any], event_b: Set[Any], state_space: Set[Any]) -> float:
    """
    Calculate the probability of the union of two events using the addition rule.

    Implements P(A ∪ B) = P(A) + P(B) - P(A ∩ B) for discrete uniform probability spaces.

    Time Complexity: O(min(|A|, |B|)) for set intersection operation
    Space Complexity: O(min(|A|, |B|)) for storing intersection result

    Args:
        event_a (Set[Any]): First event as a set of outcomes
        event_b (Set[Any]): Second event as a set of outcomes
        state_space (Set[Any]): Complete set of all possible outcomes

    Returns:
        float: Probability of event A or event B occurring (P(A ∪ B))

    Raises:
        ValueError: If state_space is empty (raised by helper function)

    Example:
        >>> state = {1, 2, 3, 4, 5, 6}  # Sample space for die roll
        >>> event_even = {2, 4, 6}      # Rolling even number
        >>> event_high = {4, 5, 6}      # Rolling 4 or higher
        >>> addition_rule_probability(event_even, event_high, state)
        0.6666666666666667  # P(even OR high) = 4/6 = 2/3
    """
    # Calculate individual probabilities - O(1) operations
    probability_a: float = _calculate_probability(event_a, state_space)
    probability_b: float = _calculate_probability(event_b, state_space)

    # Find intersection of events - O(min(|A|, |B|)) operation
    intersection_events: Set[Any] = event_a.intersection(event_b)

    # Calculate probability of intersection - O(1) operation
    probability_intersection: float = _calculate_probability(intersection_events, state_space)

    # Apply addition rule: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
    # Subtract intersection to avoid double-counting overlapping outcomes
    return probability_a + probability_b - probability_intersection

### HELPERS ###

def _calculate_probability(event: Set[Any], state_space: Set[Any]) -> float:
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





