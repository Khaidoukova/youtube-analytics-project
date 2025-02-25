import json
from src.ytmixin import YTMixin


class Channel(YTMixin):
    """Класс для ютуб-канала"""

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

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        if not isinstance(other, Channel):
            raise ValueError('Складывать можно только два объекта Channel.')
        else:
            return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __rsub__(self, other):
        return int(other.subscriber_count) - int(self.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)

    @property
    def channel_id(self):
        """Геттер для приватного атрибута channel_id"""
        return self.__channel_id

    #@channel_id.setter
    #def channel_id(self, channel_id):
       # """Сеттер для приватного атрибута channel_id"""
       # self.__channel_id = channel_id


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
            json.dump(yt_dict, file, indent=2, ensure_ascii=False)







