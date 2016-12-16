# -*- coding: utf-8 -*-
"""
16 плодов
"""
from __future__ import print_function

import datetime

__author__ = 'vovva'

import basedata

class Fruit16:
    """
    16 ветвей прогноз для тяжелобольных
    """
    rules_rel = {u'Мать':'O', u'Друг':'O',
                 u'Сын': 'X', u'Враг': 'X'}
    rules_elem = {u'Земля:Земля':'O', u'Вода:Вода':'O',
                  u'Огонь:Огонь':'X', u'Железо:Железо':'X', u'Дерево:Дерево':'X'}

    def __init__(self, bitrh):
        """
        считаем на год рождения

        :param bitrh:
        """
        self.astro = basedata.BaseAstrology(bitrh)
        el = self.astro.get_elements()
        self.el_subj = {"elts": u"%s:%s" % (el['wang'], el['animal']),
            'sog': el['sog'], 'lu' : el['lu'] }

    def find_elem_stone(self, element1, element2):
        """
        найти как соотносятся элементы
        :param element1:
        :param element2:
        :return:
        """
        el = "%s:%s" % (element1, element2)
        if el in self.rules_elem:
                return self.rules_elem[el]
        rl = self.astro.get_relations(element1, element2)
        return self.rules_rel[rl]

    def calc(self, year=None, month=None, day=None, hour=None):
        """
        вычисляем данные для гороскопа - на дату заболевания.
        если не указанно берется текущая дата

        :param year:
        :param month: лунный месяц
        :param day:
        :param hour:
        :return:
        """
        dt = datetime.datetime.now()
        if year is None:
            year = dt.year
        if month is None:
            month = dt.month
        else:
            month -=1
        if day is None:
            day = dt.day
        else:
            day -=1
        if hour is None:
            hour = dt.hour
        else:
            hour -=1

        el = self.astro.get_elements(year)
        self.el_year = {"elts": u"%s:%s" % (el['wang'], el['animal']),
            'sog': el['sog'], 'lu' : el['lu'] }
        res_mnth = self.astro.get_months_of_year(year)
        self.el_month = {"elts": u"%s:%s" % (res_mnth[month][0], res_mnth[month][1]),
            'sog': el['sog'], 'lu' : el['lu'] }
        res_day = self.astro.get_days_of_month(res_mnth[month])
        self.el_day = {"elts": u"%s:%s" % (res_day[day][1], res_day[day][2]),
            'sog': el['sog'], 'lu' : el['lu'] }
        res_hr = self.astro.get_hours_of_day(res_day[day])
        self.el_hour = {"elts": u"%s:%s" % (res_hr[hour][1], res_hr[hour][2]),
            'sog': el['sog'], 'lu' : el['lu'] }

        self.el_year['sogstone'] = self.find_elem_stone(self.el_subj['sog'], self.el_year['sog'])
        self.el_month['sogstone'] = self.find_elem_stone(self.el_subj['sog'], self.el_month['sog'])
        self.el_day['sogstone'] = self.find_elem_stone(self.el_subj['sog'], self.el_day['sog'])
        self.el_hour['sogstone'] = self.find_elem_stone(self.el_subj['sog'], self.el_hour['sog'])

        self.el_year['lustone'] = self.find_elem_stone(self.el_subj['lu'], self.el_year['lu'])
        self.el_month['lustone'] = self.find_elem_stone(self.el_subj['lu'], self.el_month['lu'])
        self.el_day['lustone'] = self.find_elem_stone(self.el_subj['lu'], self.el_day['lu'])
        self.el_hour['lustone'] = self.find_elem_stone(self.el_subj['lu'], self.el_hour['lu'])


        res_mnth = self.astro.get_tarkut(year, month, day, hour)
        self.el_year['sogtarkut'] = self.astro.find_tarkut_str(res_mnth['sogtarkut'])[2]
        self.el_year['sogtarkutstone'] = self.astro.find_tarkut_str(res_mnth['sogtarkut'])[1]
        self.el_year['lutarkut'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[2]
        self.el_year['lutarkutstone'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[1]
        self.el_month['sogtarkut'] = self.astro.find_tarkut_str(res_mnth['sogtarkut'])[2]
        self.el_month['sogtarkutstone'] = self.astro.find_tarkut_str(res_mnth['sogtarkut'])[1]
        self.el_month['lutarkut'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[2]
        self.el_month['lutarkutstone'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[1]
        self.el_day['sogtarkut'] = self.astro.find_tarkut_str(res_mnth['sogtarkut'])[2]
        self.el_day['sogtarkutstone'] = self.astro.find_tarkut_str(res_mnth['sogtarkut'])[1]
        self.el_day['lutarkut'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[2]
        self.el_day['lutarkutstone'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[1]
        self.el_hour['sogtarkut'] = self.astro.find_tarkut_str(res_mnth['sogtarkut'])[2]
        self.el_hour['sogtarkutstone'] = self.astro.find_tarkut_str(res_mnth['sogtarkut'])[1]

        self.el_year['lutarkut'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[2]
        self.el_year['lutarkutstone'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[1]
        self.el_month['lutarkut'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[2]
        self.el_month['lutarkutstone'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[1]
        self.el_day['lutarkut'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[2]
        self.el_day['lutarkutstone'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[1]
        self.el_hour['lutarkut'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[2]
        self.el_hour['lutarkutstone'] = self.astro.find_tarkut_str(res_mnth['lutarkut'])[1]

    def print_el(self):
        print()
        print("%15.15s|%15.15s|%15.15s|%15.15s|%15.15s|" %
              (u'Субъект' ,u'Год', u'Месяц', u'День', u'Час'))
        print("%15.15s|%15.15s|%15.15s|%15.15s|%15.15s|" %
              (self.el_subj['elts'] , self.el_year['elts'], self.el_month['elts'],
               self.el_day['elts'], self.el_hour['elts']))

        print("%15.15s|%9.9s|%5.5s|%9.9s|%5.5s|%9.9s|%5.5s|%9.9s|%5.5s|" %
              (self.el_subj['sog'], self.el_year['sog'], self.el_year['sogstone'],
               self.el_month['sog'], self.el_month['sogstone'],
               self.el_day['sog'], self.el_day['sogstone'],
               self.el_hour['sog'], self.el_hour['sogstone']))
        print("%15.15s|%9.9s|%5.5s|%9.9s|%5.5s|%9.9s|%5.5s|%9.9s|%5.5s|" %
              ('' , self.el_year['sogtarkut'],  self.el_year['sogtarkut'],
               self.el_month['sogtarkut'],self.el_month['sogtarkutstone'],
               self.el_day['sogtarkut'],self.el_day['sogtarkutstone'],
               self.el_hour['sogtarkut'], self.el_hour['sogtarkutstone']))
        print("%15.15s|%9.9s|%5.5s|%9.9s|%5.5s|%9.9s|%5.5s|%9.9s|%5.5s|" %
              (self.el_subj['lu'] ,  self.el_year['lu'], self.el_year['lustone'],
               self.el_month['lu'],self.el_month['lustone'],
               self.el_day['lu'], self.el_day['lustone'],
               self.el_hour['lu'], self.el_hour['lustone']))
        print("%15.15s|%9.9s|%5.5s|%9.9s|%5.5s|%9.9s|%5.5s|%9.9s|%5.5s|" %
              ('' , self.el_year['lutarkut'], self.el_year['lutarkutstone'],
               self.el_month['lutarkut'],self.el_month['lutarkutstone'],
               self.el_day['lutarkut'],self.el_day['lutarkutstone'],
               self.el_hour['lutarkut'], self.el_hour['lutarkutstone']))
