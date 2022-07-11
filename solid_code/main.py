from heroes import SuperHero, Superman, ChuckNorris
from massmedia import MassMedia, TVNews, Newspaper
from places import Kostroma, Tokyo, Place


def save_the_place(hero: SuperHero, place: Place, massmedia: MassMedia):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    massmedia.create_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), TVNews())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo(), Newspaper())
