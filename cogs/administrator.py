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
      
  @commands.command(name="setmodlog-channel")
  @commands.has_permissions(administrator = True)
  async def modlogger(self,ctx,channel: nextcord.TextChannel):
    config_cursor.execute("""
    UPDATE config
    SET modlog_channel = ?
    WHERE server_id = ?
    
    """,(channel.id,ctx.guild.id))
    config.commit()
    
    await ctx.send(embed = nextcord.Embed(
      color = 0x48a860,
      description = f"<:zaroSucces:1411668840181534851> **Mod Log channel set to {channel.mention}**"
      ))
      
  @commands.command(name="setinvitelog")
  @commands.has_permissions(administrator = True)
  async def invitelogger(self,ctx,channel: nextcord.TextChannel):
    config_cursor.execute("""
    UPDATE config
    SET invitelog_channel = ?
    WHERE server_id = ?
    
    """,(channel.id,ctx.guild.id))
    config.commit()
    
    await ctx.send(embed = nextcord.Embed(
      color = 0x48a860,
      description = f"<:zaroSucces:1411668840181534851> **Invite Log channel set to {channel.mention}**"
      ))
def setup(bot):
  bot = bot.add_cog(admin(bot))