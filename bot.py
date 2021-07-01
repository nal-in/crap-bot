import os
import random
import discord
import requests

anime_base_url = os.environ['ANIME_BASE_URL']
token = os.environ['BOT_TOKEN']
cloudinary_base = os.environ["CLOUDINARY_BASE"]

client = discord.Client()

def get_waifu(anime_base_url):
    keywords = [
            'waifu',
            'neko',
            'shinobu',
            'megumin'
    ]
    keyword = keywords[random.randint(0, len(keywords))]
    url = os.path.join(anime_base_url, keyword)
    res = requests.get(url)
    return res.json()['url']

def get_doge(doge_type):
    assert doge_type in ['smirk', 'hindi', 'gun', 'sitting', 'quoge']
    
    if doge_type == 'smirk':
        url = os.path.join(cloudinary_base, "v1625167973/doge_smirk.png")
        return url



@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    msg = message.content.lower().replace(" ", "")

    if msg == "crapwaifu":
        img = get_waifu(anime_base_url)
        await message.channel.send(img)

    if msg == "crapdogesmirk":
        img = get_doge('smirk')
        await message.channel.send(img)

client.run(token)
