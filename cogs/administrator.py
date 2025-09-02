import nextcord
from nextcord.ext import commands
from main import config, config_cursor

class admin(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command(name = "setprefix" , aliases = ["prefix"])
  @commands.has_permissions(administrator = True)
  async def setprefix(self,ctx,*,prf: str):
    config_cursor.execute("""
    UPDATE config
    SET server_prefix = ?
    WHERE server_id = ?
    """,(prf,ctx.guild.id))
    config.commit()
    
    await ctx.send(embed = nextcord.Embed(
      color = 0x48a860,
      description = f"<:zaroSucces:1411668840181534851> **Server prefix changed to {prf}**"
      ))
      
def setup(bot):
  bot = bot.add_cog(admin(bot))