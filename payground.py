# -*- coding: utf-8 -*-
"""
развлекаемся
"""
from __future__ import print_function

__author__ = 'goncharov'
import basedata

def main():
        a = basedata.BaseAstrology(1970)
        l = a.get_logmen(2016, 'man')
        p = a.get_parka(2016, 'man')
        pm = a.get_mevas(2016)['pawme']
        print(u"#доп муж: 1976гр на 2016 логмен:%s %s, парка:%s, павме:%s" % (l[0], l[1], p, pm))

        l = a.get_logmen(2016, 'woman')
        p = a.get_parka(2016, 'woman')
        pm = a.get_mevas(2016)['pawme']
        print(u"#доп жен: 1976гр на 2016 логмен:%s %s, парка:%s, павме:%s" % (l[0], l[1], p, pm))

        a = basedata.BaseAstrology(1963)
        m = a.get_mevas(2016)
        print(u"мева рожденого в 1963 на 2016: согме:%s люме:%s ванме:%s лунме:%s павме:%s "
              % (m['sogme'], m['lume'], m['wangme'], m['lunme'], m['pawme']))
        m = a.get_mevas(2017)
        print(u"мева рожденого в 1963 на 2017: согме:%s люме:%s ванме:%s лунме:%s павме:%s "
              % (m['sogme'], m['lume'], m['wangme'], m['lunme'], m['pawme']))

        a = basedata.BaseAstrology(1972)
        m = a.get_mevas(2016)
        print(u"мева рожденого в 1972 на 2016: согме:%s люме:%s ванме:%s лунме:%s павме:%s "
              % (m['sogme'], m['lume'], m['wangme'], m['lunme'], m['pawme']))
        m = a.get_mevas(2017)
        print(u"мева рожденого в 1972 на 2017: согме:%s люме:%s ванме:%s лунме:%s павме:%s "
              % (m['sogme'], m['lume'], m['wangme'], m['lunme'], m['pawme']))

        a = basedata.BaseAstrology(2016)
        m = a.get_mevas(2016)
        print(u"мева рожденого в 2016 на 2016: согме:%s люме:%s ванме:%s лунме:%s павме:%s "
              % (m['sogme'], m['lume'], m['wangme'], m['lunme'], m['pawme']))

        a = basedata.BaseAstrology(2017)
        m = a.get_mevas(2017)
        print(u"мева рожденого в 2017 на 2017: согме:%s люме:%s ванме:%s лунме:%s павме:%s "
              % (m['sogme'], m['lume'], m['wangme'], m['lunme'], m['pawme']))

        a = basedata.BaseAstrology(1962)
        m = a.get_mevas(2016)
        print(u"мева оли козыревой на 2016: согме:%s люме:%s ванме:%s лунме:%s павме:%s "
              % (m['sogme'], m['lume'], m['wangme'], m['lunme'], m['pawme']))
        m = a.get_mevas(2017)
        print(u"мева оли козыревой на 2017: согме:%s люме:%s ванме:%s лунме:%s павме:%s "
              % (m['sogme'], m['lume'], m['wangme'], m['lunme'], m['pawme']))

        a = basedata.BaseAstrology(1988)
        m = a.get_mevas(2016)
        print(u"мева николаева на 2016: согме:%s люме:%s ванме:%s лунме:%s павме:%s "
              % (m['sogme'], m['lume'], m['wangme'], m['lunme'], m['pawme']))

if __name__ == '__main__':
    main()

