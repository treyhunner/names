from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random

__title__ = 'names'
__version__ = '0.3.0.post1'
__author__ = 'Trey Hunner'
__license__ = 'MIT'

__genders__ = ('male', 'female')
__locales__ = ('en', 'ua', 'ua-latin', 'ru', 'ru-latin')

full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'en:first:male': full_path('dist.male.first.en'),
    'en:first:female': full_path('dist.female.first.en'),
    'en:last': full_path('dist.all.last.en'),
    'ua:first:male': full_path('dist.male.first.ua'),
    'ua:first:female': full_path('dist.female.first.ua'),
    'ua:last:male': full_path('dist.male.last.ua'),
    'ua:last:female': full_path('dist.female.last.ua'),
    'ua-latin:first:male': full_path('dist.male.first.ua-latin'),
    'ua-latin:first:female': full_path('dist.female.first.ua-latin'),
    'ua-latin:last:male': full_path('dist.male.last.ua-latin'),
    'ua-latin:last:female': full_path('dist.female.last.ua-latin'),
    'ru:first:male': full_path('dist.male.first.ru'),
    'ru:first:female': full_path('dist.female.first.ru'),
    'ru:last:male': full_path('dist.male.last.ru'),
    'ru:last:female': full_path('dist.female.last.ru'),
    'ru-latin:first:male': full_path('dist.male.first.ru-latin'),
    'ru-latin:first:female': full_path('dist.female.first.ru-latin'),
    'ru-latin:last:male': full_path('dist.male.last.ru-latin'),
    'ru-latin:last:female': full_path('dist.female.last.ru-latin')
}


def get_name(filename):
    with open(filename) as name_file:
        #Using cummulative wage of second name from end
        lines = name_file.readlines()
        prelast_cum_wage = float(lines[len(lines)-2].split()[2])
        selected = random.random() * prelast_cum_wage
        for line in lines:
            name, _, cummulative, _ = line.split()
            if float(cummulative) > selected:
                return name


def get_first_name(gender=None, locale="en"):
    if locale not in __locales__:
        raise ValueError("Only next locales are supported:"+__locales__)
    if gender is None:
        if locale == "en":
            gender = random.choice(('male', 'female'))
        else:
            raise ValueError("For this locale you have to set a gender")
    if gender not in __genders__:
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return get_name(FILES['%s:first:%s' % (locale, gender)]).decode('utf-8').capitalize()


def get_last_name(gender=None, locale="en"):
    if locale not in __locales__:
        raise ValueError("Only next locales are supported:"+__locales__)
    if locale == 'en':
        return get_name(FILES['%s:last' % locale]).capitalize()
    else:
        if gender is None or gender not in __genders__:
            raise ValueError("For this locale you have to set a gender, 'male' or 'female'")
        return get_name(FILES['%s:last:%s' % (locale, gender)]).decode('utf-8').capitalize()


def get_full_name(gender=None, locale="en"):
    return "{0} {1}".format(get_first_name(gender, locale), get_last_name(gender, locale))
