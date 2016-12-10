# -*- coding: utf-8 -*-
"""
    вычисляем касающиеся дневного цикла - вычисляем час

"""
from __future__ import print_function
import datetime
from astral import Astral, Location

class AstoHours:
    """
        вычисляем касающиеся дневного цикла - вычисляем час
    """
    animal_list = (
        u'Кролик', u'Дракон', u'Змея', u'Лошадь', u'Баран', u'Обезьяна',
        u'Петух', u'Собака', u'Свинья', u'Крыса', u'Корова', u'Тигр',
    )
    planets = [u'Солнце', u'Луна', u'Марс', u'Меркурий', u'Юпитер', u'Венера', u'Сатурн']

    def __init__(self, name, lat, lon, timezone, elevation):
        """

        :param name:
        :param lat:
        :param lon:
        :param timezone:
        :param elevation:
        """
        a = Astral()
        a.solar_depression = 'nautical'
        self.astral = a

        l = Location()
        l.name = name
        l.latitude = lat
        l.longitude = lon
        l.timezone = timezone
        l.elevation = elevation
        self.location = l

    def get_sun(self, day = None):
        """
        получить параметры восход заход солнца
        :param day:
        :return: Dictionary with keys ``dawn``, ``sunrise``, ``noon``,
            ``sunset`` and ``dusk`` whose values are the results of the
            corresponding methods
        """
        sun = self.location.sun(day)
        return sun

    def get_planets(self, day = None):
        """
        получить время планет управителей часа в тибьетском календаре - по звезде магов

        :param day:
        :return:
        """
        s = self.get_sun(day)
        day_len = s['dusk'] - s['dawn']
        hlen = day_len / 6.
        nlen = (24 - day_len) / 6.
        self.planets = {}
        # заполняем дневные часы
        cur_planet = 0
        hour = 0
        plan = {}
        for h in self.animal_list[:6]:
            plan[h] = { 'start': (s['dawn'] + hlen * hour, self.planets[cur_planet])
            }


def main():

    a = AstoHours('Novosibirsk',54,83,'Asia/Novosibirsk',120)
    sun = a.get_sun()
    print('Latitude: %.02f; Longitude: %.02f\n' % (a.location.latitude, a.location.longitude))
    print('Dawn:    %s' % str(sun['dawn']))
    print('Sunrise: %s' % str(sun['sunrise']))
    print('Noon:    %s' % str(sun['noon']))
    print('Sunset:  %s' % str(sun['sunset']))
    print('Dusk:    %s' % str(sun['dusk']))
    print(a.get_planets())

if __name__ == '__main__':
    main()
