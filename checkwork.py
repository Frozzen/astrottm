# -*- coding: utf-8 -*-
"""
контрольная хосмыча

Мои результаты:
1.сын - вода,друг - дерево, враг-огонь, мать - земля.
2. По руке получается Крыса в таблице указана Свинья (1959г)!
3. Сог - железо, лю -земля, ван-земля, лун - вода, ла -земля
4.м 18лет — кхон земля
ж 43 года — та железо.
5. год, согме, люме, ванме, лунме, павме
1970(Железная Собака), 9, 3, 6, 8, 4
1967, 3, 6, 9, 2,7 Огненный баран.
6. на 2001г м43 (1958г р) — водяная обезьяна, ж 29 (1972г р) — водяной дракон.
7. месяц — железная обезьяна, день — деревянной лошади, час - земляной тигр.
8.согтаркут - 9, лютаркут - 5, вантаркут - 5, лунтаркут 8.
9. год сын

"""
from __future__ import print_function

__author__ = 'goncharov'
import basedata, branches, fruit

def main():
        a = basedata.BaseAstrology(1960)
        print("#2 жпгр:", a.get_elements()['animal'])
        a = basedata.BaseAstrology(1969)
        e = a.get_elements()
        print(u"#3 5 инд.сил: Сог:%s Лю:%s Ван:%s Лун:%s Ла:%s" % (e['sog'], e['lu'], e['wang'], e['lung'], e['la']))

        print(u"#4 парка Мужчины:%s 18и, женщины:%s 43" % (a.get_parka(1969+18, element=True),
                                                           a.get_parka(1969+43, 'woman', True)))
        a = basedata.BaseAstrology(1970)
        m = a.get_mevas(2001)
        print(u"#5 мева рожденого в 1970 на 2001: согме:%s люме:%s ванме:%s лунме:%s павме:%s "
              % (m['sogme'], m['lume'], m['wangme'], m['lunme'], m['pawme']))
        a = basedata.BaseAstrology(1967)
        m = a.get_mevas(2001)
        print(u"#5 мева рожденого в 1967 на 2001: согме:%s люме:%s ванме:%s лунме:%s павме:%s "
              % (m['sogme'], m['lume'], m['wangme'], m['lunme'], m['pawme']))
        a = basedata.BaseAstrology(1958)
        l = a.get_logmen(2001)
        print(u"#6 логмен мужчины 43х на 2001: %s %s" % (l[0], l[1]))
        a = basedata.BaseAstrology(1972)
        l = a.get_logmen(2001, 'woman')
        print(u"#6 логмен женщины 29х на 2001: %s %s" % (l[0], l[1]))

        a = basedata.BaseAstrology(1973)
        m = a.get_months_of_year(1973)
        d = a.get_days_of_month(m[6])
        h = a.get_hours_of_day(d[16])
        print(u"#7 признаки месяца:%s дня:%s часа:%s родившегося в год водяного быка перед рассветом" %
              (m[6][0]+' '+m[6][1], d[16][1]+' '+d[16][2], h[11][1]+' '+h[11][2]))

        a = basedata.BaseAstrology(1970)
        t = a.get_tarkut(1970, 5, 17, 7)
        print(u"#8 таркут родившегося 17 числа 5 л.месяца года ЖелСобаки: сог:%s лю:%s ван:%s лун:%s" %
              (t['sogtarkut'], t['lutarkut'], t['wangtarkut'], t['lungtarkut']))

        a = basedata.BaseAstrology(1950)
        t = a.get_tribal(u'Вода')
        print(u"#9 Качество родового элемента вода для человека 1950 гр:%s" % t)

        a = basedata.BaseAstrology(1976)
        l = a.get_logmen(2016, 'man')
        p = a.get_parka(2016, 'man')
        pm = a.get_mevas(2016)['pawme']
        print(u"#доп муж: 1976гр на 2016 логмен:%s %s, парка:%s, павме:%s" % (l[0], l[1], p, pm))

        l = a.get_logmen(2016, 'woman')
        p = a.get_parka(2016, 'woman')
        pm = a.get_mevas(2016)['pawme']
        print(u"#доп жен: 1976гр на 2016 логмен:%s %s, парка:%s, павме:%s" % (l[0], l[1], p, pm))

        print("\nДерево жмзни\n15 ветвей")
        b = branches.Branches15(1963, u'Вода', 'man')
        b.compute(2016)
        b.do_stones()
        b.print_all()

        print("\nДерево жмзни\n300 листьев")
        for el in b.astro.element_list:
            c = branches.Branches15(1963, el, 'man')
            c.compute(2016)
            c.do_stones()
            c.print_stones()

        print("16 плодов")
        a = fruit.Fruit16(1963)
        a.calc(2016, 8, 1, 5)
        a.print_el()

        a = basedata.BaseAstrology(1963)
        l = a.get_logmen(2016, 'man')
        print(u"Выпавший логмен:%s %s" % l)

        p = a.get_parka(2016, 'man')
        print(u"ПавПар:%s " % p)

        m = a.get_mevas(2016)
        print(u"ПавМе:%s " % m['pawme'])

if __name__ == '__main__':
    main()

