import nextcord
from nextcord.ext import commands
import datetime

class moderation(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    
    
# kick command starts
  @commands.command(name = 'kick', aliases = ["k"])
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
  # kick command ends
   
  #ban command starts
  @commands.command(name = 'ban', aliases = ["b", "bn"])
  @commands.has_permissions(ban_members = True)
  async def ban(self,ctx, member: nextcord.Member, *,reason = "No reason provided"):
    if member == ctx.author or member == ctx.guild.me:
      return await ctx.send(embed = nextcord.Embed(
        color = 0xed2939,
        description = f"<:zaroError:1411668741053349908> **_I cannot ban that user._**"
        ))
          
    if member.top_role >= ctx.guild.me.top_role:
      return await ctx.send(embed = nextcord.Embed(
        color = 0xed2939,
        description = f"<:zaroError:1411668741053349908> **_My role isn't high enough to moderate this user. Move me role up above other roles._**"
        ))
        
    try:
      embedban = nextcord.Embed(
        title = f"Banned from {ctx.guild.name}",
        description = f"You have been **banned** from **{ctx.guild}** \n\n**Reason:** \n{reason}",
        color = 0xff2400
      )
      await member.send(embed = embedban)
    except:
      pass
    await member.ban(reason = reason)
    embedone = nextcord.Embed(
      color = 0x48a860,
      description = f"<:zaroSucces:1411668840181534851> **{member} was banned**"
      )
    await ctx.send(embed = embedone)
    
  @ban.error
  async def ban_error(self,ctx,error):
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
  # ban command ends
      
  # softban command starts
  @commands.command(name = 'softban', aliases = ["sb", "sbn"])
  @commands.has_permissions(ban_members = True)
  async def softban(self,ctx, member: nextcord.Member, *,reason = "No reason provided"):
    if member == ctx.author or member == ctx.guild.me:
      return await ctx.send(embed = nextcord.Embed(
        color = 0xed2939,
        description = f"<:zaroError:1411668741053349908> **_I cannot ban that user._**"
        ))
          
    if member.top_role >= ctx.guild.me.top_role:
      return await ctx.send(embed = nextcord.Embed(
        color = 0xed2939,
        description = f"<:zaroError:1411668741053349908> **_My role isn't high enough to moderate this user. Move me role up above other roles._**"
        ))
        
    try:
      inviter = await ctx.channel.create_invite()
      embedban = nextcord.Embed(
        title = f"SoftBanned from {ctx.guild.name}",
        description = f"You have been **softbanned** from **{ctx.guild}** \n\n**Reason:** \n{reason}\nHere's the link to join again\n{inviter}",
        color = 0xff2400
      )
      await member.send(embed = embedban)
    except:
      pass
    await member.ban(reason = reason)
    await member.unban()
    embedone = nextcord.Embed(
      color = 0x48a860,
      description = f"<:zaroSucces:1411668840181534851> **{member} was softbanned**"
      )
    await ctx.send(embed = embedone)
    
  @softban.error
  async def ban_error(self,ctx,error):
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
      
  # softban command ends 
      
  # mute command starts
  @commands.command(name = "mute", aliases = ['m', 'timeout','tm'])
  @commands.has_permissions(moderate_members = True)
  async def mute(self,ctx,member: nextcord.Member,duration: int, *, reason):
    if member == ctx.author or member == ctx.guild.me:
      return await ctx.send(embed = nextcord.Embed(
        color = 0xed2939,
        description = f"<:zaroError:1411668741053349908> **_I cannot mute that user._**"
        ))
    if member.top_role >= ctx.guild.me.top_role:
      return await ctx.send(embed = nextcord.Embed(
        color = 0xed2939,
        description = f"<:zaroError:1411668741053349908> **_My role isn't high enough to moderate this user. Move me role up above other roles._**"
        ))
    minutes = datetime.timedelta(minutes = duration)
    await member.edit(timeout=nextcord.utils.utcnow() + minutes)
    await ctx.send(embed = nextcord.Embed(
      color = 0x48a860,
      description = f"<:zaroSucces:1411668840181534851> **{member} was mute for {minutes} minutes.**"
      ))
  
  @mute.error
  async def mute_error(self,ctx,error):
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
      
  #mute command ends
   
   
  # warn command starts 
  @commands.command(name="warn", aliases = ["w"])
  @commands.has_permissions(moderate_members = True)
  async def warn(self,ctx, member: nextcord.Member, *, reason):
    if member.bot:
      return await ctx.send(embed = nextcord.Embed(
        color = 0xed2939,
        description = f"<:zaroError:1411668741053349908> **_You cannot warn a bot.._**"
        ))
    if member == ctx.author or member == ctx.guild.me:
      return await ctx.send(embed = nextcord.Embed(
        color = 0xed2939,
        description = f"<:zaroError:1411668741053349908> **_I cannot warn that user._**"
        ))
    if member.top_role >= ctx.guild.me.top_role:
      return await ctx.send(embed = nextcord.Embed(
        color = 0xed2939,
        description = f"<:zaroError:1411668741053349908> **_My role isn't high enough to moderate this user. Move me role up above other roles._**"
        ))
    try:
      await member.send(embed = nextcord.Embed(
        title = f"Warned in {ctx.guild.name}",
        description = f"You have been **warned** in **{ctx.guild}** \n\n**Reason:** \n{reason}",
        color = 0xff2400
        ))
    except:
      pass
    await ctx.send(embed = nextcord.Embed(
      color = 0x48a860,
      description = f"<:zaroSucces:1411668840181534851> **{member} was warned**"
      ))
    
  @warn.error
  async def warn_error(self,ctx,error):
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
    
  # warn command ends
def setup(bot):
  bot = bot.add_cog(moderation(bot))