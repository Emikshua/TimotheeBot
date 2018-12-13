import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def generateorder(self):
        """This does stuff!"""

        #Your code will go here
<<<<<<< Updated upstream
        await self.bot.say("Generating questioner order. Please wait... ")
=======
        await self.bot.say("Generating order. Please wait...")
        await self.bot.
>>>>>>> Stashed changes

def setup(bot):
    bot.add_cog(Mycog(bot))
