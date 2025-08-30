import os 
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

cmds = [
  "cogs.moderation"
  ]

intents = nextcord.Intents.default()
intents.message_content = True

def get_prefix(bot, message):
    return commands.when_mentioned_or("!")(bot, message)

bot = commands.Bot(command_prefix=get_prefix, intents=intents)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
if __name__ == '__main__':
  for i in cmds:
    bot.load_extension(i)


  bot.run(token)