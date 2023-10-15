# Goniec AnyCode

## Introduction

AnyCode Bot is a Discord bot designed for the AnyCode community and it serves a representative and information function.

## Features

### Welcome and Goodbye Messages
Whenever a user joins or leaves the server, the bot will send a welcome or goodbye message to the specified text channel. 

### Notification Forwarding
The bot can forward notifications of Discord messages to Messenger.

### Commands
All bot commands start with '$'. For example, to use the member command, you would type `$member` followed by the specific query.
- **$member Command**: Get information about AnyCode members. This command provides details about organization members.

- **$history Command**: Retrieve the history of AnyCode. This command can display the server's history, achievements, or any relevant information.

- **$info Command**: Get information about AnyCode. Use this command to learn more about the organization, its purpose, and guidelines.
  
## Development

The bot is designed with easy development in mind. You'll find predefined variables for server roles and channels within the codebase, making it straightforward to customize and extend the bot's functionality. The bot also includes robust logging to help you track its activities.

## How to contribute

1. Clone this repository.
2. Create a Virtual Environment
First, create a virtual environment to isolate the bot's dependencies. If you haven't already installed `virtualenv`, you can do so with pip:
```bash
pip install virtualenv
```
3. Create a virtual environment in your project directory:
```bash
virtualenv .venv
```
4. Install discord.py
```bash
pip install -U discord.py
```
5. Install python-dotenv for environment variable management
```bash
pip install python-dotenv
```
6. Configure the bot by adding 'DISCORD_API_TOKEN={token-string}' into .evn file
*Important note: Don't share this token with anyone.*
