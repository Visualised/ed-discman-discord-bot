from discord.ext import commands, tasks
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from data.constants import TIKTOK_NOTIFICATIONS_CHANNEL_ID


class TiktokNotifications(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.new_tiktok_video_notification.start()

    @staticmethod
    def initialize_browser_driver():
        browser_options = Options()
        browser_options.headless = True
        webdriver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=webdriver_service, options=browser_options)
        driver.get("https://www.tiktok.com/@eddiscman")

        return driver

    @tasks.loop(hours=1)
    async def new_tiktok_video_notification(self):
        driver = self.initialize_browser_driver()
        channel = self.bot.get_channel(TIKTOK_NOTIFICATIONS_CHANNEL_ID)

        elements = driver.find_elements(By.CSS_SELECTOR, "div[class*='DivWrapper']>a")
        latest_video_link = elements[0].get_attribute("href")

        with open("latest_video_link.txt", "r+", encoding="UTF-8") as f:
            file_content = f.read()
            is_latest_video = True if file_content != latest_video_link else False

            if is_latest_video:
                f.seek(0)
                f.truncate()
                f.write(latest_video_link)
                await channel.send(f"Nowy filmik na tiktoku! Link: {latest_video_link}")

        driver.close()


def setup(bot):
    bot.add_cog(TiktokNotifications(bot))
