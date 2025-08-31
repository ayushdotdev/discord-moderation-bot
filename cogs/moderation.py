import nextcord
from nextcord.ext import commands

class moderation(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    
    
# kick command starts
  @commands.command(name = 'kick')
  @commands.has_permissions(kick_members = True)
  async def kick(self,ctx, member: nextcord.Member, *,reason = "No reason provided"):
    if member == ctx.author or member == ctx.guild.me:
      return await ctx.send(embed = nextcord.Embed(
        color = 0xed2939,
        description = f"<:zaroError:1411668741053349908> **_I cannot kick that user._**"
        ))
          
    if member.top_role >= ctx.guild.me.top_role:
      return await ctx.send(embed = nextcord.Embed(
        color = 0xed2939,
        description = f"<:zaroError:1411668741053349908> **_My role isn't high enough to moderate this user. Move me role up above other roles._**"
        ))
        
    try:
      embedkick = nextcord.Embed(
        title = f"Kicked from {ctx.guild.name}",
        description = f"You have been **kicked** from **{ctx.guild}** \n\n**Reason:** \n{reason}",
        color = 0xe24c00
      )
      await member.send(embed = embedkick)
    except:
      pass
    await member.kick(reason = reason)
    embedone = nextcord.Embed(
      color = 0x48a860,
      description = f"<:zaroSucces:1411668840181534851> **{member} was kicked**"
      )
    await ctx.send(embed = embedone)
    
  @kick.error
  async def kick_error(self,ctx,error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(embed = nextcord.Embed(
        color = 0xed2939,
        description = f"<:zaroError:1411668741053349908> **_You don't have permissions to use this command._**"
        ))
    elif isinstance(error, commands.BadArgument):
      await ctx.send(embed = nextcord.Embed(
        color = 0xed2939,
        description = f"<:zaroError:1411668741053349908> **_I cannot find this user._**"
        ))
    else:
      raise error
def setup(bot):
  bot = bot.add_cog(moderation(bot))