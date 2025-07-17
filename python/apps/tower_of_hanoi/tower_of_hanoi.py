#!/usr/bin/env python3
from dataclasses import dataclass
from typing import Tuple, List

from apps.tower_of_hanoi.NamedStack import NamedStack

@dataclass
class GameConfig:
    """ Configuration parameters for Tower of Hanoi game"""
    min_rings: int = 3
    max_rings: int = 10
    tower_names: Tuple[str, ...] = ("Left", "Middle", "Right")


class TowerOfHanoi:
    """
    Tower of Hanoi game implementation.
    A classic puzzle game where rings must be moved between three towers
    following specific rules.
    """

    INVALID_MOVE_EMPTY = "\nInvalid Move: Source tower is empty"
    INVALID_MOVE_SIZE = "\nInvalid Move: Cannot place larger ring on smaller ring"
    TOWER_PROMPT = "\nWhich tower do you want to move {direction}?"
    RING_PROMPT = "\nHow many rings do you want to play with [Between {min} and {max}]?\n"

    def __init__(self) -> None:
        self.config: GameConfig = GameConfig()
        self.towers: List[NamedStack] = [NamedStack(name) for name in self.config.tower_names]
        self.source:  NamedStack
        self.auxiliary: NamedStack
        self.target: NamedStack
        self.source, self.auxiliary, self.target = self.towers
        self.moves: int  = 0
        self.num_rings = self._get_valid_ring_count()
        self.optimal_moves: int = 0
        self._initialize_game()

    def _get_valid_ring_count(self) -> int:
        while True:
            try:
                prompt = self.RING_PROMPT.format(min=self.config.min_rings, max=self.config.max_rings)
                rings = int(input(prompt))
                if self.config.min_rings <= rings <= self.config.max_rings:
                    return rings
                print(f"Please enter a number between {self.config.min_rings} and {self.config.max_rings}")
            except ValueError:
                print("Please enter a valid number")

    def _initialize_game(self) -> None:
        for ring in range(self.num_rings, 0, -1):
            self.source.push(ring)
        self.optimal_moves = (2 ** self.num_rings) - 1
        print(f"\nThe best solution to this game is {self.optimal_moves} moves.")

    def _select_tower(self, direction: str) -> NamedStack:
        while True:
            print(self.TOWER_PROMPT.format(direction=direction))
            for tower in self.towers:
                print(f"Enter {tower.name[0]} for {tower.name}")
            choice = input("").upper()
            for tower in self.towers:
                if choice == tower.name[0]:
                    return tower
            print("Invalid selection. Please try again.")

    def _make_move(self, from_tower: NamedStack, to_tower: NamedStack) -> bool:
        if from_tower.is_empty():
            print(self.INVALID_MOVE_EMPTY)
            return False
        if not to_tower.is_empty() and from_tower.peek >= to_tower.peek:
            print(self.INVALID_MOVE_SIZE)
            return False

        to_tower.push(from_tower.pop())
        self.moves += 1
        return True

    def display_state(self) -> None:
        print("\n=== Current Towers ===")
        for tower in self.towers:
            tower.display_contents()

    def is_complete(self) -> bool:
        return self.target._size == self.num_rings


    def play(self) -> None:
        """Start and run the Tower of Hanoi game"""
        print("\n=== Towers of Hanoi ===")
        while not self.is_complete():
            self.display_state()
            from_tower = self._select_tower("from")
            to_tower = self._select_tower("to")

            if self._make_move(from_tower, to_tower):
                print(f"\nMoves: {self.moves} (Optimal: {self.optimal_moves})")

if __name__ == "__main__":
    game = TowerOfHanoi()
    game.play()
