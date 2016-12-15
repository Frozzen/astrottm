# -*- coding: utf-8 -*-
"""
15,60 ветвей
"""
from __future__ import print_function

import datetime

__author__ = 'vovva'

import basedata



class Branches15:
    """
    медицинский гороскоп 15 ветвей

    """
    ill_types = (u'Дерево', u'Огонь', u'Земля', u'Железо', u'Вода')

    def __init__(self, year, itype, sex):
        """

        :param year: год рождения персоны
        :param itype: 0-5
        :param sex: пол
        :return:
        """
        self.ill_element = self.ill_types[itype]
        self.sex = sex
        # элементы
        self.chart_elements = [['' for x in range(5)] for y in range(16)]
        # камни
        self.chart_stones = [['' for x in range(6)] for y in range(17)]

        # сам
        self.astro = basedata.BaseAstrology(year)
        el = self.astro.get_elements()
        self.chart_elements[0][0] = "%s:%s" % (el['wang'], el['animal'])
        self.animal = el['animal']
        self.chart_elements[0][1] = el['sog']
        self.chart_elements[0][2] = el['lu']
        self.wang = self.chart_elements[0][3] = el['wang']
        self.chart_elements[0][4] = el['lung']

    def compute(self, year):
        """
        построить таблицу 15ветвей на год

        :param year: год возникновения болези, год осложнения, год обращения к астрологу
        :return:
        """
        # 1 ветвь утрачивается ли энергия ла - подкосит больезнь или нет
        a = basedata.BaseAstrology(year)
        el = a.get_elements()
        self.chart_elements[1][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[1][1] = el['sog']
        self.chart_elements[1][2] = el['lu']
        self.chart_elements[1][3] = el['wang']
        self.chart_elements[1][4] = el['lung']

        # 2 ветвь Жилище утрачивается ? - жрец астролог - вред астрологу
        do_from = {u'Дерево': u'Тигр', u'Огонь': u'Лошадь', u'Земля': u'Дракон', u'Железо': u'Обезьяна',
                   u'Вода': u'Крыса'}
        el = self.astro.find_relative(self.wang, u'Враг')
        y = self.astro.find_year(el, do_from[self.ill_element])
        y += year - self.astro.birth_year
        el = self.astro.get_elements(y)
        self.chart_elements[2][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[2][1] = el['sog']
        self.chart_elements[2][2] = el['lu']
        self.chart_elements[2][3] = el['wang']
        self.chart_elements[2][4] = el['lung']

        # 3 ветвь Шапка из войлока износилась? - родители субъекта
        y = self.astro.find_year(self.wang, do_from[self.ill_element])
        y += year - self.astro.birth_year
        el = self.astro.get_elements(y)
        self.chart_elements[3][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[3][1] = el['sog']
        self.chart_elements[3][2] = el['lu']
        self.chart_elements[3][3] = el['wang']
        self.chart_elements[3][4] = el['lung']

        # 4 утрачивает советник свой пост?
        do_from[u'Земля'] = u'Собака'
        el = self.astro.find_relative(self.wang, u'Друг')
        y = self.astro.find_year(el, do_from[self.ill_element])
        y += year - self.astro.birth_year
        el = self.astro.get_elements(y)
        self.chart_elements[4][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[4][1] = el['sog']
        self.chart_elements[4][2] = el['lu']
        self.chart_elements[4][3] = el['wang']
        self.chart_elements[4][4] = el['lung']

        # 5 поникли усы тигра? истощается могущестов - события у супруга
        el = self.astro.find_relative(self.wang, u'Мать')
        y = self.astro.find_year(el, do_from[self.ill_element])
        y += year - self.astro.birth_year
        el = self.astro.get_elements(y)
        self.chart_elements[5][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[5][1] = el['sog']
        self.chart_elements[5][2] = el['lu']
        self.chart_elements[5][3] = el['wang']
        self.chart_elements[5][4] = el['lung']

        # 6 приходят грабители?
        do_from = {u'Дерево': u'Кролик', u'Огонь': u'Змея', u'Земля': u'Баран', u'Железо': u'Петух', u'Вода': u'Свинья'}
        el = self.astro.find_relative(self.wang, u'Враг')
        y = self.astro.find_year(el, do_from[self.ill_element])
        y -= year - self.astro.birth_year
        el = self.astro.get_elements(y)
        self.chart_elements[6][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[6][1] = el['sog']
        self.chart_elements[6][2] = el['lu']
        self.chart_elements[6][3] = el['wang']
        self.chart_elements[6][4] = el['lung']

        # 7 уносят духи кармы?
        el = self.astro.find_relative(self.wang, u'Мать')
        y = self.astro.find_year(el, do_from[self.ill_element])
        y -= year - self.astro.birth_year
        el = self.astro.get_elements(y)
        self.chart_elements[7][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[7][1] = el['sog']
        self.chart_elements[7][2] = el['lu']
        self.chart_elements[7][3] = el['wang']
        self.chart_elements[7][4] = el['lung']

        # 8 сломалось волшебное дерево - жизненная сила ребенка
        do_from[u'Земля'] = u'Бык'
        el = self.wang
        y = self.astro.find_year(el, do_from[self.ill_element])
        y -= year - self.astro.birth_year
        el = self.astro.get_elements(y)
        self.chart_elements[8][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[8][1] = el['sog']
        self.chart_elements[8][2] = el['lu']
        self.chart_elements[8][3] = el['wang']
        self.chart_elements[8][4] = el['lung']

        # 9 амбары опустели - материальное благополучие, состояние дома
        el = self.astro.find_relative(self.wang, u'Сын')
        y = self.astro.find_year(el, do_from[self.ill_element])
        y -= year - self.astro.birth_year
        el = self.astro.get_elements(y)
        self.chart_elements[9][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[9][1] = el['sog']
        self.chart_elements[9][2] = el['lu']
        self.chart_elements[9][3] = el['wang']
        self.chart_elements[9][4] = el['lung']

        # 10 оборовался канат - небесные врата - ближайший год
        y = (year - self.astro.birth_year) + year - 8 + 1
        el = self.astro.get_elements(y)
        self.chart_elements[10][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[10][1] = el['sog']
        self.chart_elements[10][2] = el['lu']
        self.chart_elements[10][3] = el['wang']
        self.chart_elements[10][4] = el['lung']

        # 11 развязался пояс - жизненная сила
        y = -(year - self.astro.birth_year) + year + 8 - 1
        el = self.astro.get_elements(y)
        self.chart_elements[11][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[11][1] = el['sog']
        self.chart_elements[11][2] = el['lu']
        self.chart_elements[11][3] = el['wang']
        self.chart_elements[11][4] = el['lung']

        # 12 поднялся ураган? близкий друг - угроза смерти
        do_from = {u'Дерево': u'Тигр', u'Огонь': u'Лошадь', u'Земля': u'Дракон', u'Железо': u'Обезьяна',
                   u'Вода': u'Крыса'}
        el = self.astro.find_relative(self.wang, u'Сын')
        y = self.astro.find_year(el, do_from[self.ill_element])
        y += (year - self.astro.birth_year)
        el = self.astro.get_elements(y)
        self.chart_elements[12][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[12][1] = el['sog']
        self.chart_elements[12][2] = el['lu']
        self.chart_elements[12][3] = el['wang']
        self.chart_elements[12][4] = el['lung']

        # 13 разрушился звездный дом - все члены семьи
        el = self.astro.find_relative(self.wang, u'Мать')
        y = self.astro.find_year(el, u'Обезьяна')
        y -= (year - self.astro.birth_year)
        el = self.astro.get_elements(y)
        self.chart_elements[13][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[13][1] = el['sog']
        self.chart_elements[13][2] = el['lu']
        self.chart_elements[13][3] = el['wang']
        self.chart_elements[13][4] = el['lung']

        # 14 вырвалась подушка из под головы - продолжительность болезни
        y = (year - self.astro.birth_year) + year - 5 + 1
        el = self.astro.get_elements(y)
        self.chart_elements[14][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[14][1] = el['sog']
        self.chart_elements[14][2] = el['lu']
        self.chart_elements[14][3] = el['wang']
        self.chart_elements[14][4] = el['lung']

        # 15 повалился клин - опора?
        y = -(year - self.astro.birth_year) + year + 5 - 1
        el = self.astro.get_elements(y)
        self.chart_elements[15][0] = "%s:%s" % (el['wang'], el['animal'])
        self.chart_elements[15][1] = el['sog']
        self.chart_elements[15][2] = el['lu']
        self.chart_elements[15][3] = el['wang']
        self.chart_elements[15][4] = el['lung']

    def do_stones(self):
        """
        вычислить камни для гороскопа исходя из вычисленных элементов
        :return:
        """

        stones_el = {u'Земля:Земля': 'O', u'Вода:Вода': 'O', u'Дерево:Дерево': 'X', u'Огонь:Огонь': 'X',
                     u'Железо:Железо': 'X'}
        stones_rel = {u'Мать': 'O', u'Друг': 'O', u'Враг': 'X', u'Сын': 'X/O'}
        for ix in range(1, 16):
            for iy in range(1, 5):
                xel = "%s:%s" % (self.chart_elements[0][iy], self.chart_elements[ix][iy])
                if xel in stones_el:
                    stone = stones_el[xel]
                else:
                    rel = self.astro.get_relations(self.chart_elements[0][iy], self.chart_elements[ix][iy])
                    stone = stones_rel[rel]
                self.chart_stones[ix][iy] = stone

        # посчитать камни по вертикали
        for ix in range(1, 16):
            cnt = 0
            for iy in range(1, 5):
                if self.chart_stones[ix][iy] == 'O':
                    cnt += 1
                elif self.chart_stones[ix][iy] == 'X':
                    cnt -= 1
            if cnt < 0:
                self.chart_stones[ix][5] = 'X'
            elif cnt > 0:
                self.chart_stones[ix][5] = 'O'
            else:
                self.chart_stones[ix][5] = 'X/O'

        # посчитали по горизонтали
        for iy in range(1, 5):
            cnt = 0
            for ix in range(1, 16):
                if self.chart_stones[ix][iy] == 'O':
                    cnt += 1
                elif self.chart_stones[ix][iy] == 'X':
                    cnt -= 1
            if cnt < 0:
                self.chart_stones[16][iy] = 'X'
            elif cnt > 0:
                self.chart_stones[16][iy] = 'O'
            else:
                self.chart_stones[16][iy] = 'X/O'

    def print_stones(self):
        print();
        print("15 ветей элеименты")
        for iy in range(4):
            for ix in range(15):
                print("%15.15s|" % self.chart_elements[ix][iy],end='')

            print();
        print();
        print("Элемент заболевания:", self.ill_element)
        for iy in range(5):
            for ix in range(17):
                print("%5.5s|" % self.chart_stones[ix][iy],end='')

            print();

class Branches16:
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

def main():
    pass


if __name__ == '__main__':
    main()
