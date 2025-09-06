import nextcord
from nextcord.ext import commands
import datetime
from main import global_rep,global_rep_cursor,config,config_cursor
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
    config_cursor.execute("""
    SELECT modlog_channel
    FROM config
    WHERE server_id = ?
    """,(ctx.guild.id,))
    logger = config_cursor.fetchone()
    if logger and logger[0]:
      chan = ctx.guild.get_channel(logger[0])
      if chan:
        await chan.send(embed = nextcord.Embed(
          color = 0x242422,
          title = "**Member Kicked**",
          description = f"User {member.name} got kicked by {ctx.author.name} for the reason:\n{reason}"
          ))
    global_rep_cursor.execute("""
    INSERT INTO reputation(user_id, guild_id, kicks)
    VALUES (?, ?, 1)
    ON CONFLICT(user_id, guild_id) DO UPDATE SET kicks = kicks + 1
    """, (member.id, ctx.guild.id))
    global_rep.commit()
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
    global_rep_cursor.execute("""
    INSERT INTO reputation(user_id, guild_id, bans)
    VALUES (?, ?, 1)
    ON CONFLICT(user_id, guild_id) DO UPDATE SET bans = bans + 1
    """, (member.id, ctx.guild.id))
    global_rep.commit()
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
        title = f"Softbanned from {ctx.guild.name}",
        description = f"You have been **softbanned** from **{ctx.guild}** \n\n**Reason:** \n{reason}\nHere's the link to join again\n{inviter}",
        color = 0xdd571c
      )
      await member.send(embed = embedban)
    except:
      pass
    await member.ban(reason = reason)
    await member.unban()
    global_rep_cursor.execute("""
    INSERT INTO reputation(user_id, guild_id, kicks)
    VALUES (?, ?, 1)
    ON CONFLICT(user_id, guild_id) DO UPDATE SET kicks = kicks + 1
    """, (member.id, ctx.guild.id))
    global_rep.commit()
    embedone = nextcord.Embed(
      color = 0x48a860,
      description = f"<:zaroSucces:1411668840181534851> **{member} was softbanned**"
      )
    await ctx.send(embed = embedone)
    
  @softban.error
  async def softban_error(self,ctx,error):
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
    global_rep_cursor.execute("""
    INSERT INTO reputation(user_id, guild_id, mutes)
    VALUES (?, ?, 1)
    ON CONFLICT(user_id, guild_id) DO UPDATE SET mutes = mutes + 1
    """, (member.id, ctx.guild.id))
    global_rep.commit()
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
  async def warn(self,ctx, member: nextcord.Member, *, reason = "No reason provided"):
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
        color = 0xdaa520
        ))
    except:
      pass
    await ctx.send(embed = nextcord.Embed(
      color = 0x48a860,
      description = f"<:zaroSucces:1411668840181534851> **{member} was warned**"
      ))
    global_rep_cursor.execute("""
    INSERT INTO reputation(user_id, guild_id, warnings)
    VALUES (?, ?, 1)
    ON CONFLICT(user_id, guild_id) DO UPDATE SET warnings = warnings + 1
    """, (member.id, ctx.guild.id))
    global_rep.commit()
    
    global_rep_cursor.execute("""
    SELECT warnings
    FROM reputation
    WHERE user_id = ? AND guild_id = ?
    """,(member.id,ctx.guild.id))
    wrn = global_rep_cursor.fetchone()
    if wrn[0] == 3:
      await member.kick(reason = "3 warnings")
      await ctx.send(embed = nextcord.Embed(
        color = 0xff00c8,
        description =  f'<:zaroThreat:1412465462129852527> User has been kicked for receiving 3 warnings'
        ))
      try:
        embedkick = nextcord.Embed(
        title = f"Kicked from {ctx.guild.name}",
        description = f"You have been **kicked** from **{ctx.guild}** \n\n**Reason:** \nReceiving 3 warnings",
        color = 0xe24c00
      )
        await member.send(embed = embedkick)
      except:
       pass
    elif wrn[0] == 5:
      await member.ban(reason = f'{wrn[0]} warnings')
      await ctx.send(embed = nextcord.Embed(
        color = 0xff00c8,
        description = f'<:zaroThreat:1412465462129852527> User has been banned for exceeding 3 warnings'
        ))
      try:
        embedkick = nextcord.Embed(
         title = f"Banned from {ctx.guild.name}",
          description = f"You have been **banned** from **{ctx.guild}** \n\n**Reason:** \nReceiving {wrn[0]} warnings",
          color = 0xff2400
      )
        await member.send(embed = embedkick)
      except:
        pass
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