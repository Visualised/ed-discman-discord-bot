from discord.ext import commands
from discord.commands import slash_command
from data.constants import GUILD_IDS
from services.url_shortener_service import UrlShortenerService


class UrlShortener(commands.Cog):
    @slash_command(guild_ids=GUILD_IDS, name="url_shortener", description="Returns shortened URL.")
    async def url_shortener(self, ctx, url_to_shorten: str):
        await ctx.defer()
        shortened_url = UrlShortenerService.shorten_url(url_to_shorten)
        await ctx.followup.send(f"Shortened URL: {shortened_url}")


def setup(bot):
    bot.add_cog(UrlShortener(bot))
