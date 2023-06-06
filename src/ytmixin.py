import os
from googleapiclient.discovery import build

class YTMixin:
    """
    Класс-миксин для работы с API ютуба.
    """

    api_key: str = os.getenv('API_KEY')

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с API youtube.
        """

        youtube = build('youtube', 'v3', developerKey=cls.api_key)

        return youtube
