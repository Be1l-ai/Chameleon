# Copyright 2025 Be1l-ai - Modified for Chameleon Bot
# Licensed under the Apache License, Version 2.0
"""
Chameleon game commands and logic.

This cog handles all game-related commands for the Chameleon game where players
try to identify the impostor (chameleon) among them based on word associations.
"""

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context


class ChameleonGame(commands.Cog, name="chameleon"):
    """Chameleon game cog for managing game sessions."""

    def __init__(self, bot) -> None:
        """
        Initialize the Chameleon game cog.

        :param bot: The Discord bot instance.
        """
        self.bot = bot
        # Game state will be stored here
        self.active_games = {}

    @commands.hybrid_command(name="start_game", description="Start a new Chameleon game in this channel.")
    async def start_game(self, context: Context) -> None:
        """
        Start a new Chameleon game session.

        :param context: The hybrid command context.
        """
        # TODO: Implement game start logic
        embed = discord.Embed(
            title="🦎 Chameleon Game",
            description="Game start functionality will be implemented here!",
            color=0x00FF00,
        )
        await context.send(embed=embed)

    @commands.hybrid_command(name="end_game", description="End the current Chameleon game in this channel.")
    async def end_game(self, context: Context) -> None:
        """
        End the current Chameleon game session.

        :param context: The hybrid command context.
        """
        # TODO: Implement game end logic
        embed = discord.Embed(
            title="🦎 Chameleon Game",
            description="Game end functionality will be implemented here!",
            color=0xFF0000,
        )
        await context.send(embed=embed)

    @commands.hybrid_command(name="game_rules", description="Display the rules of the Chameleon game.")
    async def game_rules(self, context: Context) -> None:
        """
        Display the rules and instructions for playing Chameleon.

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            title="🦎 Chameleon Game Rules",
            description=(
                "**Objective:** Find the Chameleon among the players!\n\n"
                "**How to Play:**\n"
                "1. All players receive a secret word except one (the Chameleon)\n"
                "2. Each player gives a one-word clue related to the secret word\n"
                "3. The Chameleon must blend in without knowing the word\n"
                "4. After clues, vote on who you think is the Chameleon\n"
                "5. If caught, the Chameleon can guess the word to win!\n\n"
                "**Commands:**\n"
                "`/start_game` - Start a new game\n"
                "`/end_game` - End the current game\n"
                "`/game_rules` - Show these rules"
            ),
            color=0xBEBEFE,
        )
        await context.send(embed=embed)


async def setup(bot) -> None:
    """
    Setup function to add the cog to the bot.

    :param bot: The Discord bot instance.
    """
    await bot.add_cog(ChameleonGame(bot))
