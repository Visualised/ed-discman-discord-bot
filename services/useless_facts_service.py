import requests


class UselessFactsService:
    @staticmethod
    def get_useless_fact(language: str):
        if language != "en" and language != "de":
            language = "en"

        response = requests.get(f"https://uselessfacts.jsph.pl/random.json?language={language}")
        json_data = response.json()
        string_data = (
            f'Useless fact: {json_data["text"]}\n'
            f'source: {json_data["source"]}\n'
            f'source URL: {json_data["source_url"]}'
        )

        return string_data
