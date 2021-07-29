import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():

    print(f'{client.user.name} is connected to Discord!')

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
        await message.channel.send("I am here!")

@client.event
async def on_member_join(member):
    channel = client.get_channel(869656874524500028)
    await channel.send(f'Hi {member.name}, welcome to Botapalooza!')
    
client.run(TOKEN)
