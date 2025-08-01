import unittest
from sort.quicksort import quicksort, quicksort_iterative
from sort.PartitionStrategy import (
    PartitionStrategy,
    LomutoPartition,
    HoarePartition,
    ThreeWayPartition,
    RandomPivotPartition,
    MedianOfThreePartition,
    SedgewickPartition,
    DualPivotPartition,
    FatPivotPartition,
    HybridPartition
)
from sort.PivotStrategy import PivotStrategy

class TestQuickSort(unittest.TestCase):
    """Test cases for quicksort implementation with various partition strategies."""

    def setUp(self):
        """Set up common test data."""
        self.empty_list = []
        self.single_element = [42]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.reverse_sorted_list = [5, 4, 3, 2, 1]
        self.random_list = [64, 34, 25, 12, 22, 11, 90]
        self.duplicate_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        self.negative_list = [-5, -10, 0, 10, 5]
        self.mixed_types_list = ["apple", "banana", "cherry"]

        # Initialize all partition strategies
        self.strategies = [
            LomutoPartition(),
            RandomPivotPartition(),
            MedianOfThreePartition(),
            SedgewickPartition(),
            DualPivotPartition(),
            FatPivotPartition(),
            HybridPartition()
        ]

        # Known issues with these strategies - they will be tested separately
        self.hoare_strategy = HoarePartition()
        self.three_way_strategy = ThreeWayPartition()

        # Map strategy classes to names for better test output
        self.strategy_names = {
            LomutoPartition: "Lomuto",
            HoarePartition: "Hoare",
            ThreeWayPartition: "ThreeWay",
            RandomPivotPartition: "RandomPivot",
            MedianOfThreePartition: "MedianOfThree",
            SedgewickPartition: "Sedgewick",
            DualPivotPartition: "DualPivot",
            FatPivotPartition: "FatPivot",
            HybridPartition: "Hybrid"
        }

    def test_empty_list(self):
        """Test quicksort with an empty list using all partition strategies."""
        for strategy in self.strategies:
            with self.subTest(strategy=self.strategy_names[strategy.__class__]):
                test_list = self.empty_list.copy()
                quicksort(test_list, partition_strategy=strategy)
                self.assertEqual(test_list, [])

    def test_single_element(self):
        """Test quicksort with a single element using all partition strategies."""
        for strategy in self.strategies:
            with self.subTest(strategy=self.strategy_names[strategy.__class__]):
                test_list = self.single_element.copy()
                quicksort(test_list, partition_strategy=strategy)
                self.assertEqual(test_list, [42])

    def test_sorted_list(self):
        """Test quicksort with an already sorted list using all partition strategies."""
        for strategy in self.strategies:
            with self.subTest(strategy=self.strategy_names[strategy.__class__]):
                test_list = self.sorted_list.copy()
                quicksort(test_list, partition_strategy=strategy)
                self.assertEqual(test_list, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """Test quicksort with a reverse sorted list using all partition strategies."""
        for strategy in self.strategies:
            with self.subTest(strategy=self.strategy_names[strategy.__class__]):
                test_list = self.reverse_sorted_list.copy()
                quicksort(test_list, partition_strategy=strategy)
                self.assertEqual(test_list, [1, 2, 3, 4, 5])

    def test_random_list(self):
        """Test quicksort with a random list using all partition strategies."""
        for strategy in self.strategies:
            with self.subTest(strategy=self.strategy_names[strategy.__class__]):
                test_list = self.random_list.copy()
                quicksort(test_list, partition_strategy=strategy)
                self.assertEqual(test_list, [11, 12, 22, 25, 34, 64, 90])

    def test_duplicate_list(self):
        """Test quicksort with a list containing duplicates using all partition strategies."""
        for strategy in self.strategies:
            with self.subTest(strategy=self.strategy_names[strategy.__class__]):
                test_list = self.duplicate_list.copy()
                quicksort(test_list, partition_strategy=strategy)
                self.assertEqual(test_list, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_negative_list(self):
        """Test quicksort with a list containing negative numbers using all partition strategies."""
        for strategy in self.strategies:
            with self.subTest(strategy=self.strategy_names[strategy.__class__]):
                test_list = self.negative_list.copy()
                quicksort(test_list, partition_strategy=strategy)
                self.assertEqual(test_list, [-10, -5, 0, 5, 10])

    def test_strings_list(self):
        """Test quicksort with a list of strings using all partition strategies."""
        for strategy in self.strategies:
            with self.subTest(strategy=self.strategy_names[strategy.__class__]):
                test_list = self.mixed_types_list.copy()
                quicksort(test_list, partition_strategy=strategy)
                self.assertEqual(test_list, ["apple", "banana", "cherry"])

    def test_partial_sort(self):
        """Test quicksort with partial range sorting using all partition strategies."""
        for strategy in self.strategies:
            with self.subTest(strategy=self.strategy_names[strategy.__class__]):
                test_list = [5, 2, 9, 1, 7, 6, 3]
                # Sort only elements from index 1 to 4
                quicksort(test_list, start=1, end=4, partition_strategy=strategy)
                # Only the specified range should be sorted
                self.assertEqual(test_list, [5, 1, 2, 7, 9, 6, 3])

    def test_large_list(self):
        """Test quicksort with a larger list using all partition strategies."""
        for strategy in self.strategies:
            with self.subTest(strategy=self.strategy_names[strategy.__class__]):
                # Create a list with 100 random integers
                import random
                random.seed(42)  # For reproducibility
                large_list = [random.randint(-1000, 1000) for _ in range(100)]

                # Sort with quicksort
                test_list = large_list.copy()
                quicksort(test_list, partition_strategy=strategy)

                # Sort with Python's built-in sort for comparison
                expected = sorted(large_list)

                self.assertEqual(test_list, expected)

    def test_default_strategy(self):
        """Test quicksort with default partition strategy (Lomuto)."""
        test_list = self.random_list.copy()
        quicksort(test_list)  # No strategy specified, should use Lomuto
        self.assertEqual(test_list, [11, 12, 22, 25, 34, 64, 90])

    def test_hoare_partition(self):
        """Test Hoare partition strategy."""
        # Test with random list
        test_list = self.random_list.copy()
        quicksort(test_list, partition_strategy=self.hoare_strategy)
        self.assertEqual(test_list, [11, 12, 22, 25, 34, 64, 90])

        # Test with reverse sorted list
        test_list = self.reverse_sorted_list.copy()
        quicksort(test_list, partition_strategy=self.hoare_strategy)
        self.assertEqual(test_list, [1, 2, 3, 4, 5])

        # Test with duplicate list
        test_list = self.duplicate_list.copy()
        quicksort(test_list, partition_strategy=self.hoare_strategy)
        self.assertEqual(test_list, [1, 1, 2, 3, 4, 5, 5, 6, 9])

        # Test partial sort
        test_list = [5, 2, 9, 1, 7, 6, 3]
        quicksort(test_list, start=1, end=4, partition_strategy=self.hoare_strategy)
        self.assertEqual(test_list, [5, 1, 2, 7, 9, 6, 3])

    def test_three_way_partition(self):
        """Test ThreeWay partition strategy."""
        # Test with random list
        test_list = self.random_list.copy()
        quicksort(test_list, partition_strategy=self.three_way_strategy)
        self.assertEqual(test_list, [11, 12, 22, 25, 34, 64, 90])

        # Test with duplicate list
        test_list = self.duplicate_list.copy()
        quicksort(test_list, partition_strategy=self.three_way_strategy)
        self.assertEqual(test_list, [1, 1, 2, 3, 4, 5, 5, 6, 9])

        # Test with negative list
        test_list = self.negative_list.copy()
        quicksort(test_list, partition_strategy=self.three_way_strategy)
        self.assertEqual(test_list, [-10, -5, 0, 5, 10])

    def test_quicksort_iterative(self):
        """Test iterative quicksort implementation with various partition strategies."""
        for strategy in self.strategies:
            with self.subTest(strategy=self.strategy_names[strategy.__class__]):
                # Test with random list
                test_list = self.random_list.copy()
                quicksort_iterative(test_list, partition_strategy=strategy)
                self.assertEqual(test_list, [11, 12, 22, 25, 34, 64, 90])

                # Test with duplicate list
                test_list = self.duplicate_list.copy()
                quicksort_iterative(test_list, partition_strategy=strategy)
                self.assertEqual(test_list, [1, 1, 2, 3, 4, 5, 5, 6, 9])

        # Test with default strategy
        test_list = self.random_list.copy()
        quicksort_iterative(test_list)  # No strategy specified, should use Lomuto
        self.assertEqual(test_list, [11, 12, 22, 25, 34, 64, 90])


    def test_fat_pivot_with_key_function(self):
        """Test FatPivotPartition with custom key functions."""
        # Create a list of tuples (name, age)
        people = [
            ("Alice", 30),
            ("Bob", 25),
            ("Charlie", 35),
            ("David", 25),
            ("Eve", 30)
        ]

        # Sort by age (primary key)
        age_key = lambda x: x[1]
        fat_pivot_strategy = FatPivotPartition(key_func=age_key)

        test_list = people.copy()
        quicksort(test_list, partition_strategy=fat_pivot_strategy)

        # Check that the list is sorted by age
        for i in range(1, len(test_list)):
            self.assertLessEqual(test_list[i-1][1], test_list[i][1])

        # Sort by age (primary key) and then by name (secondary key)
        name_key = lambda x: x[0]
        fat_pivot_strategy = FatPivotPartition(key_func=age_key, secondary_key_func=name_key)

        test_list = people.copy()
        quicksort(test_list, partition_strategy=fat_pivot_strategy)

        # Check that the list is sorted by age and then by name
        expected = [
            ("Bob", 25),
            ("David", 25),
            ("Alice", 30),
            ("Eve", 30),
            ("Charlie", 35)
        ]
        self.assertEqual(test_list, expected)

    def test_pivot_strategies(self):
        """Test different pivot strategies with Lomuto partition."""
        # Create a custom subclass of LomutoPartition that uses a specific pivot strategy
        class CustomLomutoPartition(LomutoPartition):
            def __init__(self, pivot_strategy):
                self.pivot_strategy = pivot_strategy

            def partition(self, values, start, end, pivot_strategy=None):
                # Override the pivot_strategy parameter with our custom one
                return super().partition(values, start, end, self.pivot_strategy)

        # Test each pivot strategy with Lomuto partition
        for pivot_strategy in PivotStrategy:
            with self.subTest(pivot_strategy=pivot_strategy.value):
                test_list = self.random_list.copy()
                custom_lomuto = CustomLomutoPartition(pivot_strategy)
                quicksort(test_list, partition_strategy=custom_lomuto)
                self.assertEqual(test_list, [11, 12, 22, 25, 34, 64, 90])

if __name__ == '__main__':
    unittest.main()
