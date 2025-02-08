import json
import discord
from discord.ext import commands
from src.config import user_default_models, USER_MODELS_FILE
from src.utils.model_utils import get_available_models
import asyncio

@commands.command(name='setmodel')
async def set_model(ctx):
    user_id = str(ctx.author.id)
    models = get_available_models()

    if not models:
        await ctx.send("Could not retrieve the list of available models.")
        return

    models = [model for model in models if model.strip().lower() != "name"]

    await ctx.send("Available models:\n" + '\n'.join(f"{idx + 1}) {model}" for idx, model in enumerate(models)))

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    while True:
        try:
            reply = await ctx.bot.wait_for('message', check=check, timeout=60)
            if not reply.content.isdigit():
                await ctx.send("❌ Invalid input. Please enter a number corresponding to the list.")
                continue

            selected_index = int(reply.content.strip()) - 1

            if selected_index < 0 or selected_index >= len(models):
                await ctx.send("❌ Invalid selection. Please enter a valid number from the list.")
                continue

            selected_model = models[selected_index]

            user_default_models[user_id] = selected_model

            with open(USER_MODELS_FILE, 'w', encoding='utf-8') as f:
                json.dump(user_default_models, f)

            await ctx.send(f"✅ Your default model has been set to `{selected_model}`.")
            break

        except asyncio.TimeoutError:
            await ctx.send("❌ You took too long to respond. Please use `//setmodel` again.")
            break
        except Exception as e:
            await ctx.send(f"❌ An error occurred: {str(e)}")
            break
