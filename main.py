import os
from src.bot import bot

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))