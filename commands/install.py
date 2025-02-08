import asyncio
import discord
import logging
from discord.ext import commands

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@commands.command(name='install')
async def install_model(ctx, *, model_name: str = None):
    """
    Handles the installation of models using `ollama pull <model_name>`.
    If the model exists, it downloads it and confirms success.
    If no model name is provided, it prompts the user.
    If the model does not exist, it returns the last error message.
    """
    if not model_name:
        await ctx.send("❌ You must specify a model name to install. Usage: `//install <model_name>`")
        logger.warning("User did not specify a model name for installation.")
        return

    logger.info(f"Received install request for model: {model_name}")
    await ctx.send(f"🔍 Attempting to install model '{model_name}'...")

    try:
        process = await asyncio.create_subprocess_exec(
            'ollama', 'pull', model_name,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()
        stdout_message = stdout.decode().strip()
        stderr_message = stderr.decode().strip()

        if process.returncode == 0 and "success" in stdout_message.lower():
            await ctx.send(f"✅ Model '{model_name}' has been successfully installed.")
            logger.info(f"Model '{model_name}' installed successfully.")
        else:
            error_message = stderr_message.split('\n')[-1] if stderr_message else "Unknown error occurred."
            await ctx.send(f"❌ Failed to install model '{model_name}'. Error: {error_message}")
            logger.error(f"Installation failed for model '{model_name}': {error_message}")
    except asyncio.SubprocessError as e:
        await ctx.send(f"❌ An error occurred while installing the model: {str(e)}")
        logger.exception(f"Subprocess error during installation of model '{model_name}': {str(e)}")
    except Exception as e:
        await ctx.send(f"❌ An unexpected error occurred: {str(e)}")
        logger.exception(f"Unexpected error during installation of model '{model_name}': {str(e)}")
