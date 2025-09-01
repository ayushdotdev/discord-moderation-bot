import os 
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import sqlite3

global_rep = sqlite3.connect('databases/globalrep.db')
config = sqlite3.connect('databases/serverconfig.db')

global_rep_cursor = global_rep.cursor()
config_cursor = config.cursor()

global_rep_cursor.execute("""
CREATE TABLE IF NOT EXISTS reputation(
  user_id INTEGER,
  guild_id INTEGER,
  warnings INTEGER DEFAULT 0,
  kicks INTEGER DEFAULT 0,
  bans INTEGER DEFAULT 0,
  mutes INTEGER DEFAULT 0,
  PRIMARY KEY(user_id,guild_id))
  """)
global_rep.commit()

config_cursor.execute("""
CREATE TABLE IF NOT EXISTS config(
  server_id INTEGER PRIMARY KEY,
  server_prefix TEXT DEFAULT '!',
  modlog_channel INTEGER
)
""")
config.commit()

def initialize_config(guild_id):
    config_cursor.execute("""
        INSERT OR IGNORE INTO config(server_id)
        VALUES (?)
    """, (guild_id,))
    config.commit()



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
  await bot.change_presence(
  activity = nextcord.Game(name = '!help')
  )

@bot.event
async def on_guild_join(guild):
    initialize_config(guild.id)
    
    print(f"Initialized database entries for guild: {guild.name} ({guild.id})")

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
if __name__ == '__main__':
  for i in cmds:
    bot.load_extension(i)


  bot.run(token)