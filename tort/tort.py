import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def SUMMON(self, user):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("SUMMON THE GODS!")
        await self.bot.say("SUMMON THE GODS!")
        await self.bot.say("SUMMON THE GODS!")
        await self.bot.say("SUMMON THE GODS!")
        await self.bot.say("SUMMON THE GODS!")
        await self.bot.say("SUMMON THE GODS!")
        await self.bot.say("SUMMON THE GODS!")

def setup(bot):
    bot.add_cog(Mycog(bot))
