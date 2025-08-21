import unittest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from data_science.multiplication_rule import (
    multiplication_rule_for_independent_events,
    multiplication_rule_for_dependent_events,
    bayes_theorem,
    bayes_theorem_with_known_probabilities,
    _calculate_intersection_probability
)


class TestMultiplicationRule(unittest.TestCase):
    def test_multiplication_rule_for_independent_events_basic(self):
        """Test basic multiplication rule for independent events with simple sets"""
        state_space = {1, 2, 3, 4, 5, 6}  # Die roll
        event_a = {2, 4, 6}  # Even numbers
        event_b = {1, 3, 5}  # Odd numbers
        
        result = multiplication_rule_for_independent_events(event_a, event_b, state_space)
        self.assertEqual(result, 0.25)  # P(A) × P(B) = 0.5 × 0.5 = 0.25
    
    def test_multiplication_rule_for_independent_events_empty_event(self):
        """Test multiplication rule for independent events with an empty event"""
        state_space = {1, 2, 3, 4, 5, 6}
        event_a = {2, 4, 6}
        event_b = set()
        
        result = multiplication_rule_for_independent_events(event_a, event_b, state_space)
        self.assertEqual(result, 0.0)  # P(A) × P(B) = 0.5 × 0 = 0
    
    def test_multiplication_rule_for_independent_events_full_event(self):
        """Test multiplication rule for independent events when one event equals state space"""
        state_space = {1, 2, 3, 4, 5, 6}
        event_a = {1, 2, 3, 4, 5, 6}
        event_b = {2, 4, 6}
        
        result = multiplication_rule_for_independent_events(event_a, event_b, state_space)
        self.assertEqual(result, 0.5)  # P(A) × P(B) = 1.0 × 0.5 = 0.5
    
    def test_multiplication_rule_for_independent_events_empty_state_space(self):
        """Test multiplication rule for independent events with empty state space (should raise ValueError)"""
        state_space = set()
        event_a = {1, 2, 3}
        event_b = {4, 5, 6}
        
        with self.assertRaises(ValueError):
            multiplication_rule_for_independent_events(event_a, event_b, state_space)
    
    def test_multiplication_rule_for_dependent_events_basic(self):
        """Test basic multiplication rule for dependent events with simple sets"""
        state_space = {1, 2, 3, 4, 5, 6}  # Die roll
        event_a = {2, 4, 6}  # Even numbers
        event_b = {4, 5, 6}  # Numbers >= 4
        
        result = multiplication_rule_for_dependent_events(event_a, event_b, state_space)
        # P(A ∩ B) = P(A) × P(B|A) = 0.5 × (2/3) = 0.3333...
        self.assertAlmostEqual(result, 0.3333333333333333)
    
    def test_multiplication_rule_for_dependent_events_zero_probability_a(self):
        """Test multiplication rule for dependent events when event A has zero probability"""
        state_space = {1, 2, 3, 4, 5, 6}
        event_a = set()  # Empty event (zero probability)
        event_b = {2, 4, 6}
        
        with self.assertRaises(ValueError):
            multiplication_rule_for_dependent_events(event_a, event_b, state_space)
    
    def test_multiplication_rule_for_dependent_events_disjoint_events(self):
        """Test multiplication rule for dependent events with disjoint events"""
        state_space = {1, 2, 3, 4, 5, 6}
        event_a = {1, 2, 3}
        event_b = {4, 5, 6}
        
        result = multiplication_rule_for_dependent_events(event_a, event_b, state_space)
        self.assertEqual(result, 0.0)  # P(A ∩ B) = P(A) × P(B|A) = 0.5 × 0 = 0
    
    def test_multiplication_rule_for_dependent_events_identical_events(self):
        """Test multiplication rule for dependent events with identical events"""
        state_space = {1, 2, 3, 4, 5, 6}
        event_a = {1, 2, 3}
        event_b = {1, 2, 3}
        
        result = multiplication_rule_for_dependent_events(event_a, event_b, state_space)
        self.assertEqual(result, 0.5)  # P(A ∩ B) = P(A) × P(B|A) = 0.5 × 1.0 = 0.5
    
    def test_bayes_theorem_basic(self):
        """Test basic Bayes' theorem calculation with simple sets"""
        state_space = {1, 2, 3, 4, 5, 6}  # Die roll
        event_a = {2, 4, 6}  # Even numbers
        event_b = {4, 5, 6}  # Numbers >= 4
        
        result = bayes_theorem(event_a, event_b, state_space)
        # P(A|B) = P(B|A) × P(A) / P(B) = (2/3) × 0.5 / 0.5 = 0.6666...
        self.assertAlmostEqual(result, 0.6666666666666666)
    
    def test_bayes_theorem_zero_probability_b(self):
        """Test Bayes' theorem when event B has zero probability"""
        state_space = {1, 2, 3, 4, 5, 6}
        event_a = {2, 4, 6}
        event_b = set()  # Empty event (zero probability)
        
        with self.assertRaises(ValueError):
            bayes_theorem(event_a, event_b, state_space)
    
    def test_bayes_theorem_zero_probability_a(self):
        """Test Bayes' theorem when event A has zero probability"""
        state_space = {1, 2, 3, 4, 5, 6}
        event_a = set()  # Empty event (zero probability)
        event_b = {2, 4, 6}
        
        result = bayes_theorem(event_a, event_b, state_space)
        self.assertEqual(result, 0.0)  # P(A|B) = 0 when P(A) = 0
    
    def test_bayes_theorem_disjoint_events(self):
        """Test Bayes' theorem with disjoint events"""
        state_space = {1, 2, 3, 4, 5, 6}
        event_a = {1, 2, 3}
        event_b = {4, 5, 6}
        
        result = bayes_theorem(event_a, event_b, state_space)
        self.assertEqual(result, 0.0)  # P(A|B) = 0 when A and B are disjoint
    
    def test_bayes_theorem_identical_events(self):
        """Test Bayes' theorem with identical events"""
        state_space = {1, 2, 3, 4, 5, 6}
        event_a = {1, 2, 3}
        event_b = {1, 2, 3}
        
        result = bayes_theorem(event_a, event_b, state_space)
        self.assertEqual(result, 1.0)  # P(A|B) = 1.0 when A and B are identical
    
    def test_bayes_theorem_with_known_probabilities_basic(self):
        """Test basic Bayes' theorem with known probabilities"""
        prior_a = 0.5  # P(A) = 0.5
        likelihood_b_given_a = 0.8  # P(B|A) = 0.8
        marginal_b = 0.6  # P(B) = 0.6
        
        result = bayes_theorem_with_known_probabilities(prior_a, likelihood_b_given_a, marginal_b)
        # P(A|B) = P(B|A) × P(A) / P(B) = 0.8 × 0.5 / 0.6 = 0.6666...
        self.assertAlmostEqual(result, 0.6666666666666666)
    
    def test_bayes_theorem_with_known_probabilities_zero_marginal(self):
        """Test Bayes' theorem with known probabilities when marginal probability is zero"""
        prior_a = 0.5
        likelihood_b_given_a = 0.8
        marginal_b = 0.0
        
        with self.assertRaises(ValueError):
            bayes_theorem_with_known_probabilities(prior_a, likelihood_b_given_a, marginal_b)
    
    def test_bayes_theorem_with_known_probabilities_invalid_prior(self):
        """Test Bayes' theorem with known probabilities when prior probability is invalid"""
        prior_a = 1.5  # Invalid probability (> 1)
        likelihood_b_given_a = 0.8
        marginal_b = 0.6
        
        with self.assertRaises(ValueError):
            bayes_theorem_with_known_probabilities(prior_a, likelihood_b_given_a, marginal_b)
    
    def test_bayes_theorem_with_known_probabilities_invalid_likelihood(self):
        """Test Bayes' theorem with known probabilities when likelihood is invalid"""
        prior_a = 0.5
        likelihood_b_given_a = -0.2  # Invalid probability (< 0)
        marginal_b = 0.6
        
        with self.assertRaises(ValueError):
            bayes_theorem_with_known_probabilities(prior_a, likelihood_b_given_a, marginal_b)
    
    def test_bayes_theorem_with_known_probabilities_invalid_marginal(self):
        """Test Bayes' theorem with known probabilities when marginal probability is invalid"""
        prior_a = 0.5
        likelihood_b_given_a = 0.8
        marginal_b = 1.2  # Invalid probability (> 1)
        
        with self.assertRaises(ValueError):
            bayes_theorem_with_known_probabilities(prior_a, likelihood_b_given_a, marginal_b)
    
    def test_calculate_intersection_probability(self):
        """Test helper function to calculate intersection probability"""
        state_space = {1, 2, 3, 4, 5, 6}
        event_a = {2, 4, 6}
        event_b = {4, 5, 6}
        
        result = _calculate_intersection_probability(event_a, event_b, state_space)
        self.assertAlmostEqual(result, 0.3333333333333333)  # P(A ∩ B) = 2/6 = 0.3333...
    
    def test_calculate_intersection_probability_disjoint(self):
        """Test helper function with disjoint events"""
        state_space = {1, 2, 3, 4, 5, 6}
        event_a = {1, 2, 3}
        event_b = {4, 5, 6}
        
        result = _calculate_intersection_probability(event_a, event_b, state_space)
        self.assertEqual(result, 0.0)  # P(A ∩ B) = 0 when A and B are disjoint
    
    def test_calculate_intersection_probability_empty_event(self):
        """Test helper function with an empty event"""
        state_space = {1, 2, 3, 4, 5, 6}
        event_a = set()
        event_b = {2, 4, 6}
        
        result = _calculate_intersection_probability(event_a, event_b, state_space)
        self.assertEqual(result, 0.0)  # P(A ∩ B) = 0 when A is empty


if __name__ == '__main__':
    unittest.main()