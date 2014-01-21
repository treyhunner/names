from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random


__title__ = 'names'
__version__ = '0.3.0.post1'
__author__ = 'Trey Hunner'
__license__ = 'MIT'


full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'first:male': full_path('dist.male.first'),
    'first:female': full_path('dist.female.first'),
    'last': full_path('dist.all.last'),
}


def get_name(filename):
    selected = random.random() * 90
    with open(filename) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            if float(cummulative) > selected:
                return name
    return ""  # Return empty string if file is empty


def get_first_name(gender=None):
    if gender not in ('male', 'female'):
        gender = random.choice(('male', 'female'))
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return "{0} {1}".format(get_first_name(gender), get_last_name())

def gender_rank(name, gender, default=0.):
    first = name.split(" ")[0].upper()
    with open(FILES['first:%s' % gender]) as name_file:
        for line in name_file:
            name, rank, cummulative, _ = line.split()
            if name == first: return float(rank)
    return default
    
def gender_ranks(name, default=0.):
    return gender_rank(name, "male", default), gender_rank(name, "female", default)
    
def guess_gender(name, male="male", female="female", default=""):
    m, f = gender_ranks(name)
    if m > f: return male
    elif f > m: return female
    else: return default
