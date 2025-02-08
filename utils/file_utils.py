import os
import csv
from datetime import datetime
from src.config import LOG_FILE

def save_response_to_file(command, user_id, user_message, bot_response, folder_path):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    markdown_file = os.path.join(folder_path, f"{timestamp}.md")

    with open(markdown_file, 'w', encoding='utf-8') as file:
        file.write(f"# {command.capitalize()} Response\n\n")
        file.write(f"**User ID**: {user_id}\n\n")
        file.write(f"**Timestamp**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        file.write(f"**User Question**:\n\n{user_message}\n\n")
        file.write(f"**Bot Response**:\n\n{bot_response}\n")

    with open(LOG_FILE, 'a', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), command, user_id, markdown_file])
