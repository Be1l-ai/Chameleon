# Copyright 2025 Be1l-ai - Modified for Chameleon Bot
# Licensed under the Apache License, Version 2.0
"""
Core game logic for the Chameleon game.

This module contains the business logic for running a Chameleon game session,
including player management, word selection, voting, and win condition checking.
"""

from typing import List, Optional, Dict, Any
import random


class GameSession:
    """Represents a single Chameleon game session."""

    def __init__(self, channel_id: int, players: List[int]) -> None:
        """
        Initialize a new game session.

        :param channel_id: The Discord channel ID where the game is being played.
        :param players: List of player user IDs participating in the game.
        """
        self.channel_id = channel_id
        self.players = players
        self.chameleon_id: Optional[int] = None
        self.secret_word: Optional[str] = None
        self.category: Optional[str] = None
        self.clues: Dict[int, str] = {}
        self.votes: Dict[int, int] = {}
        self.game_state = "setup"  # setup, giving_clues, voting, ended

    def select_chameleon(self) -> int:
        """
        Randomly select a player to be the Chameleon.

        :return: The user ID of the selected Chameleon.
        """
        self.chameleon_id = random.choice(self.players)
        return self.chameleon_id

    def set_secret_word(self, word: str, category: str) -> None:
        """
        Set the secret word for this game session.

        :param word: The secret word that all players except the Chameleon will know.
        :param category: The category of the secret word.
        """
        self.secret_word = word
        self.category = category

    def add_clue(self, player_id: int, clue: str) -> bool:
        """
        Add a clue from a player.

        :param player_id: The user ID of the player giving the clue.
        :param clue: The clue provided by the player.
        :return: True if the clue was added successfully, False otherwise.
        """
        if player_id not in self.players:
            return False
        self.clues[player_id] = clue
        return True

    def add_vote(self, voter_id: int, voted_for_id: int) -> bool:
        """
        Add a vote for who the voter thinks is the Chameleon.

        :param voter_id: The user ID of the player casting the vote.
        :param voted_for_id: The user ID of the player being voted for.
        :return: True if the vote was recorded successfully, False otherwise.
        """
        if voter_id not in self.players or voted_for_id not in self.players:
            return False
        self.votes[voter_id] = voted_for_id
        return True

    def get_vote_results(self) -> Dict[int, int]:
        """
        Calculate and return the vote results.

        :return: Dictionary mapping player IDs to the number of votes they received.
        """
        vote_counts: Dict[int, int] = {player: 0 for player in self.players}
        for voted_for in self.votes.values():
            vote_counts[voted_for] += 1
        return vote_counts

    def check_chameleon_caught(self) -> tuple[bool, Optional[int]]:
        """
        Check if the Chameleon was caught (received the most votes).

        :return: Tuple of (was_caught: bool, most_voted_player_id: Optional[int])
        """
        vote_results = self.get_vote_results()
        if not vote_results:
            return False, None

        most_voted = max(vote_results.items(), key=lambda x: x[1])
        return most_voted[0] == self.chameleon_id, most_voted[0]


class WordListManager:
    """Manages word lists and categories for the game."""

    def __init__(self, word_lists: Dict[str, List[str]]) -> None:
        """
        Initialize the word list manager.

        :param word_lists: Dictionary mapping categories to lists of words.
        """
        self.word_lists = word_lists

    def get_random_word(self, category: Optional[str] = None) -> tuple[str, str]:
        """
        Get a random word from a category.

        :param category: Specific category to choose from, or None for random category.
        :return: Tuple of (word, category)
        """
        if category is None or category not in self.word_lists:
            category = random.choice(list(self.word_lists.keys()))

        if not self.word_lists[category]:
            raise ValueError(f"No words available in category: {category}")

        word = random.choice(self.word_lists[category])
        return word, category

    def get_categories(self) -> List[str]:
        """
        Get all available categories.

        :return: List of category names.
        """
        return list(self.word_lists.keys())
