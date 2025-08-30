import nextcord
from nextcord.ext import commands

class moderation(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command(name='hi')
  async def greet(self,ctx):
    await ctx.send('Hello')
    
def setup(bot):
  bot = bot.add_cog(moderation(bot))