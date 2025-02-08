import discord
import os
# import asyncio
# import time
from discord.ext import commands
from dotenv import load_dotenv
from src.commands.facts import facts
from src.commands.install import install_model
from src.commands.setmodel import set_model
from src.commands.help import help_command
from src.commands.exit import exit_conversation
from src.config import conversation_history, BASE_RESPONSE_DIR

load_dotenv()

GUILD_ID = os.getenv("DISCORD_GUILD_ID", 0)
DISCORD_CHANNEL_NAME = os.getenv("DISCORD_CHANNEL_NAME", "file-indexer")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="//", intents=intents)

awaiting_input = set()

@bot.event
async def on_ready():
    print(f"✅ {bot.user.name} has connected to Discord!")
    
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    user_id = str(message.author.id)

    if user_id in awaiting_input:
        awaiting_input.remove(user_id)  
        return

    if message.content.startswith("//"):
        command = message.content.split()[0]  
        if command in ["//setmodel", "//install"]:
            awaiting_input.add(user_id)  

        await bot.process_commands(message)
        return

    if user_id in conversation_history["active"]:
        ctx = await bot.get_context(message)
        await facts(ctx, message=message.content)
        return

    await bot.process_commands(message)

bot.add_command(facts)
bot.add_command(install_model)
bot.add_command(set_model)
bot.add_command(help_command)
bot.add_command(exit_conversation)

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
