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


class Names:

    def __init__(self, seed=None):
        self.set_seed(seed)

    def set_seed(self, seed):
        self.rnd = random.Random(seed)

    def get_name(self, filename):
        selected = self.rnd.random() * 90
        with open(filename) as name_file:
            for line in name_file:
                name, _, cummulative, _ = line.split()
                if float(cummulative) > selected:
                    return name
        return ""  # Return empty string if file is empty

    def get_first_name(self, gender=None):
        if gender is None:
            gender = self.rnd.choice(('male', 'female'))
        if gender not in ('male', 'female'):
            raise ValueError("Only 'male' and 'female' are supported as gender")
        return self.get_name(FILES['first:%s' % gender]).capitalize()

    def get_last_name(self):
        return self.get_name(FILES['last']).capitalize()

    def get_full_name(self, gender=None):
        return "{0} {1}".format(
            self.get_first_name(gender), self.get_last_name())


def get_name(filename):
    return Names().get_name(filename)


def get_first_name(gender=None):
    return Names().get_first_name(gender=gender)


def get_last_name():
    return Names().get_last_name()


def get_full_name(gender=None):
    return Names().get_full_name(gender=gender)
