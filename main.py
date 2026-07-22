# imports
import os

import discord
import requests
from requests.api import request
import yaml
from dotenv import load_dotenv
from discord.ext import tasks as discordTasks
from discord.ext import commands
from datetime import datetime as dt

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# API URL
url = "https://leetcode-api-pied.vercel.app/"

with open('config.yaml', 'r') as file:
    configFile = yaml.safe_load(file)

hour = configFile['messageTime']['hour']
minutes = configFile['messageTime']['minutes']
blacklistedDays = [item.lower() for item in configFile['blacklistedDays']]
channelName = configFile['channelName']

# Discord intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
mainChannel = discord.utils.get(client.get_all_channels(), name=channelName)

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
            response = requests.get(url+"random", timeout=5)
            response.raise_for_status()

            data = response.json()
            id = data["frontend_id"]
            title = data["title"]
            difficulty = data["difficulty"]
            leetcode_url = data["url"]
            leetcode_message = (
                "https://klipy.com/gifs/jojo-kira-yoshikage-1\n"
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
            "https://klipy.com/gifs/jojo-kira-yoshikage-1\nMy name is Yoshikage Kira. I'm 33 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married. I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest. I don't smoke, but I occasionally drink. I'm in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning. I was told there were no issues at my last check-up. I'm trying to explain that I'm a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn't lose to anyone."
        )

async def sendQuestions():
    try:
        response = requests.get(url+"daily",timeout=5)
        response.raise_for_status()
        data = response.json()
        id = data["frontend_id"]
        title = data["title"]
        difficulty = data["difficulty"]
        leetcode_url = data["url"]
        kira_message = (
            "https://klipy.com/gifs/jojo-kira-yoshikage-1\n"
            "*straightens tie with practiced precision, ensuring not a single wrinkle remains*\n"
            f"**LeetCode Problem #{id} - {title}**\n"
            f"**Difficulty:** {difficulty}\n"
            f"**Link:** {leetcode_url}\n\n"
            "*regards the server with an expression of polite indifference*\n"
            "> \"Good morning, plebs. While you busy yourselves with your noisy little lives, I've prepared today's LeetCode problem.\"\n\n"
            "*adjusts cufflinks without the slightest wasted movement*\n"
            "> \"Complete it before **23:59 tonight**. A predictable schedule is the foundation of a peaceful existence, and I would prefer this server not descend into unnecessary chaos.\"\n\n"
            "*takes a sip of coffee, unbothered by the passage of time*\n"
            "> \"Whether you solve it elegantly or brute-force your way through it is your concern. I merely expect results.\"\n\n"
            "*briefly glances toward the notifications, mildly disappointed already*\n"
            "> \"Those who fail to submit on time will simply confirm my expectations. Those who succeed may continue living their ordinary lives for another day.\"\n\n"
            "*smooths his tie one final time before pressing Enter with immaculate precision.*"
        )
        await channelName.send(kira_message)
    except requests.exceptions.RequestException as e:
        print(f"API Request failed: {e}")
        await channelName.send("❌ Failed to fetch a random LeetCode problem.")


@discordTasks.loop(minutes=1.0)
async def messageDaily():
    global blacklistedDays
    if dt.now().strftime('%A'). lower() in blacklistedDays:
        return
    if (dt.now().hour == hour) and (dt.now().strftime('%M') == str(minutes)):
        await sendQuestions()

client.run(TOKEN)
