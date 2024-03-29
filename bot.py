import discord
from discord.ext import commands
from datetime import datetime
import asyncio
from discord import app_commands, Client, Message
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
    #bot starts running!r
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
            
            elif isinstance(response,discord.Embed):
                await message.channel.send(embed = response)

            else: await message.channel.send(response)

    @client.event
    async def embed(ctx, *, message):
        embed = discord.Embed()
    
    # Check if the command issuer has a role with color
        role = discord.utils.get(ctx.guild.roles)
        if role:
                embed.colour = role.color
        else:
        # Default color if role color not found
            embed.colour = discord.Color.default()

        await ctx.send(embed=embed)


    client.run(config['TOKEN'])

if __name__ == "__main__":
    run_discord_bot()