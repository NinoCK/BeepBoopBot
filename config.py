import os
import json
import csv
from dotenv import load_dotenv

load_dotenv()

BASE_RESPONSE_DIR = "responses"
LOG_FILE = 'conversation_log.csv'
USER_MODELS_FILE = 'user_default_models.json'

os.makedirs(BASE_RESPONSE_DIR, exist_ok=True)

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Timestamp', 'Command', 'User ID', 'Response Folder'])

if os.path.exists(USER_MODELS_FILE):
    with open(USER_MODELS_FILE, 'r', encoding='utf-8') as f:
        user_default_models = json.load(f)
else:
    user_default_models = {}

conversation_history = {
    "facts": {},
    "global_context": {},
    "active": {},
    "folders": {} 
}
