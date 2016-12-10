# -*- coding: utf-8 -*-
"""
все гороскопы в куче. вызов

all_horo.py --birth=1963 --year=2016


"""
from __future__ import print_function

__author__ = 'goncharov'

import  basedata, branches
import getopt, sys

def usage():
    print(__doc__)
    sys.exit(1)

def main(birth_year, year):


    a = basedata.BaseAstrology(birth_year)
    e = a.get_elements()
    print(u"#3 5 инд.сил: Сог:%s Лю:%s Ван:%s Лун:%s Ла:%s" % (e['sog'], e['lu'], e['wang'], e['lung'], e['la']))
    print(u"#4 парка Мужчины:%s 18и, женщины:%s 43" % (a.get_parka(1960+18), a.get_parka(1960+43)))
    m = a.get_mevas(year)
    print(u"#5 мева рожденого в %d на %d: согме:%s люме:%s ванме:%s лунме:%s павме:%s "
          % (birth_year, year, m['sogme'], m['lume'], m['wangme'], m['lunme'], m['pawme']))
    l = a.get_logmen(year)
    print(u"#6 логмен мужчины: %s %s" % (l[0], l[1]))

    m = a.get_months_of_year(year)
    d = a.get_days_of_month(m[6])
    h = a.get_hours_of_day(d[15])
    print(u"#7 признаки месяца:%s дня:%s часа:%s родившегося в год водяного быка перед рассветом" %
          (m[6][0]+' '+m[6][1], d[6][1]+' '+d[6][2], h[11][1]+' '+h[11][2]))

    t = a.get_tarkut(1970, 5, 17, 7)
    print(u"#8 таркут родившегося 17 числа 5 л.месяца года ЖелСобаки: сог:%s лю:%s ван:%s лун:%s" %
          (t['sogtarkut'], t['lutarkut'], t['wangtarkut'], t['lungtarkut']))

    t = a.get_tribal(u'Вода')
    print(u"#9 Качество родового элемента вода:%s" % t)
    p = a.get_parka(year, 'man')
    pd = a.get_parka_direction(p)
    print("направление парка:",pd)

    print("15 вевей:")
    for i in range(5):
        ba = branches.Branches15(birth_year, i, 'man')
        ba.compute(year)
        ba.do_stones()
        ba.print_stones()



if __name__ == '__main__':
    year = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "b:y:",["birth=",  "year="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()

    for o, a in opts:
        if o in ("-b",  "--birth"):
            birth = int(a)
        elif o in ("-y",  "--year"):
            year = int(a)
        else:
            usage()
    main(birth, year)
