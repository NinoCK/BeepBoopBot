
```markdown
# BeepBoopBot 🤖

BeepBoopBot is a Discord bot that provides AI-powered coding assistance, general knowledge Q&A, and file processing for enhanced interactions.

## 🚀 Features

- 🧑‍💻 **Code Assistance**: Get help with coding problems using AI-powered models.
- 📚 **Facts & Knowledge**: Ask general questions and receive informative responses.
- 🔧 **Model Selection**: Choose your preferred AI model for personalized responses.
- 📥 **Model Installation**: Install new AI models directly through the bot.

## 🛠 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/beepboopbot.git
cd beepboopbot
```

### 2️⃣ Install Dependencies
Ensure you have Python 3.8+ installed. Then run:
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add:
```
DISCORD_BOT_TOKEN=your_discord_bot_token
```

### 4️⃣ Run the Bot
```sh
python main.py
```

## 📜 Commands

| Command           | Description |
|------------------|-------------|
| `//ask [query]` | Ask the model. |
| `//setmodel` | Choose your default AI model. |
| `//install [model]` | Install a new AI model. |
| `//bothelp` | Display help information. |

## 🤖 Tech Stack
- **Python**
- **Discord.py**
- **Ollama AI Models**
- **PyPDF2 (for PDF processing)**
- **dotenv (for environment variables)**

## 📌 Contributing
Contributions are welcome! Feel free to fork, submit issues, or make pull requests.

## 🔗 License
This project is licensed under the MIT License.
