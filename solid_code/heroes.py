from abc import ABC, abstractmethod

from antagonistfinder import AntagonistFinder
from places import Place


class SuperHero(ABC):
    def __init__(self, name: str, can_use_ultimate_attack: bool = True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place: Place):
        self.finder.find_antagonist(place)

    @abstractmethod
    def attack(self):
        pass

    def ultimate(self):
        pass


class KickMixin:
    @staticmethod
    def kick():
        print('Pow')

    @staticmethod
    def roundhouse_kick():
        print('Bump')


class GunMixin:
    @staticmethod
    def fire_a_gun():
        print('PIU PIU')


class LaserMixin:
    @staticmethod
    def incinerate_with_lasers():
        print('Wzzzuuuup!')


class Superman(SuperHero, KickMixin, LaserMixin):
    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        self.kick()

    def ultimate(self):
        self.incinerate_with_lasers()


class ChuckNorris(SuperHero, KickMixin, GunMixin):
    def __init__(self):
        super(ChuckNorris, self).__init__('Chuck Norris', False)

    def attack(self):
        self.fire_a_gun()
        self.roundhouse_kick()
