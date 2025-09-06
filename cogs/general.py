import nextcord
from nextcord.ext import commands
from nextcord import ButtonStyle
from main import config_cursor

class general(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command(name = 'help')
  async def help(self,ctx,*, cmd:str = None):
    config_cursor.execute("""
    SELECT server_prefix
    FROM config
    WHERE server_id = ?
    """,(ctx.guild.id,))
    row = config_cursor.fetchone()
    prefix = row[0]
    view = nextcord.ui.View()
    prev_btn = nextcord.ui.Button(
      label = "◀️",
      style = ButtonStyle.primary
      )
    next_btn = nextcord.ui.Button(
      label = "▶️",
      style = ButtonStyle.primary
      )
    view.add_item(prev_btn)
    view.add_item(next_btn)
    pages = []
    for cog_name,cog_object in self.bot.cogs.items():
      page = nextcord.Embed(
        title = f'*{cog_name} Commands*',
        color = 0xff00c8
        )
      for cmd in cog_object.get_commands():
        page.add_field(
          name = f'{prefix}{cmd.name}',
          value = cmd.help or "No description provided"
          )
      pages.append(page)
    current_page = 0
    async def prev_callback(interaction: nextcord.Interaction):
      nonlocal current_page
      current_page = max(current_page - 1,0)
      await interaction.response.edit_message(embed = pages[current_page],view = view)
    async def next_callback(interaction: nextcord.Interaction):
      nonlocal current_page
      current_page = max(current_page + 1,0)
      await interaction.response.edit_message(embed = pages[current_page],view = view)
    prev_btn.callback = prev_callback
    next_btn.callback = next_callback
    await ctx.send(embed = pages[current_page],view = view)
    
def setup(bot):
  bot.add_cog(general(bot))