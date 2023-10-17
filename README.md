# Goniec AnyCode

## Introduction

# This is the messenger branch

## Setup

Facebook API requires two values to function properly. Both are set in `.env`:
1. `DISCORD_API_TOKEN`
2. `FB_PAGE_ID`
3. `FB_PAGE_ACCESS`

Not sure whether `FB_PAGE_ACCESS` needs to be reset every so often. I have acquired a 'long-lived page access token', which shouldn't expire, but who knows what Facebook will do.
User IDs, API endpoints etc. are handled by the module itself.

## Usage

Sample usage is shown in `fbtest.py`.

- `from Interfaces.FacebookInterface import FacebookInterface`
- Create a `FacebookInterface` object
- Create a message object, which is a Python object(! not raw json)
- `FacebookInterface` provides two (public) methods:
    - `send_privmessage(message_obj, user_id)` - sends a formatted private message to the selected User ID. This User ID is only Page-scoped, so you need to know it in advance. This will probably become a private function.
    - `broadcast_message(message_obj)` - `FacebookInterface` fetches all User IDs that ever messaged the Page, and sends a formatted message to each User.
