# Chameleon Discord Bot

A Discord bot for playing the Chameleon game - a social deduction party game where players try to identify the impostor (the Chameleon) based on word associations!

## About the Game

In Chameleon, all players except one receive a secret word. The Chameleon must blend in by giving clues without knowing what the word is. After everyone gives their clues, players vote on who they think is the Chameleon. If caught, the Chameleon can still win by correctly guessing the secret word!

## Features

- 🦎 Full Chameleon game implementation (coming soon)
- 🎮 Interactive game sessions with multiple players
- 📊 Game statistics and leaderboards (planned)
- 🎨 Custom word lists and categories
- ⚙️ Easy configuration and setup
- 🔒 Owner-only bot management commands

## Installation

### Prerequisites

- Python 3.12 or higher
- Discord Bot Token ([Create one here](https://discord.com/developers/applications))
- Basic knowledge of Discord bots

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Be1l-ai/Chameleon.git
   cd Chameleon
   ```

2. **Install dependencies:**
   ```bash
   python -m pip install -r requirements.txt
   ```

3. **Configure the bot:**
   
   Rename `.env.example` to `.env` and fill in your bot token:
   ```env
   DISCORD_BOT_TOKEN=your_bot_token_here
   COMMAND_PREFIX=!
   INVITE_LINK=your_bot_invite_link_here
   ```

4. **Run the bot:**
   ```bash
   python bot.py
   ```

### Docker Setup

You can also run the bot using Docker:

```bash
docker compose up -d --build
```

> **Note**: `-d` runs the container in detached mode (in the background).

## Configuration

### Environment Variables

- `DISCORD_BOT_TOKEN` - Your Discord bot token (required)
- `COMMAND_PREFIX` - Prefix for text commands (default: `!`)
- `INVITE_LINK` - Invite link for your bot (optional)

### Required Bot Permissions

When inviting the bot to your server, ensure it has these permissions:

- **Read Messages/View Channels** - To see game channels
- **Send Messages** - To send game messages and responses
- **Embed Links** - To send rich game embeds
- **Add Reactions** - For reaction-based voting
- **Send Messages in Threads** - For thread-based games (optional)
- **Manage Messages** - To clean up game messages (optional)

### Required Bot Intents

The following intents are enabled and must be turned on in the Discord Developer Portal:

- **Message Content Intent** - To read command messages
- **Server Members Intent** - To access member information for DMs
- **Presence Intent** - For member reactions (optional)

**To enable intents:**
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your application
3. Navigate to the "Bot" section
4. Scroll down to "Privileged Gateway Intents"
5. Enable the required intents

## Usage

### Commands

#### Game Commands
- `/start_game` - Start a new Chameleon game in the current channel
- `/end_game` - End the current game session
- `/game_rules` - Display the game rules and instructions

#### General Commands
- `/help` - List all available commands
- `/ping` - Check if the bot is responsive
- `/botinfo` - Get information about the bot
- `/serverinfo` - Get information about the current server
- `/invite` - Get the bot invite link

#### Owner Commands (Bot Owner Only)
- `!sync <global|guild>` - Sync slash commands
- `/load <cog>` - Load a cog/extension
- `/unload <cog>` - Unload a cog/extension
- `/reload <cog>` - Reload a cog/extension
- `/shutdown` - Shut down the bot

## Development

See [INTEGRATION.md](INTEGRATION.md) for detailed development documentation and integration guide.

### Project Structure

```
Chameleon/
├── bot.py                 # Main bot entry point
├── cogs/                  # Command modules (cogs)
│   ├── chameleon_game.py # Game commands
│   ├── general.py        # General utility commands
│   └── owner.py          # Bot owner commands
├── utils/                 # Utility modules
│   └── game_logic.py     # Core game logic
├── data/                  # Data files
│   └── word_lists.json   # Word lists for the game
├── database/              # Database management
│   ├── __init__.py       # Database manager
│   └── schema.sql        # Database schema
└── requirements.txt       # Python dependencies
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.

## Built With

- [Python 3.12.9](https://www.python.org/)

## Attribution

This project is based on the [Python Discord Bot Template](https://github.com/kkrypt0nn/Python-Discord-Bot-Template) by [kkrypt0nn](https://github.com/kkrypt0nn).

Original work Copyright 2019-Present Krypton (kkrypt0nn) - Licensed under the Apache License, Version 2.0.

The template has been forked and modified to create a Chameleon game bot.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
