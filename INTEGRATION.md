# Chameleon Bot Integration Guide

This document outlines the integration points and development guide for adding the Chameleon game functionality to the bot.

## Architecture Overview

The Chameleon bot follows a modular architecture using Discord.py's cog system:

```
Chameleon/
├── bot.py                      # Main bot entry point and event handlers
├── cogs/
│   ├── chameleon_game.py      # Game commands and Discord interactions
│   ├── general.py             # General utility commands
│   └── owner.py               # Bot owner management commands
├── utils/
│   └── game_logic.py          # Core game logic (language-agnostic)
├── data/
│   └── word_lists.json        # Word lists organized by category
└── database/
    ├── __init__.py            # Database manager
    └── schema.sql             # Database schema
```

## Integration Points

### 1. Game Commands (`cogs/chameleon_game.py`)

This cog handles all Discord-specific game interactions:

- **Commands to implement:**
  - `/start_game` - Initiates a new game session in the channel
  - `/end_game` - Ends the current game session
  - `/game_rules` - Displays game rules and instructions
  - `/join_game` - Allows players to join before game starts
  - `/give_clue <word>` - Players submit their clues
  - `/vote <player>` - Vote for who you think is the Chameleon
  - `/guess <word>` - Chameleon's final guess attempt

- **Integration points:**
  - Uses `GameSession` from `utils/game_logic.py` for game state
  - Uses `WordListManager` from `utils/game_logic.py` for word selection
  - Sends DMs to players with their secret word (or Chameleon status)
  - Creates interactive embeds for game state display

### 2. Game Logic (`utils/game_logic.py`)

Contains the core game mechanics independent of Discord:

- **`GameSession` class:**
  - Manages player list, Chameleon selection, secret word
  - Tracks clues, votes, and game state
  - Implements win condition checking

- **`WordListManager` class:**
  - Loads and manages word lists from JSON
  - Provides random word selection by category
  - Supports category filtering

### 3. Data Storage (`data/word_lists.json`)

JSON file containing word lists organized by categories:

```json
{
  "category_name": ["word1", "word2", "word3"],
  ...
}
```

**To expand word lists:**
- Add new categories as keys
- Add words as arrays under each category
- Words should be simple, recognizable, and appropriate

### 4. Database Integration (Optional)

The existing database system can be extended to track:

- Game statistics (wins, losses, games played)
- Player statistics (times caught as Chameleon, successful guesses)
- Leaderboards

**Schema additions needed:**
```sql
CREATE TABLE IF NOT EXISTS game_history (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    channel_id INTEGER,
    server_id INTEGER,
    chameleon_id INTEGER,
    secret_word TEXT,
    chameleon_caught BOOLEAN,
    chameleon_guessed_word BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS player_stats (
    user_id INTEGER,
    server_id INTEGER,
    games_played INTEGER DEFAULT 0,
    times_chameleon INTEGER DEFAULT 0,
    times_caught INTEGER DEFAULT 0,
    successful_guesses INTEGER DEFAULT 0,
    PRIMARY KEY (user_id, server_id)
);
```

## Development Workflow

### Phase 1: Basic Game Flow
1. Implement player joining mechanism
2. Implement Chameleon selection and word distribution
3. Create clue submission and display
4. Implement voting mechanism

### Phase 2: Advanced Features
1. Add timer for each phase (joining, clues, voting)
2. Add reaction-based voting interface
3. Implement Chameleon's final guess
4. Add game history and statistics

### Phase 3: Polish
1. Add custom word list upload per server
2. Implement leaderboards
3. Add game difficulty settings
4. Add custom emoji and styling

## Discord Intents Required

The bot requires these intents (already configured):
- `message_content` - To read command messages
- `members` - To access member information for DMs
- `reactions` - For reaction-based voting (if implemented)

## Bot Permissions Required

The bot needs these permissions:
- **Send Messages** - To send game messages and responses
- **Embed Links** - To send rich game state embeds
- **Add Reactions** - For reaction-based voting
- **Manage Messages** - To clean up game messages (optional)
- **Read Message History** - To track game flow
- **Send Messages in Threads** - If thread-based games are supported

## Testing Checklist

Before deploying game features:

- [ ] Test with minimum players (3)
- [ ] Test with maximum players (8-10)
- [ ] Test Chameleon winning by guessing correctly
- [ ] Test Chameleon losing when caught
- [ ] Test Chameleon winning when not caught
- [ ] Test concurrent games in different channels
- [ ] Test game cleanup on unexpected errors
- [ ] Test with invalid inputs and edge cases
- [ ] Test DM delivery failures (user has DMs disabled)
- [ ] Test word list loading and selection

## Code Style Guidelines

- Follow PEP 8 conventions
- Use type hints for all function parameters and returns
- Format code with `black --line-length 120`
- Add comprehensive docstrings to all classes and methods
- Keep game logic separate from Discord interactions
- Handle errors gracefully with user-friendly messages

## Environment Variables

Required in `.env`:
```
DISCORD_BOT_TOKEN=your_token_here
COMMAND_PREFIX=!
INVITE_LINK=your_invite_link
```

## Next Steps

1. Review and test the placeholder implementations
2. Implement the game flow in `chameleon_game.py`
3. Add unit tests for `game_logic.py`
4. Expand word lists in `word_lists.json`
5. Add database tracking for statistics
6. Implement leaderboard commands
7. Add configuration options per server

## Resources

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Chameleon Game Rules](https://boardgamegeek.com/boardgame/227224/chameleon)

## Support

For questions or issues during development:
1. Check the Discord.py documentation
2. Review the existing cog implementations in `cogs/general.py` and `cogs/owner.py`
3. Test changes in a development Discord server before production
