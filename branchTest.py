# -*- coding: utf-8 -*-

from __future__ import print_function

__author__ = 'goncharov'

import unittest
import branches

__author__ = 'vovva'

class TestBranches(unittest.TestCase):

    def test_15braches(self):
        a = branches.Branches15(1974, 0, 'man')
        self.assertEqual(a.chart_elements[0],[u'Дерево:Тигр',u'Дерево',u'Вода',u'Дерево',u'Железо'])

        a.compute(2000)
        self.assertEqual(a.chart_elements[1], [u'Железо:Дракон',u'Земля',u'Железо',u'Железо',u'Дерево'])
        self.assertEqual(a.chart_elements[2], [u'Огонь:Дракон',u'Земля',u'Земля',u'Огонь',u'Дерево'])
        self.assertEqual(a.chart_elements[3], [u'Железо:Дракон',u'Земля',u'Железо',u'Железо',u'Дерево'])
        self.assertEqual(a.chart_elements[4], [u'Дерево:Дракон',u'Земля',u'Огонь',u'Дерево',u'Дерево'])
        self.assertEqual(a.chart_elements[5], [u'Земля:Дракон',u'Земля',u'Дерево',u'Земля',u'Дерево'])

        self.assertEqual(a.chart_elements[6], [u'Дерево:Бык',u'Земля',u'Железо',u'Дерево',u'Вода'])
        self.assertEqual(a.chart_elements[7], [u'Огонь:Бык',u'Земля',u'Вода',u'Огонь',u'Вода'])
        self.assertEqual(a.chart_elements[8], [u'Земля:Бык',u'Земля',u'Огонь',u'Земля',u'Вода'])
        self.assertEqual(a.chart_elements[9], [u'Железо:Бык',u'Земля',u'Земля',u'Железо',u'Вода'])
        self.assertEqual(a.chart_elements[10], [u'Земля:Свинья',u'Вода',u'Дерево',u'Земля',u'Огонь'])

        self.assertEqual(a.chart_elements[11], [u'Железо:Петух',u'Железо',u'Дерево',u'Железо',u'Вода'])
        self.assertEqual(a.chart_elements[12], [u'Вода:Дракон',u'Земля',u'Вода',u'Вода',u'Дерево'])
        self.assertEqual(a.chart_elements[13], [u'Огонь:Лошадь',u'Огонь',u'Вода',u'Огонь',u'Железо'])
        self.assertEqual(a.chart_elements[14], [u'Вода:Тигр',u'Дерево',u'Железо',u'Вода',u'Железо'])
        self.assertEqual(a.chart_elements[15], [u'Земля:Лошадь',u'Огонь',u'Огонь',u'Земля',u'Железо'])

        r = [
            ['','','','','','','','','','','','','','','','',''],
            ['','O','O','O','O','O',   'O','O','O','O','O',         'X','O','X/O','X','X/O',  'O'],
            ['','O','X','O','O','X/O', 'O','O','O','X','X/O',       'X/O','O','O','O','O',    'O'],
            ['','X','X/O','X','X','O', 'X','X/O','O','X','O',       'X','O','X/O','O','O',    'X/O'],
            ['','O','O','O','O','O',   'X/O','X/O','X/O','X/O','X', 'X/O','O','X','X','X',     'O'],
            ['','O','O','O','O','O',   'O','O','O','X','O',         'X','O','X/O','X/O','O',   '']
            ]
        res = zip(*r)
        a.do_stones()
        for i in range(17):
            self.assertEqual(tuple(a.chart_stones[i]), res[i])

if __name__ == '__main__':
    unittest.main()

