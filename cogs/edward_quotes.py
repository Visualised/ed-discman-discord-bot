import random
from discord.ext import commands
from discord.commands import slash_command
from data.constants import GUILD_IDS


class RandomEdwardQuotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=GUILD_IDS, name="edward_quote", description="Send random edward quote")
    async def send_random_quote(self, ctx):
        with open("edward_quotes.txt", encoding="UTF-8") as f:
            lines = f.read().splitlines()
        await ctx.respond(random.choice(lines))


def setup(bot):
    bot.add_cog(RandomEdwardQuotes(bot))
