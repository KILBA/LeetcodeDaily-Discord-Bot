# LeetCode Daily Discord Bot

A Discord bot that automatically posts a LeetCode daily challenge problem every day.

---

## Setup Guide

### Prerequisites

- Python 3.10 or higher
- A Discord account and a server where you have permission to add bots

### Step 1: Create a Discord Bot Application

1. Go to [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application**, give it a name, and click **Create**.
3. Go to the **Bot** tab and click **Add Bot**.
4. Under **Privileged Gateway Intents**, enable:
   - **Message Content Intent**
5. Copy the **Bot Token** (keep this secret).
6. Go to the **OAuth2 > URL Generator** tab, select scopes: `bot`.
7. Under **Bot Permissions**, select:
   - Send Messages
   - Embed Links
   - Read Message History
8. Copy the generated URL and open it in your browser to invite the bot to your server.
9. Copy the **Channel ID** of the channel where you want the bot to post:
   - Enable Developer Mode in Discord (Settings > Advanced > Developer Mode).
   - Right-click the channel name and select **Copy Channel ID**.

### Step 2: Clone and Install

```bash
git clone https://github.com/your-username/LeetcodeDaily-Discord-Bot.git
cd LeetcodeDaily-Discord-Bot
python3 -m venv bot-env
source bot-env/bin/activate   # Linux/Mac
# bot-env\Scripts\activate    # Windows
pip install -r requirements.txt
```

### Step 3: Configure Environment

Create a `.env` file in the project root:

```
DISCORD_TOKEN=your-bot-token-here
CHANNEL_ID=your-channel-id-here
```

### Step 4: Run the Bot

```bash
python main.py
```
