from abc import ABC, abstractmethod
from typing import List


class Place(ABC):
    name: str

    @staticmethod
    @abstractmethod
    def get_antagonist():
        pass


class Kostroma(Place):
    name = 'Kostroma'

    @staticmethod
    def get_antagonist():
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    @staticmethod
    def get_antagonist():
        print('Godzilla stands near a skyscraper')


class Planet(ABC):
    coordinates: List[float]

    def get_tv_news_from_earth(self, news: str):
        print(f'Planet {self.coordinates} got news from Earth: "{news}"')


class Mars(Planet):
    coordinates = [123.213123, 45345.123123]
