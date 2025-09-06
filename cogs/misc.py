import nextcord
from nextcord.ext import commands
from nextcord import ButtonStyle

class misc(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command(name = "ping", help = "Check latency of the bot")
  async def ping(self,ctx):
    latent = round(self.bot.latency * 1000)
    await ctx.send(f"Pong! Latency {latent} ms")

  @commands.command(name = "invite", help = "Get an invite link for the bot")
  async def invite(self,ctx):
    view = nextcord.ui.View()
    button = nextcord.ui.Button(
      label="Invite Me 🚀", 
      style=ButtonStyle.link, 
      url = "https://discord.com/oauth2/authorize?client_id=1133450786895044688&permissions=8&integration_type=0&scope=bot"
      )
    view.add_item(button)
    await ctx.send(embed = nextcord.Embed(
      color = 0xff00c8,
      description = "Thank you for your consideration\nClick the button to invite me:\n"
      ),view = view)

def setup(bot):
  bot.add_cog(misc(bot))