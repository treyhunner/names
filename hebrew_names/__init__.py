from os.path import abspath, join, dirname
import itertools
import codecs
import random


__title__ = 'hebrew-names'
__version__ = '0.0.1'
__author__ = 'Aluma Gelbard'
__license__ = 'MIT'


def full_path(filename):
    return abspath(join(dirname(__file__), filename))


ETHNICITIES = ('jew', 'muslim', 'christian', 'druze', 'other')
GENDERS = ('male', 'female')

FILES = {
    f'first:{ethnicity}:{gender}': full_path(f'dist.{ethnicity}.{gender}.first')
    for (ethnicity, gender) in itertools.product(ETHNICITIES, GENDERS)
}

FILES.update({
    f'last:{ethnicity}': full_path(f'dist.{ethnicity}.last')
    for ethnicity in ETHNICITIES
})

FILES['cumulatives.all'] = full_path('dist.cumulatives.all')

CUMULATIVES = None


def load_cumulatives():
    with codecs.open(FILES['cumulatives.all'], 'r', 'utf-16') as cumulatives_file:
        global CUMULATIVES
        CUMULATIVES = {
            file: float(last_cumulative) for (file, last_cumulative) in (line.split('\t') for line in cumulatives_file)
        }


def get_name(file):
    if (not CUMULATIVES):
        load_cumulatives()

    selected = random.random() * CUMULATIVES[file]
    with codecs.open(FILES[file], 'r', 'utf-16') as name_file:
        for line in name_file:
            name, _, _, cumulative, _ = line.split('\t')
            if float(cumulative) >= selected:
                return name
    return ""  # Return empty string if file is empty


def select_gender(gender=None):
    gender = gender or random.choice(GENDERS)
    if gender not in GENDERS:
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return gender


def select_ethnicity(ethnicity=None):
    ethnicity = ethnicity or random.choice(ETHNICITIES)
    if ethnicity not in ETHNICITIES:
        raise ValueError("Only 'jew', 'muslim', 'christian', 'druze' and 'other' are supported as ethnicity")
    return ethnicity


def get_first_name(ethnicity=None, gender=None):
    ethnicity = select_ethnicity(ethnicity)
    gender = select_gender(gender)
    return get_name(f'first:{ethnicity}:{gender}')


def get_last_name(ethnicity=None):
    ethnicity = select_ethnicity(ethnicity)
    return get_name(f'last:{ethnicity}')


def get_full_name(ethnicity=None, gender=None):
    ethnicity = select_ethnicity(ethnicity)
    return f'{get_first_name(ethnicity, gender)} {get_last_name(ethnicity)}'.strip()
