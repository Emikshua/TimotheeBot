import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def generateorder(self, user):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("Generating the order! Please wait...")
        wait(10)
        await self.bot.say("Fatal Error. Check logs.")
def setup(bot):
    bot.add_cog(Mycog(bot))
