import discord
import time
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def generateorder(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("Generating the order! Please wait...")
        time.sleep(5)
        await self.bot.say("Miles, Sebastian, Aidan, Steph")

    async def tstart(self):

        await self.bot.say("Starting game. Please wait")
        time.sleep(5)
        await self.bot.say("Game can not be started. Minimum of 4 players is needed. Current amount of players: 1000000000")
        await self.bot.say("FATAL ERROR. PLEASE RESTART NOW")
def setup(bot):
    bot.add_cog(Mycog(bot))
