import discord
from discord.ext import commands

@commands.command(name='bothelp')
async def help_command(ctx):
    help_text = """
**Available Commands:**

- `//ask [message]` : Ask general questions or request information.
- `//setmodel` : Set your default model from the list of available models.
- `//install [model_name]` : Install a new model by specifying its name.
- `//bothelp` : Display this help message.

**Usage Examples:**
- `//ask What is the capital of France?`
- `//install llama3.2:1b`

*Note:* You can set a default model using `//setmodel` to customize the AI model that generates your responses.
"""
    await ctx.send(help_text)
