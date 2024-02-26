import discord
from datetime import datetime
import asyncio
from discord import app_commands
from responses import handle_response
import dotenv

config = dotenv.dotenv_values('.env')

def run_discord_bot():
    #client setup

    intents = discord.Intents.default()
    intents.message_content = True
    activity = discord.Activity(name='YOU', type=discord.ActivityType.watching)
    client = discord.Client(intents=intents, activity=activity)
    tree = app_commands.CommandTree(client)

    @client.event
    #bot starts running
    async def on_ready():
        await tree.sync()
        print(f'{client.user} is now running :D')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return None

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: {user_message} ({channel})')

        if user_message[0] == '!':
            response = handle_response(user_message[1:])
            if response is None:
                return None
            await message.channel.send(response)



    client.run(config['TOKEN'])

if __name__ == "__main__":
    run_discord_bot()