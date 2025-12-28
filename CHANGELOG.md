# Changelog

All notable changes to the Chameleon Discord Bot project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Forked from [Python Discord Bot Template](https://github.com/kkrypt0nn/Python-Discord-Bot-Template) by kkrypt0nn
- Apache 2.0 license compliance with NOTICE file and copyright headers
- Chameleon game cog placeholder (`cogs/chameleon_game.py`)
- Core game logic module (`utils/game_logic.py`)
- Word lists configuration (`data/word_lists.json`)
- Integration documentation (`INTEGRATION.md`)
- Bot intents enabled: `message_content`, `members`, `reactions`
- Updated environment variables to use `DISCORD_BOT_TOKEN` and `COMMAND_PREFIX`

### Changed
- Updated bot status messages to reflect Chameleon game theme
- Updated `botinfo` command to show Chameleon bot information
- Reformatted all Python code with black (line-length 120)
- Updated requirements.txt with version constraints
- Updated .env.example with new variable names
- Modified README.md to include attribution section

### Removed
- Template example cogs: `fun.py`, `moderation.py`, `template.py`
- Template-specific commands: bitcoin, 8ball, server invite, feedback form
- Template warning/moderation system (can be re-added if needed)

### Fixed
- Added `logs/` directory to .gitignore

## [0.1.0] - 2025-01-XX

### Initial Release
- Basic bot framework ready for Chameleon game implementation
- Core infrastructure: logging, error handling, config management
- Owner commands for bot management
- General utility commands (help, ping, serverinfo, invite)
- Database support with SQLite
- Docker support maintained from original template

---

## Attribution

This project is based on the Python Discord Bot Template:
- **Original Author**: Krypton (kkrypt0nn)
- **Original Repository**: https://github.com/kkrypt0nn/Python-Discord-Bot-Template
- **License**: Apache License 2.0
- **Original Copyright**: 2019-Present Krypton

Modified by Be1l-ai to create a Chameleon game bot.
