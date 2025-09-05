import nextcord
from nextcord.ext import commands

class misc(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command(name = "ping")
  async def ping(self,ctx):
    latent = round(self.bot.latency * 1000)
    await ctx.send(f"Pong! Latency {latent} ms")

  @commands.command(name = "invite")
  async def invite(self,ctx):
    await ctx.send(embed = nextcord.Embed(
      color = 0xff00c8,
      description = ""
      ))

def setup(bot):
  bot.add_cog(misc(bot))