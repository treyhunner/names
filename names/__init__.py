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
    'tlds': full_path('dist.tlds'),
    'companies': full_path('dist.companies'),
}

def get_tld(filename):
    selected = random.random() * 83
    with open(filename) as tld_file:
        for line in tld_file:
            tld, cummulative = line.split()
            if float(cummulative) > selected:
                return tld
    return ""

def get_company(filename):
    selected = random.random() * 60
    with open(filename) as company_file:
        for line in company_file:
            cc = line.split()
            cummulative = cc[-1]
            if float(cummulative) > selected:
                return ' '.join(cc[:-1])
    return ""

def get_name(filename):
    selected = random.random() * 91
    with open(filename) as name_file:
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

def get_email(name, company=None, tld=None):
    if company is None:
        company = get_company(FILES['companies'])
    if tld is None:
        tld = get_tld(FILES['tlds'])
    email = '{0}@{1}.{2}'.format(name, company, tld)
    return email.replace(' ', '').lower()

