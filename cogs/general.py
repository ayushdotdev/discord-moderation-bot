import nextcord
from nextcord.ext import commands
from nextcord import ButtonStyle
from main import config_cursor

class help(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command(name = 'help')
  async def help(self,ctx,*, cmd:str):
    config_cursor.execute("""
    SELECT server_prefix
    FROM config
    WHERE server_id = ?
    """,(ctx.guild.id))
    row = config_cursor.fetchone()
    prefix = row[0]
    view = nextcord.ui.View()
    view.add_item(nextcord.ui.Button(
      label = "◀️",
      style = ButtonStyle.primary
      ))
    view.add_item(nextcord.ui.Button(
      label = "▶️",
      style = ButtonStyle.primary
      ))
    pages = []
    for cog_name,cog_object in self.bot.cogs.items:
      page = nextcord.Embed(
        title = f'*{cog_name} Commands*'
        color = 0xff00c8
        )
      for cmd in cog_object.get_commands():
        page.add_field(
          name = f'{prefix}{cmd.name}'
          )