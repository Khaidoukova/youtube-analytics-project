import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate



class Channel:
    """Класс для ютуб-канала"""

    @classmethod
    def get_service(cls):
        """Класс-метод, возвращающий объект для работы с YouTube API"""
        api_key: str = os.getenv('YT_API_KEY')
        yt_object = build('youtube', 'v3', developerKey=api_key)
        return yt_object


    def __init__(self, channel_id) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = Channel.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        # новые атрибуты
        self.title = channel["items"][0]["snippet"]["title"]
        self.description = channel["items"][0]["snippet"]["description"]
        self.url = channel["items"][0]["snippet"]["thumbnails"]["default"]["url"]
        self.subscriber_count = channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = channel["items"][0]["statistics"]["videoCount"]
        self.view_count = channel["items"][0]["statistics"]["viewCount"]

    @property
    def channel_id(self):
        """Геттер для приватного атрибута channel_id"""
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Сеттер для приватного атрибута channel_id"""
        self.__channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = Channel.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        info = json.dumps(channel, indent=2, ensure_ascii=False)
        print(info)

    def to_json(self, file_name):
        yt_dict = {}
        yt_dict["id"] = self.channel_id
        yt_dict["title"] = self.title
        yt_dict["description"] = self.description
        yt_dict["url"] = self.url
        yt_dict["subscriber_count"] = self.subscriber_count
        yt_dict["video_count"] = self.video_count
        yt_dict["view_count"] = self.view_count
        with open(file_name, 'w', encoding="UTF-8") as file:
            json.dump(yt_dict, file, indent=2, ensure_askii=False)







