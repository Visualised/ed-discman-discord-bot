import os
import time
import random
from discord.ext import commands
from data.constants import ROBERT_KUBICA_PICTURES_URLS_FILENAME
from services.google_images_service import GoogleImagesService


class RobertKubicaPictures(commands.Cog):
    @staticmethod
    def is_file_older_than_a_day(filename):
        DAY = 86400
        current_date = time.time()
        file_modification_date = os.path.getmtime(filename)

        if (current_date - file_modification_date) > DAY:
            return True
        else:
            return False

    @commands.Cog.listener()
    async def on_message(self, message: str):
        if "EEEE" in message.content:
            with open(ROBERT_KUBICA_PICTURES_URLS_FILENAME, "a+", encoding="UTF-8") as f:
                f.seek(0)
                images_urls = f.read().splitlines()

                is_file_older_than_a_day = self.is_file_older_than_a_day(ROBERT_KUBICA_PICTURES_URLS_FILENAME)
                does_file_need_updating = True if is_file_older_than_a_day or not images_urls else False

                if does_file_need_updating:
                    google_image_service = GoogleImagesService()
                    pictures_urls_list = google_image_service.get_images_urls("robert kubica śmieszne")
                    google_image_service.save_links_to_file(ROBERT_KUBICA_PICTURES_URLS_FILENAME, pictures_urls_list)
                    images_urls = f.read().splitlines()

                random_image_url = random.choice(images_urls)

            await message.channel.send(random_image_url)


def setup(bot):
    bot.add_cog(RobertKubicaPictures(bot))
