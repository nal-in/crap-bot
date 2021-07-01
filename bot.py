import os
import random
import discord
import requests

anime_base_url = os.environ['ANIME_BASE_URL']
token = os.environ['BOT_TOKEN']

client = discord.Client()

def get_img(anime_base_url):
    keywords = [
            'waifu',
            'neko',
            'shinobu',
            'megumin'
    ]
    keyword = keywords[random.randint(0, len(keywords))]
    url = anime_base_url + keyword
    res = requests.get(url)
    return res.json()['url']

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    msg = message.content.lower().replace(" ", "")
    if msg == "crapwaifu":
        img = get_img(anime_base_url)
        await message.channel.send(img)

client.run(token)
