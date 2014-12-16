from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random
from multiprocessing import Pool, cpu_count


__title__ = 'names'
__version__ = '0.3.0.post1'
__author__ = 'Trey Hunner'
__license__ = 'MIT'


full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'first:male': {
        'path': full_path('dist.male.first'),
    },
    'first:female': {
        'path': full_path('dist.female.first'),
    },
    'last': {
        'path': full_path('dist.all.last'),
    }
}


def get_name(filename):
    if 'cache' in filename and len(filename['cache']) > 0:
        selected = random.randint(0, len(filename['cache']) - 1)
        return filename['cache'][selected]
    else:
        selected = random.random() * 90
        with open(filename['path']) as name_file:
            for line in name_file:
                name, _, cummulative, _ = line.split()
                if float(cummulative) > selected:
                    return name
        return ""  # Return empty string if file is empty


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


def cache_file(filename):
    filename['cache'] = []
    with open(filename['path']) as name_file:
        for line in name_file:
            name, _, _, _ = line.split()
            filename['cache'].append(name)
    return ""  # Return empty string if file is empty


def get_full_names(gender=None, count=1):
    for f in FILES.values():
        cache_file(f)

    random.seed()
    pool = Pool(cpu_count())
    return list(pool.imap(get_full_name, [gender] * count))
