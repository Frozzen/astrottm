# -*- coding: utf-8 -*-
"""
    вычисляем основные данные и таблицы по астрологии

"""
from __future__ import print_function

data_5elements = u"""1984:Деревянная:Крыса:Вода:Железо:Дерево:Дерево:Железо
1985:Деревянный:Бык:Земля:Железо:Дерево:Вода:Огонь
1986:Огненный:Тигр:Дерево:Огонь:Огонь:Железо:Вода
1987:Огненный:Кролик:Дерево:Огонь:Огонь:Огонь:Вода
1988:Земляной:Дракон:Земля:Дерево:Земля:Дерево:Огонь
1989:Земляная:Змея:Огонь:Дерево:Земля:Вода:Дерево
1990:Железная:Лошадь:Огонь:Земля:Железо:Железо:Дерево
1991:Железный:Баран:Земля:Земля:Железо:Огонь:Огонь
1992:Водяная:Обезьяна:Железо:Железо:Вода:Дерево:Земля
1993:Водяной:Петух:Железо:Железо:Вода:Вода:Земля
1994:Деревянная:Собака:Земля:Огонь:Дерево:Железо:Огонь
1995:Деревянная:Свинья:Вода:Огонь:Дерево:Огонь:Железо
1996:Огненная:Крыса:Вода:Вода:Огонь:Дерево:Железо
1997:Огненный:Бык:Земля:Вода:Огонь:Вода:Огонь
1998:Земляной:Тигр:Дерево:Земля:Земля:Железо:Вода
1999:Земляной:Кролик:Дерево:Земля:Земля:Огонь:Вода
2000:Железный:Дракон:Земля:Железо:Железо:Дерево:Огонь
2001:Железная:Змея:Огонь:Железо:Железо:Вода:Дерево
2002:Водяная:Лошадь:Огонь:Дерево:Вода:Железо:Дерево
2003:Водяной:Баран:Земля:Дерево:Вода:Огонь:Огонь
2004:Деревянная:Обезьяна:Железо:Вода:Дерево:Дерево:Земля
2005:Деревянный:Петух:Железо:Вода:Дерево:Вода:Земля
2006:Огненная:Собака:Земля:Земля:Огонь:Железо:Огонь
2007:Огненная:Свинья:Вода:Земля:Огонь:Огонь:Железо
2008:Земляная:Крыса:Вода:Огонь:Земля:Дерево:Железо
2009:Земляной:Бык:Земля:Огонь:Земля:Вода:Огонь
2010:Железный:Тигр:Дерево:Дерево:Железо:Железо:Вода
2011:Железный:Кролик:Дерево:Дерево:Железо:Огонь:Вода
2012:Водяной:Дракон:Земля:Вода:Вода:Дерево:Огонь
2013:Водяная:Змея:Огонь:Вода:Вода:Вода:Дерево
2014:Деревянная:Лошадь:Огонь:Железо:Дерево:Железо:Дерево
2015:Деревянный:Баран:Земля:Железо:Дерево:Огонь:Огонь
2016:Огненная:Обезьяна:Железо:Огонь:Огонь:Дерево:Земля
2017:Огненный:Петух:Железо:Огонь:Огонь:Вода:Земля
2018:Земляная:Собака:Земля:Дерево:Земля:Железо:Огонь
2019:Земляная:Свинья:Вода:Дерево:Земля:Огонь:Железо
2020:Железная:Крыса:Вода:Земля:Железо:Дерево:Железо
2021:Железный:Бык:Земля:Земля:Железо:Вода:Огонь
2022:Водяной:Тигр:Дерево:Железо:Вода:Железо:Вода
2023:Водяной:Кролик:Дерево:Железо:Вода:Огонь:Вода
2024:Деревянный:Дракон:Земля:Огонь:Дерево:Дерево:Огонь
2025:Деревянная:Змея:Огонь:Огонь:Дерево:Вода:Дерево
2026:Огненная:Лошадь:Огонь:Вода:Огонь:Железо:Дерево
2027:Огненный:Баран:Земля:Вода:Огонь:Огонь:Огонь
2028:Земляная:Обезьяна:Железо:Земля:Земля:Дерево:Земля
2029:Земляной:Петух:Железо:Земля:Земля:Вода:Земля
2030:Железная:Собака:Земля:Железо:Железо:Железо:Огонь
2031:Железная:Свинья:Вода:Железо:Железо:Огонь:Железо
2032:Водяная:Крыса:Вода:Дерево:Вода:Дерево:Железо
2033:Водяной:Бык:Земля:Дерево:Вода:Вода:Огонь
2034:Деревянный:Тигр:Дерево:Вода:Дерево:Железо:Вода
2035:Деревянный:Кролик:Дерево:Вода:Дерево:Огонь:Вода
2036:Огненный:Дракон:Земля:Земля:Огонь:Дерево:Огонь
2037:Огненная:Змея:Огонь:Земля:Огонь:Вода:Дерево
2038:Земляная:Лошадь:Огонь:Огонь:Земля:Железо:Дерево
2039:Земляной:Баран:Земля:Огонь:Земля:Огонь:Огонь
2040:Железная:Обезьяна:Железо:Дерево:Железо:Дерево:Земля
2041:Железный:Петух:Железо:Дерево:Железо:Вода:Земля
2042:Водяная:Собака:Земля:Вода:Вода:Железо:Огонь
2043:Водяная:Свинья:Вода:Вода:Вода:Огонь:Железо
1924:Деревянная:Крыса:Вода:Железо:Дерево:Дерево:Железо
1925:Деревянный:Бык:Земля:Железо:Дерево:Вода:Огонь
1926:Огненный:Тигр:Дерево:Огонь:Огонь:Железо:Вода
1927:Огненный:Кролик:Дерево:Огонь:Огонь:Огонь:Вода
1928:Земляной:Дракон:Земля:Дерево:Земля:Дерево:Огонь
1929:Земляная:Змея:Огонь:Дерево:Земля:Вода:Дерево
1930:Железная:Лошадь:Огонь:Земля:Железо:Железо:Дерево
1931:Железный:Баран:Земля:Земля:Железо:Огонь:Огонь
1932:Водяная:Обезьяна:Железо:Железо:Вода:Дерево:Земля
1933:Водяной:Петух:Железо:Железо:Вода:Вода:Земля
1934:Деревянная:Собака:Земля:Огонь:Дерево:Железо:Огонь
1935:Деревянная:Свинья:Вода:Огонь:Дерево:Огонь:Железо
1936:Огненная:Крыса:Вода:Вода:Огонь:Дерево:Железо
1937:Огненный:Бык:Земля:Вода:Огонь:Вода:Огонь
1938:Земляной:Тигр:Дерево:Земля:Земля:Железо:Вода
1939:Земляной:Кролик:Дерево:Земля:Земля:Огонь:Вода
1940:Железный:Дракон:Земля:Железо:Железо:Дерево:Огонь
1941:Железная:Змея:Огонь:Железо:Железо:Вода:Дерево
1942:Водяная:   Лошадь:Огонь:Дерево:Вода:Железо:Дерево
1943:Водяной:Баран:Земля:Дерево:Вода:Огонь:Огонь
1944:Деревянная:Обезьяна:Железо:Вода:Дерево:Дерево:Земля
1945:Деревянный:Петух:Железо:Вода:Дерево:Вода:Земля
1946:Огненная:Собака:Земля:Земля:Огонь:Железо:Огонь
1947:Огненная:Свинья:Вода:Земля:Огонь:Огонь:Железо
1948:Земляная:Крыса:Вода:Огонь:Земля:Дерево:Железо
1949:Земляной:Бык:Земля:Огонь:Земля:Вода:Огонь
1950:Железный:Тигр:Дерево:Дерево:Железо:Железо:Вода
1951:Железный:Кролик:Дерево:Дерево:Железо:Огонь:Вода
1952:Водяной:Дракон:Земля:Вода:Вода:Дерево:Огонь
1953:Водяная:Змея:Огонь:Вода:Вода:Вода:Дерево
1954:Деревянная:Лошадь:Огонь:Железо:Дерево:Железо:Дерево
1955:Деревянный:Баран:Земля:Железо:Дерево:Огонь:Огонь
1956:Огненная:Обезьяна:Железо:Огонь:Огонь:Дерево:Земля
1957:Огненный:Петух:Железо:Огонь:Огонь:Вода:Земля
1958:Земляная:Собака:Земля:Дерево:Земля:Железо:Огонь
1959:Земляная:Свинья:Вода:Дерево:Земля:Огонь:Железо
1960:Железная:Крыса:Вода:Земля:Железо:Дерево:Железо
1961:Железный:Бык:Земля:Земля:Железо:Вода:Огонь
1962:Водяной:Тигр:Дерево:Железо:Вода:Железо:Вода
1963:Водяной:Кролик:Дерево:Железо:Вода:Огонь:Вода
1964:Деревянный:Дракон:Земля:Огонь:Дерево:Дерево:Огонь
1965:Деревянная:Змея:Огонь:Огонь:Дерево:Вода:Дерево
1966:Огненная:Лошадь:Огонь:Вода:Огонь:Железо:Дерево
1967:Огненный:Баран:Земля:Вода:Огонь:Огонь:Огонь
1968:Земляная:Обезьяна:Железо:Земля:Земля:Дерево:Земля
1969:Земляной:Петух:Железо:Земля:Земля:Вода:Земля
1970:Железная:Собака:Земля:Железо:Железо:Железо:Огонь
1971:Железная:Свинья:Вода:Железо:Железо:Огонь:Железо
1972:Водяная:Крыса:Вода:Дерево:Вода:Дерево:Железо
1973:Водяной:Бык:Земля:Дерево:Вода:Вода:Огонь
1974:Деревянный:Тигр:Дерево:Вода:Дерево:Железо:Вода
1975:Деревянный:Кролик:Дерево:Вода:Дерево:Огонь:Вода
1976:Огненный:Дракон:Земля:Земля:Огонь:Дерево:Огонь
1977:Огненная:Змея:Огонь:Земля:Огонь:Вода:Дерево
1978:Земляная:Лошадь:Огонь:Огонь:Земля:Железо:Дерево
1979:Земляной:Баран:Земля:Огонь:Земля:Огонь:Огонь
1980:Железная:Обезьяна:Железо:Дерево:Железо:Дерево:Земля
1981:Железный:Петух:Железо:Дерево:Железо:Вода:Земля
1982:Водяная:Собака:Земля:Вода:Вода:Железо:Огонь
1983:Водяная:Свинья:Вода:Вода:Вода:Огонь:Железо
1984:Деревянная:Крыса:Вода:Железо:Дерево:Дерево:Железо
1985:Деревянный:Бык:Земля:Железо:Дерево:Вода:Огонь
1986:Огненный:Тигр:Дерево:Огонь:Огонь:Железо:Вода
1987:Огненный:Кролик:Дерево:Огонь:Огонь:Огонь:Вода
1988:Земляной:Дракон:Земля:Дерево:Земля:Дерево:Огонь
1989:Земляная:Змея:Огонь:Дерево:Земля:Вода:Дерево
1990:Железная:Лошадь:Огонь:Земля:Железо:Железо:Дерево
1991:Железный:Баран:Земля:Земля:Железо:Огонь:Огонь
1992:Водяная:Обезьяна:Железо:Железо:Вода:Дерево:Земля
1993:Водяной:Петух:Железо:Железо:Вода:Вода:Земля
1994:Деревянная:Собака:Земля:Огонь:Дерево:Железо:Огонь
1995:Деревянная:Свинья:Вода:Огонь:Дерево:Огонь:Железо
1996:Огненная:Крыса:Вода:Вода:Огонь:Дерево:Железо
1997:Огненный:Бык:Земля:Вода:Огонь:Вода:Огонь
1998:Земляной:Тигр:Дерево:Земля:Земля:Железо:Вода
1999:Земляной:Кролик:Дерево:Земля:Земля:Огонь:Вода
2000:Железный:Дракон:Земля:Железо:Железо:Дерево:Огонь
2001:Железная:Змея:Огонь:Железо:Железо:Вода:Дерево
2002:Водяная:Лошадь:Огонь:Дерево:Вода:Железо:Дерево
2003:Водяной:Баран:Земля:Дерево:Вода:Огонь:Огонь
2004:Деревянная:Обезьяна:Железо:Вода:Дерево:Дерево:Земля
2005:Деревянный:Петух:Железо:Вода:Дерево:Вода:Земля
2006:Огненная:Собака:Земля:Земля:Огонь:Железо:Огонь
2007:Огненная:Свинья:Вода:Земля:Огонь:Огонь:Железо
2008:Земляная:Крыса:Вода:Огонь:Земля:Дерево:Железо
2009:Земляной:Бык:Земля:Огонь:Земля:Вода:Огонь
2010:Железный:Тигр:Дерево:Дерево:Железо:Железо:Вода
2011:Железный:Кролик:Дерево:Дерево:Железо:Огонь:Вода
2012:Водяной:Дракон:Земля:Вода:Вода:Дерево:Огонь
2013:Водяная:Змея:Огонь:Вода:Вода:Вода:Дерево
2014:Деревянная:Лошадь:Огонь:Железо:Дерево:Железо:Дерево
2015:Деревянный:Баран:Земля:Железо:Дерево:Огонь:Огонь
2016:Огненная:Обезьяна:Железо:Огонь:Огонь:Дерево:Земля
2017:Огненный:Петух:Железо:Огонь:Огонь:Вода:Земля
2018:Земляная:Собака:Земля:Дерево:Земля:Железо:Огонь
2019:Земляная:Свинья:Вода:Дерево:Земля:Огонь:Железо
2020:Железная:Крыса:Вода:Земля:Железо:Дерево:Железо
2021:Железный:Бык:Земля:Земля:Железо:Вода:Огонь
2022:Водяной:Тигр:Дерево:Железо:Вода:Железо:Вода
2023:Водяной:Кролик:Дерево:Железо:Вода:Огонь:Вода
2024:Деревянный:Дракон:Земля:Огонь:Дерево:Дерево:Огонь
2025:Деревянная:Змея:Огонь:Огонь:Дерево:Вода:Дерево
2026:Огненная:Лошадь:Огонь:Вода:Огонь:Железо:Дерево
2027:Огненный:Баран:Земля:Вода:Огонь:Огонь:Огонь
2028:Земляная:Обезьяна:Железо:Земля:Земля:Дерево:Земля
2029:Земляной:Петух:Железо:Земля:Земля:Вода:Земля
2030:Железная:Собака:Земля:Железо:Железо:Железо:Огонь
2031:Железная:Свинья:Вода:Железо:Железо:Огонь:Железо
2032:Водяная:Крыса:Вода:Дерево:Вода:Дерево:Железо
2033:Водяной:Бык:Земля:Дерево:Вода:Вода:Огонь
2034:Деревянный:Тигр:Дерево:Вода:Дерево:Железо:Вода
2035:Деревянный:Кролик:Дерево:Вода:Дерево:Огонь:Вода
2036:Огненный:Дракон:Земля:Земля:Огонь:Дерево:Огонь
2037:Огненная:Змея:Огонь:Земля:Огонь:Вода:Дерево
2038:Земляная:Лошадь:Огонь:Огонь:Земля:Железо:Дерево
2039:Земляной:Баран:Земля:Огонь:Земля:Огонь:Огонь
2040:Железная:Обезьяна:Железо:Дерево:Железо:Дерево:Земля
2041:Железный:Петух:Железо:Дерево:Железо:Вода:Земля
2042:Водяная:Собака:Земля:Вода:Вода:Железо:Огонь
2043:Водяная:Свинья:Вода:Вода:Вода:Огонь:Железо"""

data_relations = u"""Дерево:Вода:Мать
Дерево:Дерево:-
Огонь:Огонь:-
Земля:Земля:-
Вода:Вода:-
Железо:Железо:-
Огонь:Дерево:Мать
Земля:Огонь:Мать
Железо:Земля:Мать
Вода:Железо:Мать
Дерево:Огонь:Сын
Огонь:Земля:Сын
Земля:Железо:Сын
Железо:Вода:Сын
Вода:Дерево:Сын
Дерево:Земля:Друг
Огонь:Железо:Друг
Земля:Вода:Друг
Железо:Дерево:Друг
Вода:Огонь:Друг
Дерево:Железо:Враг
Огонь:Вода:Враг
Земля:Дерево:Враг
Железо:Огонь:Враг
Вода:Земля:Враг"""

data_parka = u"""ли:огонь:младшая дочь:Ю
кхон:земля:мать:ЮЗ
та:железо:младший сын:З
кхен:земля:отец:СЗ
кхам:вода:внук:С
кин:земля:старший сын:СВ
син:дерево:внучка:В
сон:земля:старшая дочь:ЮВ"""

data_parka_directions = u"""3:4:12:4:3:21:12:22:3
1:сон:23:2:ли:12:13:кхон:4
14:2:13:13:1:14:2:14:1
1:2:13::::24:12:4
3:син:14::::14:та:3
25:4:12::::1:13:2
14:13:2:2:1:14:13:14:1
26:кин:1:4:кхам:13:12:кхен:2
3:12:4:12:3:27:4:28:3"""

data_parka_codes = u"""1:Небесное лекарство
2:Поддержка жизни
3:Реализация счастливой судьбы
4:Порождение процветания
11:Истощение тела
12:Пять злых духов
13:Зло
14:Демон отсечения
21:истощение голова
22:истощение левая рука
23:истощение правая рука
24:истощение левое плечо
25:истощение правое плечо
26:истощение правая нога
27:истощение пенис
28:истощение левая нога
ли:ли
кхон:кхон
та:та
кхен:кхен
кхам:кхам
кин:кин
син:син
сон:сон"""

data_meva = u"""1 Белая:является зеркалом духов врачевания МЭН
2 Чёрная:является зеркалом злых демонов ДУТ
3 Синяя:является зеркалом озёрных духов ЦО МЭН
4 Зелёная:является зеркалом НАГОВ (ЛУ)
5 Жёлтая:является зеркалом духов ДЖАЛА
6 Белая:является зеркалом духов умерших правителей ГЬЯЛПО
7 Красная:является зеркалом свирепых духов ЦЭН
8 Белая:является зеркалом божеств местности ЮЛЛХА
9 Красная:является зеркалом божеств благополучия ЯНГ"""

data_meva_rect = u"""4:9:2
3:5:7
8:1:6"""

data_animal_recode = {
    u'Деревянный': u'Дерево',
    u'Деревянная': u'Дерево',
    u'Огненный': u'Огонь',
    u'Огненная': u'Огонь',
    u'Земляной': u'Земля',
    u'Земляная': u'Земля',
    u'Железный': u'Железо',
    u'Железная': u'Железо',
    u'Водяной': u'Вода',
    u'Водяная': u'Вода',
}
data_metreng = u"""1:1864:1:Деревянная Крыса
9:1865:1:Деревянный Бык
8:1866:1:Огненный Тигр
7:1867:1:Огненный Кролик
6:1868:1:Земляной Дракон
5:1869:1:Земляная Змея
4:1870:1:Железная Лошадь
3:1871:1:Железный Баран
2:1872:1:Водяная Обезьяна
1:1873:1:Водяной Петух
9:1874:1:Деревянная Собака
8:1875:1:Деревянная Свинья
7:1876:1:Огненная Крыса
6:1877:1:Огненный Бык
5:1878:1:Земляной Тигр
4:1879:1:Земляной Кролик
3:1880:1:Железный Дракон
2:1881:1:Железная Змея
1:1882:1:Водяная Лошадь
9:1883:1:Водяной Баран
8:1884:1:Деревянная Обезьяна
7:1885:1:Деревянный Петух
6:1886:1:Огненная Собака
5:1887:1:Огненная Свинья
4:1888:1:Земляная Крыса
3:1889:1:Земляной Бык
2:1890:1:Железный Тигр
1:1891:1:Железный Кролик
9:1892:1:Водяной Дракон
8:1893:1:Водяная Змея
7:1894:1:Деревянная Лошадь
6:1895:1:Деревянный Баран
5:1896:1:Огненная Обезьяна
4:1897:1:Огненный Петух
3:1898:1:Земляная Собака
2:1899:1:Земляная Свинья
1:1900:1:Железная Крыса
9:1901:1:Железный Бык
8:1902:1:Водяной Тигр
7:1903:1:Водяной Кролик
6:1904:1:Деревянный Дракон
5:1905:1:Деревянная Змея
4:1906:1:Огненная Лошадь
3:1907:1:Огненный Баран
2:1908:1:Земляная Обезьяна
1:1909:1:Земляной Петух
9:1910:1:Железная Собака
8:1911:1:Железная Свинья
7:1912:1:Водяная Крыса
6:1913:1:Водяной Бык
5:1914:1:Деревянный Тигр
4:1915:1:Деревянный Кролик
3:1916:1:Огненный Дракон
2:1917:1:Огненная Змея
1:1918:1:Земляная Лошадь
9:1919:1:Земляной Баран
8:1920:1:Железная Обезьяна
7:1921:1:Железный Петух
6:1922:1:Водяная Собака
5:1923:1:Водяная Свинья
4:1924:2:Деревянная Крыса
3:1925:2:Деревянный Бык
2:1926:2:Огненный Тигр
1:1927:2:Огненный Кролик
9:1928:2:Земляной Дракон
8:1929:2:Земляная Змея
7:1930:2:Железная Лошадь
6:1931:2:Железный Баран
5:1932:2:Водяная Обезьяна
4:1933:2:Водяной Петух
3:1934:2:Деревянная Собака
2:1935:2:Деревянная Свинья
1:1936:2:Огненная Крыса
9:1937:2:Огненный Бык
8:1938:2:Земляной Тигр
7:1939:2:Земляной Кролик
6:1940:2:Железный Дракон
5:1941:2:Железная Змея
4:1942:2:Водяная Лошадь
3:1943:2:Водяной Баран
2:1944:2:Деревянная Обезьяна
1:1945:2:Деревянный Петух
9:1946:2:Огненная Собака
8:1947:2:Огненная Свинья
7:1948:2:Земляная Крыса
6:1949:2:Земляной Бык
5:1950:2:Железный Тигр
4:1951:2:Железный Кролик
3:1952:2:Водяной Дракон
2:1953:2:Водяная Змея
1:1954:2:Деревянная Лошадь
9:1955:2:Деревянный Баран
8:1956:2:Огненная Обезьяна
7:1957:2:Огненный Петух
6:1958:2:Земляная Собака
5:1959:2:Земляная Свинья
4:1960:2:Железная Крыса
3:1961:2:Железный Бык
2:1962:2:Водяной Тигр
1:1963:2:Водяной Кролик
9:1964:2:Деревянный Дракон
8:1965:2:Деревянная Змея
7:1966:2:Огненная Лошадь
6:1967:2:Огненный Баран
5:1968:2:Земляная Обезьяна
4:1969:2:Земляной Петух
3:1970:2:Железная Собака
2:1971:2:Железная Свинья
1:1972:2:Водяная Крыса
9:1973:2:Водяной Бык
8:1974:2:Деревянный Тигр
7:1975:2:Деревянный Кролик
6:1976:2:Огненный Дракон
5:1977:2:Огненная Змея
4:1978:2:Земляная Лошадь
3:1979:2:Земляной Баран
2:1980:2:Железная Обезьяна
1:1981:2:Железный Петух
9:1982:2:Водяная Собака
8:1983:2:Водяная Свинья
7:1984:3:Деревянная Крыса
6:1985:3:Деревянный Бык
5:1986:3:Огненный Тигр
4:1987:3:Огненный Кролик
3:1988:3:Земляной Дракон
2:1989:3:Земляная Змея
1:1990:3:Железная Лошадь
9:1991:3:Железный Баран
8:1992:3:Водяная Обезьяна
7:1993:3:Водяной Петух
6:1994:3:Деревянная Собака
5:1995:3:Деревянная Свинья
4:1996:3:Огненная Крыса
3:1997:3:Огненный Бык
2:1998:3:Земляной Тигр
1:1999:3:Земляной Кролик
9:2000:3:Железный Дракон
8:2001:3:Железная Змея
7:2002:3:Водяная Лошадь
6:2003:3:Водяной Баран
5:2004:3:Деревянная Обезьяна
4:2005:3:Деревянный Петух
3:2006:3:Огненная Собака
2:2007:3:Огненная Свинья
1:2008:3:Земляная Крыса
9:2009:3:Земляной Бык
8:2010:3:Железный Тигр
7:2011:3:Железный Кролик
6:2012:3:Водяной Дракон
5:2013:3:Водяная Змея
4:2014:3:Деревянная Лошадь
3:2015:3:Деревянный Баран
2:2016:3:Огненная Обезьяна
1:2017:3:Огненный Петух
9:2018:3:Земляная Собака
8:2019:3:Земляная Свинья
7:2020:3:Железная Крыса
6:2021:3:Железный Бык
5:2022:3:Водяной Тигр
4:2023:3:Водяной Кролик
3:2024:3:Деревянный Дракон
2:2025:3:Деревянная Змея
1:2026:3:Огненная Лошадь
9:2027:3:Огненный Баран
8:2028:3:Земляная Обезьяна
7:2029:3:Земляной Петух
6:2030:3:Железная Собака
5:2031:3:Железная Свинья
4:2032:3:Водяная Крыса
3:2033:3:Водяной Бык
2:2034:3:Деревянный Тигр
1:2035:3:Деревянный Кролик
9:2036:3:Огненный Дракон
8:2037:3:Огненная Змея
7:2038:3:Земляная Лошадь
6:2039:3:Земляной Баран
5:2040:3:Железная Обезьяна
4:2041:3:Железный Петух
3:2042:3:Водяная Собака
2:2043:3:Водяная Свинья"""


class AstroException(Exception):
    pass


class BaseAstrology:
    """

    """
    hour_animal_list = [
        u'Кролик',
        u'Дракон', u'Змея', u'Лошадь', u'Баран', u'Обезьяна',
        u'Петух',
        u'Собака', u'Свинья', u'Крыса', u'Корова', u'Тигр',
    ]
    forces_list = (u'sog', u'lu', u'wang', u'lung', u'la')
    element_list = (u'Дерево', u'Огонь', u'Земля', u'Железо', u'Вода')
    animal_list = (
        u'Тигр', u'Кролик', u'Дракон', u'Змея', u'Лошадь', u'Баран',
        u'Обезьяна', u'Петух', u'Собака', u'Свинья', u'Крыса', u'Корова',
    )

    year_sex = {
        u'Тигр': u'мужской', u'Кролик': u'женский',
        u'Дракон': u'мужской', u'Змея': u'женский',
        u'Лошадь': u'мужской', u'Баран': u'женский',
        u'Обезьяна': u'мужской', u'Петух': u'женский',
        u'Собака': u'мужской', u'Свинья': u'женский',
        u'Крыса': u'мужской', u'Корова': u'женский',
    }

    tarkut = [(1, '-', u'Взять дыхание'), (2, '-', u'Матка'),
              (3, '+', u'Формирование тела'), (4, '+', u'Побеги'), (5, '+', u'Омовение'),
              (6, '+', u'Одевание'), (7, '+', u'Деятельность'), (8, '+', u'Процветание'),
              (9, '-', u'Упадок'), (10, '-', u'Болезнь'), (1, '-', u'Смерть'), (1, '-', u'Кладбище'),
              ]
    # кладбище лоя элементов в животном знаке
    tarkut_animal = {u'Железо': u'Корова',
                     u'Земля': u'Дракон', u'Вода': u'Дракон',
                     u'Дерево': u'Баран',
                     u'Огонь': u'Собака'}
    year_element = {u'Тигр': u'Дерево', u'Кролик': u'Дерево',
                    u'Дракон': u'Земля',
                    u'Змея': u'Огонь', u'Лошадь': u'Огонь',
                    u'Баран': u'Земля',
                    u'Обезьяна': u'Железо', u'Петух': u'Железо',
                    u'Собака': u'Земля',
                    u'Свинья': u'Вода', u'Крыса': u'Вода',
                    u'Корова': u'Земля'}

    def __init__(self, year):
        """
        собрать данные на год рождения

        :param year: год рождения
        :return:
        """
        global data_5elements, data_relations, data_parka_directions, data_parka_codes

        self.birth_year = year
        self.elements = {}
        for l in data_5elements.split('\n'):
            a = l.split(':')
            self.elements[int(a[0])] = {'animal': a[2], 'sog': a[3], 'lu': a[4], 'wang': a[5], 'lung': a[6], 'la': a[7]}
        startY = min(self.elements.keys())
        for y in range(1, 120):
            self.elements[startY - 120 + y] = self.elements[startY + y]
            self.elements[startY + 120 + y] = self.elements[startY + y]

        self.relations = {}
        for l in data_relations.split('\n'):
            a = l.split(':')
            nm = "%s:%s" % (a[0], a[1])
            self.relations[nm] = a[2]

        self.parka = []
        for l in data_parka.split('\n'):
            a = l.split(':')
            self.parka.append(a)

        self.parka_directions = []
        for l in data_parka_directions.split('\n'):
            a = l.split(':')
            self.parka_directions.append(a)

        self.parka_codes = {}
        for l in data_parka_codes.split('\n'):
            a = l.split(':')
            self.parka_codes[a[0]] = a[1]

        self.meva = []
        for l in data_meva.split('\n'):
            a = l.split(':')
            self.meva.append(a)

        self.meva_rect = []
        for l in data_meva_rect.split('\n'):
            a = l.split(':')
            self.meva_rect.append(a)

        self.metreng = {}
        for l in data_metreng.split('\n'):
            a = l.split(':')
            self.metreng[int(a[1])] = {'meva': int(a[0]), 'metreng': int(a[2]), 'year': a[3]}

        self.meva_order = [[1, 2], [2, 0], [0, 1], [0, 0], [1, 1], [2, 2], [2, 1], [0, 2], [1, 0]]
        return

    def get_elements(self, year=None):
        """
        вернуть 5 базовых элементов
        ;bdjyjt
        :param year:
        :return:
        """
        if year is None:
            year = self.birth_year
        return self.elements[year]

    def get_relations(self, rfrom, rto):
        """
        вернуть отношения от элемента к элементу

        for k,v in a.relations.iteritems():
            print('отношения:', k, v)
        :param rfrom:
        :param rto:
        :return:
        """
        nm = "%s:%s" % (rfrom, rto)
        return self.relations[nm]

    def find_year(self, element, animal):
        """
        найти год по знакам, вниз от года рождения

        :param element:
        :param animal:
        :return:
        # for y in range(self.birth_year, 1924, -1):
        #     el, an = self.metreng[y]['year'].split(' ')
        #     el = data_animal_recode[el]
        #     if  el == element and an == animal:
        #         return y
        """
        minY = min(self.elements.keys())
        for y in range(self.birth_year, minY, -1):
            if self.elements[y]['wang'] == element and self.elements[y]['animal'] == animal:
                return y
        raise AstroException("incorrect %s:%s pair" % (element, animal))

    def find_relative(self, rfrom, relation):
        """
        найти элемент по отношению рдоства к указанному элементу
        
        :param rfrom: 
        :param relation: сын, мать, друг, враг
        :return:
        """
        for k, v in self.relations.iteritems():
            if k.split(':')[0] == rfrom and v == relation:
                return k.split(':')[1]
        raise AstroException("no relation %s for %s" % (relation, rfrom))

    def cross_relation(self, rfrom, rto, notin=('-', u'Друг', u'Мать', u'Сын')):
        """
        перекрестные отношения сил forces_list от до

        :type rfrom: dict
        :type rto: dict
        :param notin: не учитывать отношения из списка
        :param rfrom:
        :param rto:
        :return:
        """
        cross = {}
        for f in self.forces_list:
            for t in self.forces_list:
                if self.get_relations(rfrom[f], rto[t]) in notin:
                    continue
                nm = "%s:%s" % (f, t)
                cross[nm] = self.get_relations(rfrom[f], rto[t])
        return cross

    def get_parka(self, year, sex='man'):
        """
        вычислить текущую парка года

        :param year:
        :param sex: пол 'man'm 'woman'
        :return:
        """
        if sex == 'man':
            ix = divmod(year - self.birth_year + 1, 8)[1]
            return self.parka[ix - 1][0]
        else:
            ix = divmod(year - self.birth_year + 4, 8)[1]
            return self.parka[8 - ix][0]

    def get_parka_direction(self, parka):
        """
        вернуть направления для парка

        :param parka:
        :return:
        """
        for ix in range(3):
            for iy in range(3):
                if parka == self.parka_directions[ix * 3 + 1][iy * 3 + 1]:
                    r = []
                    for i in range(3):
                        r.append(self.parka_directions[ix * 3 + i][iy * 3:iy * 3 + 3])
                    r2 = []
                    for i in range(3):
                        t = []
                        for j in range(3):
                            t.append(self.parka_codes[r[i][j]])
                        r2.append(t)
                    return r2
        return []

    def __fill_meva_rect(self, year_meva):
        new_meva_rect = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for ix in range(4, 13):
            nix = self.meva_order[ix % 9]
            new_meva_rect[nix[1]][nix[0]] = year_meva
            year_meva = (year_meva + 1)
            if year_meva > 9:
                year_meva = 1
        return new_meva_rect

    def __build_new_meva_rect(self, year):
        age = year - self.birth_year
        age_dir = self.meva_order[((age - 1) % 9 + 5) % 9]  # направление
        year_meva = self.metreng[year]['meva']
        new_meva_rect = self.__fill_meva_rect(year_meva)
        l = new_meva_rect[age_dir[1]][age_dir[0]]
        new_meva_rect = self.__fill_meva_rect(l)
        return l, new_meva_rect

    def __find_in_mentreng(self, animal_metreng, birth_metreng):
        for y, v in self.metreng.iteritems():
            if v['year'] == animal_metreng and v['metreng'] == birth_metreng:
                return y
        raise AstroException('no such metreng:%s %d' % (animal_metreng, birth_metreng))

    def get_mevas(self, year):
        """
        вернуть согме, люме, вангме, лунме, павме для года

        :param year:
        :return:
        """
        s, lu_me, w, u, p = (-1, -1, -1, -1, -1)
        age = year - self.birth_year
        lu_me, new_meva_rect = self.__build_new_meva_rect(year)
        s = new_meva_rect[0][2]
        w = new_meva_rect[2][0]

        # LungMe
        data_lung_me = {
            u'Тигр': u'Железная Обезьяна', u'Лошадь': u'Железная Обезьяна', u'Собака': u'Железная Обезьяна',
            u'Крыса': u'Деревянный Тигр', u'Дракон': u'Деревянный Тигр', u'Обезьяна': u'Деревянный Тигр',
            u'Петух': u'Водяная Свинья', u'Бык': u'Водяная Свинья', u'Змея': u'Водяная Свинья',
            u'Синья': u'Огненная Змея', u'Кролик': u'Огненная Змея', u'Баран': u'Огненная Змея',
        }
        birth_animal = self.get_elements()['animal']
        animal_metreng = data_lung_me[birth_animal]
        birth_metreng = self.metreng[self.birth_year]['metreng']
        birth_meva = self.metreng[self.birth_year]['meva']
        year_of_sogme = self.__find_in_mentreng(animal_metreng, birth_metreng)
        um = self.metreng[year_of_sogme]['meva']
        new_meva_rect = self.__fill_meva_rect(um)
        u = new_meva_rect[0][2]

        # PawMe
        birth_year_sex = self.year_sex[birth_animal]
        pawme_order = {u'мужской': [[1, 1], [0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0], [0, 0]],
                       u'женский': [[1, 1], [0, 1], [0, 0], [1, 0], [1, 2], [2, 1], [2, 2], [1, 2], [0, 2]]
                       }
        ix1 = pawme_order[birth_year_sex][age % 9]
        new_meva_rect = self.__fill_meva_rect(lu_me)
        p = new_meva_rect[ix1[0]][ix1[1]]
        return {'sogme': s, 'lume': lu_me, 'wangme': w, 'lunme': u, 'pawme': p, 'bmewa': birth_meva}

    def __rotate_animal(self, from_animal, count):
        """
        просчитать по животным с иходного и получить новый

        :param from_animal:
        :param count:
        :return:
        """
        ix = self.animal_list.index(from_animal)
        ix = (ix + count) % 12
        return self.animal_list[ix]

    def __rotate_element(self, from_element, count):
        """
        просчитать по элементам с иходного и получить новый

        :param from_element:
        :param count:
        :return:
        """
        ix = self.element_list.index(from_element)
        ix = (ix + count) % 5
        return self.element_list[ix]

    def get_logmen(self, year, sex='man'):
        """
        вычислить логмен для года

        :param year:
        :param sex:
        :return:
        """
        age = year - self.birth_year
        if sex == 'man':
            animal = self.animal_list[age % 12 - 1]
            el = self.get_elements(self.birth_year)['wang']
            s_el = self.find_relative(el, u'Сын')
            element = self.__rotate_element(s_el, age)
        else:
            animal = self.animal_list[7 - (6 - age) % 12]
            el = self.get_elements(self.birth_year)['wang']
            s_el = self.find_relative(el, u'Мать')
            element = self.__rotate_element(s_el, -age)
        return element, animal

    def get_months_of_year(self, year):
        """
        вернуть список элементов и животных месяцев года

        :param year:
        :return:
        """
        elements = []
        el = self.get_elements(year)['wang']
        el = self.find_relative(el, u'Сын')
        for i in range(6):
            elements.append(el)
            elements.append(el)
            el = self.__rotate_element(el, 1)
        res = []
        for i in range(12):
            res.append((elements[i], self.animal_list[i], self.year_sex[self.animal_list[i]]))
        return res

    def get_days_of_month(self, month):
        """
        дать список дней месяца

        :param month: (u'Огонь', u'Тигр', u'мужской')
        :return:
        """

        if month[2] == u'мужской':
            animal = u'Тигр'
        else:
            animal = u'Обезьяна'
        el = self.find_relative(month[0], u'Сын')
        res = []
        for d in range(30):
            res.append((d + 1, el, animal))
            el = self.__rotate_element(el, 1)
            animal = self.__rotate_animal(animal, 1)
        return res

    def get_hours_of_day(self, month):
        """
        вернуть список часов

        :param day: в формате (15, u'Огонь', u'Собака')
        :return:
        """
        el = self.find_relative(month[1], u'Сын')
        res = []
        for h in range(12):
            res.append((h + 1, el, self.hour_animal_list[h]))
            el = self.__rotate_element(el, 1)
        return res

    def get_tarkut(self, year, month, day, hour):
        """
        посчитать все таркуты

        :param year: (u'Вода', u'Баран')
        :param month: 3
        :param day: 2
        :param hour: 4 == 'полдень'
        :return:
        """
        s, l, w, lung = '', '', '', ''
        yel = self.get_elements(year)
        yanimal = yel['animal']
        cem = self.tarkut_animal[yel['sog']]
        an = self.__rotate_animal(cem, 1)
        for i in range(12):
            if an == yanimal:
                s = i
                break
            an = self.__rotate_animal(an, 1)

        mnth = self.get_months_of_year(year)[month - 1]
        cem = self.tarkut_animal[yel['lu']]
        an = self.__rotate_animal(cem, 1)
        for i in range(12):
            if an == mnth[1]:
                l = i
                break
            an = self.__rotate_animal(an, 1)

        dy = self.get_days_of_month(mnth)[day - 1]
        cem = self.tarkut_animal[yel['wang']]
        an = self.__rotate_animal(cem, 1)
        for i in range(12):
            if an == dy[2]:
                w = i
                break
            an = self.__rotate_animal(an, 1)

        hr = self.get_hours_of_day(dy)[hour - 1]
        cem = self.tarkut_animal[yel['lung']]
        an = self.__rotate_animal(cem, 1)
        for i in range(12):
            if an == hr[2]:
                lung = i
                break
            an = self.__rotate_animal(an, 1)

        return {'sogtarkut': s + 1, 'lutarkut': l + 1, 'wangtarkut': w + 1, 'lungtarkut': lung + 1}

    def get_tribal(self, telement):
        """
        определить родовой элемент

        :param telement: предполагаемый родовой элемент
        :return:
        """
        jpgr = self.get_elements(self.birth_year)['animal']
        big_exaust = (u"Железо:Корова", u"Вода:Дракон", u"Земля:Дракон", u"Дерево:Баран", u"Огонь:Собака")
        n = u"%s:%s" % (telement, jpgr)
        if n in big_exaust:
            return u"Большое истощение"
        small_exaust = (u"Дерево:Корова", u"Огонь:Дракон", u"Железо:Баран", u"Вода:Собака", u"Земля:Собака")
        if n in small_exaust:
            return u"Малое истощение"
        yelement = self.get_elements(self.birth_year)['sog']
        rel = self.get_relations(telement, yelement)
        if yelement == telement:
            return u'Сила'
        if rel in (u'Мать', u'Друг', u'Враг', u'Сын'):
            return rel


if __name__ == "__main__":
    pass