# imports
import os

import discord
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# API URL
url = "https://leetcode-api-pied.vercel.app/random"

# Discord intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # !random command
    if message.content == "!random":
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            data = response.json()
            id = data["frontend_id"]
            title = data["title"]
            difficulty = data["difficulty"]
            leetcode_url = data["url"]
            leetcode_message = (
                "*straightens tie with one precise motion, sits perfectly still*\n"
                f"**LeetCode Problem #{id} - {title}**\n"
                f"**Difficulty:** {difficulty}\n"
                f"**Link:** {leetcode_url}\n"
                "*speaks in a calm, measured tone*\n"
                "> \"I've just posted today's coding challenge. All members should attempt this problem now.\"\n"
                "*adjusts monitor slightly for optimal viewing angle*\n"
                "> \"The solution should be submitted by **23:59 tonight**. Late submissions won't be accepted—just as I don't tolerate disorder or imperfection.\"\n"
                "*taps keyboard once, sending the message with perfect precision.*"
            )
            await message.channel.send(leetcode_message)
        except requests.exceptions.RequestException as e:
            print(f"API Request failed: {e}")
            await message.channel.send("❌ Failed to fetch a random LeetCode problem.")

    # Any other message
    else:
        await message.channel.send(
            "My name is Yoshikage Kira. I'm 33 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married. I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest. I don't smoke, but I occasionally drink. I'm in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning. I was told there were no issues at my last check-up. I'm trying to explain that I'm a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn't lose to anyone."
        )


client.run(TOKEN)
