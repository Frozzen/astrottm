# -*- coding: utf-8 -*-
"""
рабираемся с часами

"""
from __future__ import print_function
from astral import Astral, Location
import datetime

__author__ = 'goncharov'


class HoursHoro:
    week_days = [u'Воскресенье', u'Понедельник', u'Вторник', u'Среда', u'Четверг', u'Пятница', u'Суббота']
    planet_days = [u'Солнце', u'Луна', u'Марс', u'Меркурий', u'Юпитер', u'Венера', u'Сатурн']
    mages_star = [u'Солнце', u'Венера', u'Меркурий', u'Луна', u'Сатурн', u'Юпитер', u'Марс']

    def __init__(self, name, lat, lon, timezone, elevation):

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

        self.planets_hours = {}
        # дневные управители
        ih = 0
        for wd in self.week_days:
            hours = []
            for h in self.hour_animal_list[:6]:
                hours.append((h, self.mages_star[ih], self.mages_star[(ih + 1) % 7]))
                ih = (ih + 2) % 7
            ih -= 2
            self.planets_hours[wd] = hours

        # ночные управители
        ih = 0
        for wd in self.week_days:
            for h in self.hour_animal_list[6:]:
                self.planets_hours[wd].append((h, self.mages_star[ih], self.mages_star[(ih - 2) % 7]))
                ih = (ih - 4) % 7
            ih = (ih - 1) % 7

    def print_tabs(self):
        # дневные управители
        print(u'дневные управители')
        print("%15.15s|" % u' ', end='')
        for h in self.hour_animal_list[:6]:
            print("%-21.21s|" % (h), end='')
        print()
        for d in self.week_days:
            print("%15.15s|" % d, end='')
            for h in range(6):
                print("%10.10s|%10.10s|" % (
                    self.planets_hours[d][h][1], self.planets_hours[d][h][2]), end='')

            print()

        # ночные управители
        print(u'ночные управители')
        print("%15.15s|" % u' ', end='')
        for h in self.hour_animal_list[6:]:
            print("%-21.21s|" % (h), end='')
        print()
        for d in self.week_days:
            print("%15.15s|" % d, end='')
            for h in range(6, 12):
                print("%10.10s|%10.10s|" % (
                    self.planets_hours[d][h][1], self.planets_hours[d][h][2]), end='')

            print()

    def get_sun(self, day=None):
        """
        получить параметры восход заход солнца
        :param day:
        :return: Dictionary with keys ``dawn``, ``sunrise``, ``noon``,
            ``sunset`` and ``dusk`` whose values are the results of the
            corresponding methods
        """
        sun = self.location.sun(day)
        return sun

    def get_planets(self, day=None):
        """
        получить время планет управителей часа в тибьетском календаре - по звезде магов

        :param day:
        :return:
        """

        s = self.get_sun(day)
        day_len = s['dusk'] - s['dawn']
        dlen = day_len.seconds / 6.
        nlen = (24 * 3600 - day_len.seconds) / 6.
        # TODO сделать интерполяцию сплайном часов
        hour = 0
        plan = {}
        for h in self.hour_animal_list[:6]:
            plan[h] = {
                'start': s['dawn'] + datetime.timedelta(seconds=(dlen * hour))
            }
            hour += 1
        hour = 0
        for h in self.hour_animal_list[6:]:
            plan[h] = {
                'start': s['dusk'] + datetime.timedelta(seconds=(nlen * hour))
            }
            hour += 1
        return plan

    def print_hrs(self, hours):
        for h in self.hour_animal_list:
            print("%20.20s %s" % (h, hours[h]['start'].strftime("%H:%M:%S")))


if __name__ == '__main__':
    a = HoursHoro('Novosibirsk', 54, 83, 'Asia/Novosibirsk', 120)
    a.print_tabs()
    a.print_hrs(a.get_planets())
