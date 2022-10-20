from telethon import TelegramClient, events
import telethon
import aiohttp
import nextcord
import textwrap
import os
import requests
import json
import random
from dotenv import load_dotenv
from datetime import datetime
from pytz import timezone    

load_dotenv()

url = os.environ.get("WEBHOOK")
appid = os.environ.get("APPID")
apihash = os.environ.get("APIHASH")
apiname = os.environ.get("APINAME")
dlloc = os.environ.get("DLLOC")
input_channels_entities = os.environ.get("INPUT_CHANNELS")
blacklist = os.environ.get("BLACKLIST")

if blacklist == 'True':
    blacklist = True
if input_channels_entities is not None:
  input_channels_entities = list(map(int, input_channels_entities.split(',')))

def start():
    client = TelegramClient(apiname, appid, apihash)
    client.start()
    print('Started')
    print(f'Input channels: {input_channels_entities}')
    print(f'Blacklist: {blacklist}')
    @client.on(events.NewMessage(chats=input_channels_entities, blacklist_chats=blacklist))
    async def handler(event):
        if (type(event.chat)==telethon.tl.types.User):
          return #Ignore Messages from Users or Bots
        msg = event.message.message
        await send_to_webhook(msg,event.chat.title)
        
    client.run_until_disconnected()

async def send_to_webhook(message,username): # Send message to webhook
    async with aiohttp.ClientSession() as session:
        print('Sending w/o media')
        webhook = nextcord.Webhook.from_url(url, session=session)
        for line in textwrap.wrap(message, 2000, replace_whitespace=False): # Send message to discord
            embed = nextcord.Embed(description="```{}```".format(line), color=nextcord.Colour.random(), timestamp=datetime.now(timezone('America/Sao_Paulo')))
            await webhook.send(embed=embed,username=username)

if __name__ == "__main__":
    start()
