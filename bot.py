import os
import random
import discord
import requests
import pymongo

anime_base_url = os.environ['ANIME_BASE_URL']
token = os.environ['BOT_TOKEN']
cloudinary_base = os.environ["CLOUDINARY_BASE"]
num_quotes = 1643
mongo_url = os.environ["MONGO_URL"]

client = discord.Client()

def get_help():
    m = "You have summoned the crap bot.\n\tcrap waifu: get waifu pics\n\tcrap quote: get motivational quotes\n\tcrap doge help: get help with the crap doge commands"
    return m

def get_waifu():
    keywords = [
            'waifu',
            'neko',
            'cuddle',
            'hug',
            'awoo',
            'kiss',
            'pat',
            'smug',
            'bonk',
            'blush',
            'smile',
            'wave',
            'handhold',
            'happy',
            'wink'
    ]
    keyword = keywords[random.randint(0, len(keywords))]
    url = os.path.join(anime_base_url, keyword)
    res = requests.get(url)
    return res.json()['url']

def get_quote():
    idx = random.randint(0, num_quotes)
    mongo_client = pymongo.MongoClient(mongo_url)
    return mongo_url
    db = mongo_client["crap_motivator"]
    collection = db["normal_quotes"]

    res = collection.find_one({"idx": idx})
    return res["quote"]


def get_doge(doge_type):
    assert doge_type in ['help', 'smirk', 'hindi', 'gun', 'sitting', 'quoge', 'wow', 'sad', 'swole', 'chinese']

    if doge_type == 'help':
        m = "Available doge commands:\n\tcrap doge sitting\n\tcrap doge smirk\n\tcrap doge hindi\n\tcrap doge quoge\n\tcrap doge gun\n\tcrap doge wow\n\tcrap doge sad\n\tcrap doge swole\n\tcrap doge chinese"
        return m
    
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

    if doge_type == 'wow':
        url = os.path.join(cloudinary_base, "v1625247089/doge_wow.jpg")
        return url

    if doge_type == 'sad':
        url = os.path.join(cloudinary_base, "v1625247015/doge_sad.png")
        return url

    if doge_type == 'swole':
        url = os.path.join(cloudinary_base, "v1625246942/doge_swole.jpg")
        return url

    if doge_type == 'chinese':
        url = os.path.join(cloudinary_base, "v1625246909/doge_chinese.jpg")
        return url

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    msg = message.content.lower().replace(" ", "")

    if msg == "craphelp":
        response = get_help()
        await message.channel.send(response)

    if msg == "crapwaifu":
        response = get_waifu()
        await message.channel.send(response)

    if msg == "crapquote":
        response = get_quote()
        await message.channel.send(response)

    if msg[0:8] == "crapdoge":
        doge_type = msg[8:]
        response = get_doge(doge_type)
        await message.channel.send(response)

client.run(token)
