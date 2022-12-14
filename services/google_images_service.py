from google_images_download import google_images_download


class GoogleImagesService:
    @staticmethod
    def get_images_urls(query: str):
        arguments = {
            "keywords": query,
            "limit": 50,
            "no_download": True,
            "silent_mode": True,
        }

        scraper = google_images_download.googleimagesdownload()
        response = scraper.download(arguments)
        images_urls = response[0][query]
        images_urls = [
            url + "\n" for url in images_urls
        ]  # adds line break to each URL to make it save to file friendly

        return images_urls

    @staticmethod
    def save_links_to_file(filename: str, links: list):
        with open(filename, "w+", encoding="UTF-8") as f:
            f.writelines(links)
