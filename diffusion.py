# import os
# # os.environ[TF_CPP_MIN_LOG_LEVEL] = '3'
# import discord
# import uuid
# import torch
# import torch
# from diffusers import StableDiffusion3Pipeline

# pipe = StableDiffusion3Pipeline.from_pretrained("stabilityai/stable-diffusion-3.5-medium", torch_dtype=torch.bfloat16)
# pipe = pipe.to("cuda")


# TOKEN = open('TOKEN', 'r').read()

# intents = discord.Intents.default()
# intents.messages = True
# intents.message_content = True

# client = discord.Client(intents=intents)

# @client.event
# async def on_connect():
#     print(f"Connected to Discord as {client.user}")

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('//generate '):
#         await message.channel.send("Generating image...")

#         file = f"{uuid.uuid4()}.png"

#         image = pipe(
#         message.content[5: ],
#         num_inference_steps=40,
#         guidance_scale=4.5,
#         ).images[0]
#         image.save("capybara.png")

#         with open(file, 'rb') as f:
#             picture = discord.File(f)
#             await message.channel.send(file=picture)
        
#         os.remove(file)

# client.run(TOKEN)