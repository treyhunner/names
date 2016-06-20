from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random
import sys


__title__ = 'names'
__version__ = '0.3.0.post1'
__author__ = 'Austin Roberts'
__license__ = 'MIT'


full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'first:male': full_path('dist.male.first'),
    'first:female': full_path('dist.female.first'),
    'last': full_path('dist.all.last'),
}

cache = {}

def load_file(filename):
    try:
        return cache[filename]
    except KeyError:
        cache[filename] = []
        with open(filename) as fd:
            for line in fd:
                name, _, cummulative, _ = line.split()
                cache[filename].append((name, float(cummulative)))
        return cache[filename]


def get_name(filename):
    # Do a binary search to pick a name
    selected = random.random() * 90
    names = load_file(filename)
    max_index = len(names)
    min_index = 0
    if min_index == max_index:
        # Empty file
        return ""
    while min_index < max_index:
        index = (min_index + max_index) // 2
        name, cummulative = names[index]
        if cummulative < selected:
            min_index = index
        else:
            max_index = index
        if max_index == min_index + 1:
            # Once the min_index and max_index are one apart, we need to look at
            # them directly
            if names[min_index][1] > selected:
                return names[min_index][0]
            return names[max_index][0]
    return name

def get_first_name(gender=None):
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return "{0} {1}".format(get_first_name(gender), get_last_name())
