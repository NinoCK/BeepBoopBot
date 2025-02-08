from discord.ext import commands
from src.config import conversation_history

@commands.command(name='exit')

async def exit_conversation(ctx):
    user_id = str(ctx.author.id)

    if user_id in conversation_history["active"]:
        del conversation_history["active"][user_id]  
        conversation_history["folders"].pop(user_id, None)  
        conversation_history["facts"].pop(user_id, None) 
        await ctx.send("You have exited the conversation mode. Your next question will start a new conversation.")
    else:
        await ctx.send("You are not in an active conversation.")
