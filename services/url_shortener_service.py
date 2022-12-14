import requests


class UrlShortenerService:
    @staticmethod
    def shorten_url(url: str):
        response = requests.post("https://cleanuri.com/api/v1/shorten", data={"url": url})
        data = response.json()
        return data["result_url"]
