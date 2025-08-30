import os 
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
if __name__ == '__main__':
  bot.run(token)