from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random
from bisect import bisect_left


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

# An array of (cumulative, name) pairs to use
CACHED_FILES = {}


def get_name(filename, cached=False):
    # Choose a random name
    selected = random.random() * 90
    if cached:
        # Build a cache for this filename
        if filename not in CACHED_FILES:
            names = []
            with open(filename) as name_file:
                for line in name_file:
                    name, _, cumulative, _ = line.split()
                    names.append((float(cumulative), name))
            CACHED_FILES[filename] = names

        names = CACHED_FILES[filename]
        if len(names) == 0:
            return ""  # Return empty string if file is empty

        idx = min(bisect_left(names, (selected,)), len(names) - 1)
        return names[idx][1]

    else:
        with open(filename) as name_file:
            for line in name_file:
                name, _, cummulative, _ = line.split()
                if float(cummulative) > selected:
                    return name
        return ""  # Return empty string if file is empty


def get_first_name(gender=None, cached=False):
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return get_name(FILES['first:%s' % gender], cached).capitalize()


def get_last_name(cached=False):
    return get_name(FILES['last'], cached).capitalize()


def get_full_name(gender=None, cached=False):
    return "{0} {1}".format(get_first_name(gender, cached),
                            get_last_name(cached))
