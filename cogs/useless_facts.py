from discord.ext import commands
from discord.commands import slash_command
from data.constants import GUILD_IDS
from services.useless_facts_service import UselessFactsService


class UselessFacts(commands.Cog):
    description_string = "Returns useless facts. Supports English (en) and German (de) language"

    @slash_command(guild_ids=GUILD_IDS, name="get_useless_fact", description=description_string)
    async def get_useless_fact(self, ctx, language: str):
        await ctx.defer()
        useless_fact = UselessFactsService.get_useless_fact(language)
        await ctx.followup.send(useless_fact)


def setup(bot):
    bot.add_cog(UselessFacts(bot))
