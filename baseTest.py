# -*- coding: utf-8 -*-

from __future__ import print_function

__author__ = 'goncharov'

import unittest
import basedata


class TestBaseAstrology(unittest.TestCase):
    def test_elements(self):
        a = basedata.BaseAstrology(1963)
        j = a.get_elements()
        self.assertEqual(a.birth_year, 1963)
        res = {'animal': u'Кролик', 'sog': u'Дерево', 'lu': u'Железо', 'wang': u'Вода',
               'lung': u'Огонь', 'la': u'Вода'}
        self.assertEqual(j, res)

        a = basedata.BaseAstrology(1984)
        j = a.get_elements()
        self.assertEqual(a.birth_year, 1984)
        res = {'animal': u'Крыса', 'sog': u'Вода', 'lu': u'Железо',
               'wang': u'Дерево', 'lung': u'Дерево', 'la': u'Железо'}
        self.assertEqual(j, res)

    def test_relations(self):
        a = basedata.BaseAstrology(1963)
        j = a.get_elements()
        c = a.cross_relation(j, j, '-')
        res = {u'sog:wang': u'Мать', u'lu:la': u'Сын', u'lu:wang': u'Сын', u'lu:sog': u'Друг',
               u'wang:lu': u'Мать', u'la:lu': u'Мать', u'sog:lu': u'Враг', u'lung:wang': u'Враг',
               u'lung:lu': u'Друг', u'lung:la': u'Враг', u'sog:lung': u'Сын', u'la:lung': u'Друг',
               u'lung:sog': u'Мать', u'la:sog': u'Сын', u'wang:lung': u'Друг', u'lu:lung': u'Враг',
               u'wang:sog': u'Сын', u'sog:la': u'Мать'}
        self.assertEqual(c, res)

        a = basedata.BaseAstrology(1984)
        j = a.get_elements()
        c = a.cross_relation(j, j, '-')
        res = {u'sog:wang': u'Сын', u'la:sog': u'Сын', u'lu:wang': u'Друг', u'lu:sog': u'Сын',
               u'wang:lu': u'Враг', u'sog:lu': u'Мать', u'la:wang': u'Друг', u'lung:la': u'Враг',
               u'sog:lung': u'Сын', u'wang:la': u'Враг', u'la:lung': u'Друг', u'lung:sog': u'Мать',
               u'lung:lu': u'Враг', u'lu:lung': u'Друг', u'wang:sog': u'Мать', u'sog:la': u'Мать'}
        self.assertEqual(c, res)
        # for k,v in c.iteritems():
        #     #if not (v in ('-', u'Друг', u'Мать', u'Сын')):
        #     print("u'%s': u'%s'," % (k, v))

    def test_parka(self):
        a = basedata.BaseAstrology(1965)
        p = a.get_parka(2000, 'man')

        self.assertEqual(p, u'та')
        p = a.get_parka(2001, 'man')
        self.assertEqual(p, u'кхен')

        a = basedata.BaseAstrology(1979)
        p = a.get_parka(2000, 'woman')
        self.assertEqual(p, u'ли')
        p = a.get_parka(2001, 'woman')
        self.assertEqual(p, u'сон')


    def test_parkaDirection(self):
        a = basedata.BaseAstrology(1963)
        p = a.get_parka(2000, 'man')
        pd = a.get_parka_direction(p)
        # for ix in range(3):
        #      for iy in range(3):
        #          print("u'%s'," % pd[ix][iy], end=' ')
        #      print()
        res = [[u'Демон отсечения', u'Зло', u'Поддержка жизни'],
               [u'истощение правая нога', u'кин', u'Небесное лекарство'],
               [u'Реализация счастливой судьбы', u'Пять злых духов', u'Порождение процветания']]
        #self.assertEqual(pd, res)

        a = basedata.BaseAstrology(1984)
        p = a.get_parka(2016, 'man')
        pd = a.get_parka_direction(p)
        res = [[u'Порождение процветания', u'Реализация счастливой судьбы', u'истощение голова'],
               [u'Поддержка жизни', u'ли', u'Пять злых духов'],
               [u'Зло', u'Небесное лекарство', u'Демон отсечения']]
        #self.assertEqual(pd, res)

    def test_meva(self):
        a = basedata.BaseAstrology(1974)
        m = a.get_mevas(2000)
        res = {'wangme':2, 'lume':8, 'pawme':7, 'lunme':8, 'sogme':5, 'bmewa':8}
        self.assertEqual(m, res)
        a = basedata.BaseAstrology(1975)
        m = a.get_mevas(2000)
        res = {'pawme': 3, 'sogme': 4, 'wangme': 1, 'lunme': 2, 'bmewa': 7, 'lume': 7}
        self.assertEqual(m, res)

    def test_logmen(self):
        a = basedata.BaseAstrology(1970)
        l = a.get_logmen(2000, 'man')
        self.assertEqual(l, (u'Железо', u'Баран'))
        a = basedata.BaseAstrology(1968)
        l = a.get_logmen(2001, 'man')
        self.assertEqual(l, (u'Вода', u'Собака'))

        a = basedata.BaseAstrology(1974)
        l = a.get_logmen(2001, 'woman')
        self.assertEqual(l, (u'Огонь', u'Лошадь'))

        a = basedata.BaseAstrology(1972)
        l = a.get_logmen(2001, 'woman')
        self.assertEqual(l, (u'Вода', u'Дракон'))

    def test_month(self):
        a = basedata.BaseAstrology(1924)
        res = a.get_months_of_year(1925)
        self.assertEqual(res, [
            (u'Огонь', u'Тигр', u'мужской'), (u'Огонь', u'Кролик', u'женский'),
            (u'Земля', u'Дракон', u'мужской'), (u'Земля', u'Змея', u'женский'),
            (u'Железо', u'Лошадь', u'мужской'), (u'Железо', u'Баран', u'женский'),
            (u'Вода', u'Обезьяна', u'мужской'), (u'Вода', u'Петух', u'женский'),
            (u'Дерево', u'Собака', u'мужской'), (u'Дерево', u'Свинья', u'женский'),
            (u'Огонь', u'Крыса', u'мужской'), (u'Огонь', u'Корова', u'женский')])

        res = a.get_days_of_month((u'Огонь', u'Тигр', u'мужской'))
        self.assertEqual(res[14], (15, u'Огонь', u'Дракон'))
        res = a.get_days_of_month((u'Огонь', u'Тигр', u'женский'))
        self.assertEqual(res[14], (15, u'Огонь', u'Собака'))

        res = a.get_hours_of_day((15, u'Огонь', u'Тигр'))
        self.assertEqual(res[6], (7, u'Железо', u'Петух'))

    def test_tarkut(self):
        a = basedata.BaseAstrology(1980)
        res = a.get_tarkut(1980, 3, 3, 4)
        self.assertEqual(res, {'sogtarkut': 7, 'wangtarkut': 3, 'lungtarkut': 11, 'lutarkut': 9})

    def test_tribal(self):
        a = basedata.BaseAstrology(1970)
        res = a.get_tribal(u"Земля")
        self.assertEqual(res,u'Малое истощение')
        res = a.get_tribal(u"Железо")
        self.assertEqual(res,u'Мать')
        res = a.get_tribal(u"Огонь")
        self.assertEqual(res,u'Большое истощение')
        return
if __name__ == '__main__':
    unittest.main()
