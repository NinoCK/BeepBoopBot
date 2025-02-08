


# import discord
# from discord.ext import commands
# import torch
# from diffusers import StableDiffusion3Pipeline
# import os
# from huggingface_hub import login
# from dotenv import load_dotenv

# load_dotenv()

# HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
# login(HUGGINGFACE_TOKEN)

# # Load Stable Diffusion model on CPU instead of GPU
# pipe = StableDiffusion3Pipeline.from_pretrained(
#     "stabilityai/stable-diffusion-3.5-medium",
#     torch_dtype=torch.float32,  # Use float32 for CPU
#     token=HUGGINGFACE_TOKEN
# )

# device = "cuda"
# pipe = pipe.to(device)

# @commands.command(name="generate")
# async def generate(ctx, *, prompt: str):
#     """Generate an image using Stable Diffusion 3.5 on CPU and send it to Discord"""

#     await ctx.send(f"⚠ Generating image on **CPU** (this will take some time)...\nGenerating: `{prompt}`")

#     try:
#         # Generate Image (CPU is much slower, so reduce quality slightly)
#         image = pipe(prompt, num_inference_steps=20, guidance_scale=3.5, height=320, width=320).images[0]

#         # Save Image
#         image_path = "generated_image.png"
#         image.save(image_path)

#         # Send Image to Discord
#         with open(image_path, "rb") as file:
#             discord_file = discord.File(file, filename="generated_image.png")
#             await ctx.send(file=discord_file)

#         # Cleanup
#         os.remove(image_path)

#     except Exception as e:
#         await ctx.send(f"❌ An error occurred: {e}")
