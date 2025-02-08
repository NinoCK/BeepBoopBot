import os
import PyPDF2
from discord.ext import commands # I needed it before, no harm keeping it
from src.config import conversation_history, BASE_RESPONSE_DIR

async def process_uploaded_pdf(message, attachment):

    user_id = str(message.author.id)
    file_name = attachment.filename
    user_folder = conversation_history["folders"].get(user_id)

    if user_id not in conversation_history["active"]:
        await message.channel.send("Start a conversation using `//ask` before uploading a file.")
        return

    if not user_folder:
        await message.channel.send("No active conversation folder found. Please start with `//ask`.")
        return
    
    file_path = os.path.join(user_folder, file_name)

    try:
        await attachment.save(file_path)

        with open(file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            pdf_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

        # Need to limit the text size,tends to overload memory(at least mine?)
        max_characters = 4000
        pdf_text = pdf_text[:max_characters] + "\n... [Truncated]" if len(pdf_text) > max_characters else pdf_text

        pdf_context = f"Additional knowledge from uploaded PDF:\n{pdf_text}"

        if user_id in conversation_history["facts"]:
            conversation_history["facts"][user_id].insert(1, {'role': 'system', 'content': pdf_context})
        else:
            conversation_history["facts"][user_id] = [{'role': 'system', 'content': pdf_context}]

        await message.channel.send(f"✅ `{file_name}` has been processed and stored. You can now ask a question using this document as context.")

    except Exception as e:
        await message.channel.send(f"❌ Error processing `{file_name}`: {e}")
