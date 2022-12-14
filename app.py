import dotenv
import os
import discord

dotenv.load_dotenv()
bot_token = str(os.getenv("TOKEN"))

intent = discord.Intents.default()
intent.message_content = True
intent.members = True
bot = discord.Bot(intents=intent)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}.")


if __name__ == "__main__":
    bot.run(bot_token)
