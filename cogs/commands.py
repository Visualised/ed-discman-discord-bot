from discord.ext import commands
from discord.commands import slash_command
from data.constants import GUILD_IDS


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=GUILD_IDS, name="work", description="Checks to see if I am online")
    async def work(self, ctx):
        await ctx.respond(f"I am working! \n\nLatency: {self.bot.latency * 1000} ms.")

    @slash_command(guild_ids=GUILD_IDS, name="to_uppercase", description="Write your message in uppercase")
    async def reply_in_uppercase(self, ctx, message: str):
        await ctx.respond(f"{message.upper()}")


def setup(bot):
    bot.add_cog(Commands(bot))
