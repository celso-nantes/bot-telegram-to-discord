# Telegram-To-Discord
Mirrors all messages from Telegram sends them to the webhook. 

# Requirements

- Python 3.10 or later
- Python pip -> requirements.txt
- Discord bot token
- Telegram API tokens

# How to run
```py
#Download the repo and extract to an empty folder
#Open a CLI ex. CMD,PS,GitBash in the directory
pip3 install -r requirements.txt
#Rename example.env to .env
#Edit info in .env
#APPID and HASH are created here https://core.telegram.org/api/obtaining_api_id
python3 main.py
