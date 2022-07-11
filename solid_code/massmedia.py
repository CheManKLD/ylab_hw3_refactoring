from abc import ABC, abstractmethod

from heroes import SuperHero
from places import Place, Mars, Planet


class MassMedia(ABC):
    name: str

    @abstractmethod
    def create_news(self, hero: SuperHero, place: Place):
        pass


class TVNews(MassMedia):
    name = 'CNN'

    def create_news(self, hero, place):
        hero_name = getattr(hero, 'name', 'hero')
        place_name = getattr(place, 'name', 'place')
        news = f'{self.name} - Breaking News: {hero_name} saved the {place_name}!'
        print(news)
        Planet.get_tv_news_from_earth(Mars, news)


class Newspaper(MassMedia):
    name = 'Daily News'

    def create_news(self, hero, place):
        hero_name = getattr(hero, 'name', 'hero')
        place_name = getattr(place, 'name', 'place')
        print(f'Front page of {self.name}: {hero_name} saved the {place_name}!')
