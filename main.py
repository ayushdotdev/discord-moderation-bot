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
  modlog_channel INTEGER,
  invitelog_channel INTEGER
)
""")
config.commit()

def initialize_config(guild_id):
    config_cursor.execute("""
        INSERT OR IGNORE INTO config(server_id)
        VALUES (?)
    """, (guild_id,))
    config.commit()


# cog list
cmds = [
  "cogs.moderation",
  "cogs.administrator",
  "cogs.misc",
  "cogs.general"
  ]

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

def get_prefix(bot, message):
    config_cursor.execute("""
      SELECT server_prefix FROM config WHERE server_id = ?
      """,(message.guild.id,))
    row = config_cursor.fetchone()
    return commands.when_mentioned_or(row[0])(bot, message)

bot = commands.Bot(command_prefix=get_prefix, intents=intents, help_command = None)

@bot.event
async def on_member_join(member):
  config_cursor.execute("""
    SELECT invitelog_channel
    FROM config
    WHERE server_id = ?
    """,(member.guild.id,))
  invite_chan = config_cursor.fetchone()
  if invite_chan and invite_chan[0]:
    channel = member.guild.get_channel(invite_chan[0])
    if channel:
      global_rep_cursor.execute("""
      SELECT SUM(kicks),SUM(bans),SUM(mutes), SUM(warnings)
      FROM reputation
      WHERE user_id = ?
      """,(member.id,))
      result = global_rep_cursor.fetchone()
      if result:
        total_kicks, total_bans, total_mutes, total_warnings = result
        total_kicks = total_kicks or 0
        total_bans = total_bans or 0
        total_mutes = total_mutes or 0
        total_warnings = total_warnings or 0
        
        await channel.send(embed = nextcord.Embed(
          color = 0x242422,
          description = f"{member.mention} just joined. They have received {total_bans} bans, {total_kicks} kicks, {total_warnings} warnings, and {total_mutes} mutes across all the servers I'm in."
          ))

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')
  await bot.change_presence(
  activity = nextcord.Game(name = '!help')
  )
  for guild in bot.guilds:
    initialize_config(guild.id)
    print("Done initialisation")

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