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
            'megumin',
            'cuddle',
            'hug',
            'awoo',
            'kiss',
            'pat',
            'smug',
            'bonk',
            'blush',
            'smile',
            'wink'
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

    if doge_type == 'hindi':
        url = os.path.join(cloudinary_base, "v1625168058/doge_hindi.jpg")
        return url

    if doge_type == 'gun':
        url = os.path.join(cloudinary_base, "v1625168273/doge_gun.png")
        return url

    if doge_type == 'sitting':
        url = os.path.join(cloudinary_base, "v1625168164/doge_sitting.png")
        return url

    if doge_type == 'quoge':
        url = os.path.join(cloudinary_base, "v1625168322/doge_quoge.png")
        return url

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    msg = message.content.lower().replace(" ", "")

    if msg == "crapwaifu":
        img = get_waifu(anime_base_url)
        await message.channel.send(img)

    if msg[0:8] == "crapdoge":
        doge_type = msg[8:]
        response = get_doge(doge_type)
        await message.channel.send(response)

client.run(token)
