import unittest
from unittest.mock import patch
from io import StringIO
from apps.tower_of_hanoi.tower_of_hanoi import TowerOfHanoi, GameConfig

class TestTowerOfHanoi(unittest.TestCase):
    @patch('builtins.input', return_value='3')  # Mock user input for ring count
    def setUp(self, mock_input):
        """Set up a game instance for testing"""
        self.game = TowerOfHanoi()
        # Reset the mock to avoid affecting other tests
        mock_input.reset_mock()

    def test_game_config(self):
        """Test GameConfig initialization"""
        config = GameConfig()
        self.assertEqual(config.min_rings, 3)
        self.assertEqual(config.max_rings, 10)
        self.assertEqual(config.tower_names, ("Left", "Middle", "Right"))

        # Test custom config
        custom_config = GameConfig(min_rings=2, max_rings=5, tower_names=("A", "B", "C"))
        self.assertEqual(custom_config.min_rings, 2)
        self.assertEqual(custom_config.max_rings, 5)
        self.assertEqual(custom_config.tower_names, ("A", "B", "C"))

    @patch('builtins.input', return_value='3')
    def test_initialization(self, mock_input):
        """Test game initialization"""
        game = TowerOfHanoi()

        # Check towers are created correctly
        self.assertEqual(len(game.towers), 3)
        self.assertEqual(game.source.name, "Left")
        self.assertEqual(game.auxiliary.name, "Middle")
        self.assertEqual(game.target.name, "Right")

        # Check rings are placed on source tower
        self.assertEqual(game.source._size, 3)
        self.assertEqual(game.auxiliary._size, 0)
        self.assertEqual(game.target._size, 0)

        # Check optimal moves calculation
        self.assertEqual(game.optimal_moves, 7)  # 2^3 - 1 = 7

        # Check initial moves count
        self.assertEqual(game.moves, 0)

    @patch('builtins.input', return_value='5')
    def test_different_ring_count(self, mock_input):
        """Test initialization with different ring count"""
        game = TowerOfHanoi()

        # Check rings are placed on source tower
        self.assertEqual(game.source._size, 5)

        # Check optimal moves calculation
        self.assertEqual(game.optimal_moves, 31)  # 2^5 - 1 = 31

    def test_make_move_valid(self):
        """Test making a valid move"""
        # Initial state: [3, 2, 1] on source, [] on auxiliary, [] on target

        # Move from source to auxiliary (valid: smaller disk on empty tower)
        result = self.game._make_move(self.game.source, self.game.auxiliary)
        self.assertTrue(result)
        self.assertEqual(self.game.source._size, 2)
        self.assertEqual(self.game.auxiliary._size, 1)
        self.assertEqual(self.game.moves, 1)

        # Move from source to target (valid: smaller disk on empty tower)
        result = self.game._make_move(self.game.source, self.game.target)
        self.assertTrue(result)
        self.assertEqual(self.game.source._size, 1)
        self.assertEqual(self.game.target._size, 1)
        self.assertEqual(self.game.moves, 2)

        # Move from auxiliary to target (valid: smaller disk on larger disk)
        result = self.game._make_move(self.game.auxiliary, self.game.target)
        self.assertTrue(result)
        self.assertEqual(self.game.auxiliary._size, 0)
        self.assertEqual(self.game.target._size, 2)
        self.assertEqual(self.game.moves, 3)

    def test_make_move_invalid_empty(self):
        """Test making an invalid move from empty tower"""
        # Move from empty auxiliary to target (invalid: source is empty)
        result = self.game._make_move(self.game.auxiliary, self.game.target)
        self.assertFalse(result)
        self.assertEqual(self.game.auxiliary._size, 0)
        self.assertEqual(self.game.target._size, 0)
        self.assertEqual(self.game.moves, 0)

    def test_make_move_invalid_size(self):
        """Test making an invalid move with larger disk on smaller disk"""
        # Move top disk from source to auxiliary
        self.game._make_move(self.game.source, self.game.auxiliary)

        # Try to move larger disk from source to auxiliary (invalid: larger on smaller)
        result = self.game._make_move(self.game.source, self.game.auxiliary)
        self.assertFalse(result)
        self.assertEqual(self.game.source._size, 2)
        self.assertEqual(self.game.auxiliary._size, 1)
        self.assertEqual(self.game.moves, 1)

    def test_is_complete(self):
        """Test is_complete method"""
        # Initial state: game is not complete
        self.assertFalse(self.game.is_complete())

        # Manually set up a completed game state by moving all disks to target tower
        # Clear the source tower
        while not self.game.source.is_empty():
            self.game.source.pop()

        # Put all disks on target tower in correct order (largest at bottom)
        for ring in range(self.game.num_rings, 0, -1):
            self.game.target.push(ring)

        # Now game should be complete
        self.assertTrue(self.game.is_complete())

    @patch('builtins.print')
    def test_display_state(self, mock_print):
        """Test display_state method"""
        self.game.display_state()
        mock_print.assert_called()  # Just verify that print was called

if __name__ == '__main__':
    unittest.main()
