import discord
import requests

from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Created by: nvr'))
    print(f'BOT ONLINE - {client.user.name}')
    print(f'ID DO BOT {client.user.id}')

# Welcome Message
@client.event
async def on_member_join(member):
    canal = client.get_channel('450911361543831552') # ID of channel Welcome

    url = requests.get(member.avatar_url)

    avatar = Image.open(BytesIO(url.content))
    avatar = avatar.resize((130, 130));
    bigsize = (avatar.size[0] * 3,  avatar.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(avatar.size, Image.ANTIALIAS)
    avatar.putalpha(mask)

    output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save('avatar.png')

    avatar = Image.open('avatar.png')
    fundo = Image.open('bemvindo.png')
    fonte = ImageFont.truetype('BebasNeue.ttf', 45)
    escrever = ImageDraw.Draw(fundo)
    escrever.text(xy=(180, 174), text=member.name, fill=(53, 59, 72), font=fonte) # output name when the user join!
    fundo.paste(avatar, (40, 90), avatar)
    fundo.save('bv.png')
    await client.send_file(canal, 'bv.png')

client.run("YOUR_TOKEN_BOT")
