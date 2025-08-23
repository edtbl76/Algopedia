"""
Multiplication Rule for probability Calculations

This module implements the multiplication rule for probability theory, which calculates
the probability of the intersection of two events (both events occurring together).
The multiplication rule has different forms depending on whether events are independent
or dependent:

Independent Events:
- P(A ∩ B) = P(A) × P(B)
- The occurrence of one event does not affect the probability of the other

Dependent Events:
- P(A ∩ B) = P(A) × P(B|A)
- Where P(B|A) is the conditional probability of B given A has occurred

The module also includes Bayes' theorem implementation, which uses the multiplication
rule as a foundation for calculating posterior probabilities.

Mathematical Background:
The multiplication rule is fundamental in probability theory and stems from the
definition of conditional probability:
- P(B|A) = P(A ∩ B) / P(A)
- Rearranging: P(A ∩ B) = P(A) × P(B|A)

For independent events, P(B|A) = P(B), which simplifies the rule to P(A ∩ B) = P(A) × P(B).

State Space Assumptions:
All functions assume a discrete uniform probability space where outcomes in the
state space are equally likely. Each outcome has probability 1/|state_space|.

Example Applications:
- Card drawing: probability of drawing two specific cards
- Dice rolling: probability of rolling specific combinations
- Survey analysis: probability of respondents having multiple characteristics
"""


from typing import Any, Set
from data_science.probability.utilities import calculate_probability


def multiplication_rule_for_independent_events(event_a: Set[Any], event_b: Set[Any], state_space: Set[Any]) -> float:
    """
    Calculate P(A ∩ B) for independent events using multiplication rule.

    For independent events: P(A ∩ B) = P(A) × P(B)

    Args:
        event_a: Set of outcomes for event A
        event_b: Set of outcomes for event B
        state_space: Complete set of all possible outcomes

    Returns:
        probability of both events occurring
    """
    # Apply multiplication rule for independent events: P(A ∩ B) = P(A) × P(B)
    return calculate_probability(event_a, state_space) * calculate_probability(event_b, state_space)


def multiplication_rule_for_dependent_events(event_a: Set[Any], event_b: Set[Any], state_space: Set[Any]) -> float:
    """
    Calculate P(A ∩ B) for dependent events using multiplication rule.

    For dependent events: P(A ∩ B) = P(A) × P(B|A)
    Where P(B|A) = P(A ∩ B) / P(A)

    Args:
        event_a: Set of outcomes for event A
        event_b: Set of outcomes for event B
        state_space: Complete set of all possible outcomes

    Returns:
        probability of both events occurring

    Raises:
        ValueError: If event A has zero probability (cannot calculate conditional probability)
    """
    # Step 1: Calculate the probability of event A occurring
    probability_a: float = calculate_probability(event_a, state_space)

    # Step 2: Check if event A has zero probability - if so, conditional probability is undefined
    if probability_a == 0:
        raise ValueError("Cannot calculate conditional probability of event A with zero probability")


    # Step 3:
    # - Find the intersection of events A and B (outcomes where both A and B occur) via helper call
    # - Calculate P(A ∩ B) - the probability of both events occurring together
    probability_a_and_b: float = _calculate_intersection_probability(event_a, event_b, state_space)

    # Step 4: Calculate conditional probability P(B|A) using the formula P(B|A) = P(A ∩ B) / P(A)
    conditional_probability_b_given_a: float = probability_a_and_b / probability_a

    # Step 5: Apply multiplication rule for dependent events: P(A ∩ B) = P(A) × P(B|A)
    # Note: This equals probability_a_and_b, but demonstrates the multiplication rule formula
    return probability_a * conditional_probability_b_given_a


def bayes_theorem(event_a: Set[Any], event_b: Set[Any], state_space: Set[Any]) -> float:
    """
    Calculate P(A|B) using Bayes' theorem.

    Historical Background:
    Bayes' theorem is named after Reverend Thomas Bayes (1702-1761), an English
    Presbyterian minister and mathematician. The theorem was posthumously published
    in 1763 in "An Essay towards solving a Problem in the Doctrine of Chances" by
    Richard Price, who refined Bayes' original work.

    The theorem gained prominence through the work of Pierre-Simon Laplace (1749-1827),
    who independently discovered and extensively developed the concept. Laplace called
    it the "probability of causes" and used it to solve astronomical and statistical
    problems. The modern formulation and widespread application of Bayesian statistics
    emerged in the 20th century, particularly through the work of Harold Jeffreys,
    Bruno de Finetti, and Dennis Lindley.

    Mathematical Foundation:
    Bayes' theorem provides a way to update probabilities based on new evidence.
    It describes the probability of an event based on prior knowledge of conditions
    that might be related to the event.

    Formula: P(A|B) = P(B|A) × P(A) / P(B)

    Where:
    - P(A|B) is the posterior probability: probability of A given B is true
    - P(B|A) is the likelihood: probability of B given A is true
    - P(A) is the prior probability: initial probability of A
    - P(B) is the marginal probability: total probability of B

    Applications:
    - Medical diagnosis: updating disease probability given test results
    - Machine learning: spam filtering, classification algorithms
    - Statistics: parameter estimation and hypothesis testing
    - Finance: risk assessment and portfolio optimization
    - Artificial intelligence: reasoning under uncertainty

    The theorem is fundamental to Bayesian statistics, which treats probability as
    a measure of belief or confidence rather than just frequency. This philosophical
    approach contrasts with frequentist statistics and has led to ongoing debates
    in statistical methodology.

    Args:
        event_a: Set of outcomes for event A
        event_b: Set of outcomes for event B
        state_space: Complete set of all possible outcomes

    Returns:
        Conditional probability P(A|B)

    Raises:
        ValueError: If event B has zero probability

    Example:
        Medical diagnosis scenario:
        - A = patient has disease (prior knowledge: 1% of population has disease)
        - B = positive test result (test is 90% accurate)
        - Bayes' theorem calculates P(disease|positive test)
    """

    # Calculate P(A) - prior probability
    probability_a: float = calculate_probability(event_a, state_space)

    # Calculate P(B) - marginal probability
    probability_b: float = calculate_probability(event_b, state_space)

    # Check if P(B) is zero - cannot calculate conditional probability
    if probability_b == 0:
        raise ValueError("Cannot calculate Bayes' theorem with event B having zero probability")

    # Calculate P(A ∩ B) - joint probability
    probability_a_and_b: float = _calculate_intersection_probability(event_a, event_b, state_space)

    # Calculate P(B|A) - likelihood
    if probability_a == 0:
        probability_b_given_a: float = 0
    else:
        probability_b_given_a: float = probability_a_and_b / probability_a

    # Apply Bayes' theorem: P(A|B) = P(B|A) × P(A) / P(B)
    return (probability_b_given_a * probability_a) / probability_b


def bayes_theorem_with_known_probabilities(prior_a: float, likelihood_b_given_a: float, marginal_b: float) -> float:
    """
    Calculate P(A|B) using Bayes' theorem with known probabilities.

    Bayes' theorem: P(A|B) = P(B|A) × P(A) / P(B)

    Args:
        prior_a: P(A) - prior probability of event A
        likelihood_b_given_a: P(B|A) - likelihood of B given A
        marginal_b: P(B) - marginal probability of event B

    Returns:
        Posterior probability P(A|B)

    Raises:
        ValueError: If marginal_b is zero or probabilities are invalid
    """
    # Validate input probabilities
    if not (0 <= prior_a <= 1):
        raise ValueError("Prior probability must be between 0 and 1")
    if not (0 <= likelihood_b_given_a <= 1):
        raise ValueError("Likelihood must be between 0 and 1")
    if not (0 <= marginal_b <= 1):
        raise ValueError("Marginal probability must be between 0 and 1")

    if marginal_b == 0:
        raise ValueError("Cannot calculate Bayes' theorem with marginal probability of zero")

    # Apply Bayes' theorem: P(A|B) = P(B|A) × P(A) / P(B)
    return (likelihood_b_given_a * prior_a) / marginal_b


### HELPERS ###
def _calculate_intersection_probability(event_a: Set[Any], event_b: Set[Any], state_space: Set[Any]) -> float:
    """
    Helper function to calculate P(A ∩ B) - probability of intersection of two events.

    Args:
        event_a: Set of outcomes for event A
        event_b: Set of outcomes for event B
        state_space: Complete set of all possible outcomes

    Returns:
        probability of both events occurring together
    """
    intersection_events: Set[Any] = event_a.intersection(event_b)
    return calculate_probability(intersection_events, state_space)
