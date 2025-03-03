import discord
from discord.ext import commands
from config import token

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah login sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def tentang(ctx):
    await ctx.send('Ini adalah echo-bot yang dibuat dengan pustaka discord.py!')

@client.command()
async def info(ctx):
    await ctx.send('Untuk menggunakan bot ini, gunakan prefix `/` di awal pesan!')

@client.command()
async def tujuan(ctx):
    await ctx.send('Untuk memudahkan pengguna dalam mengulang pesan yang dikirimkan!')

client.run(token)