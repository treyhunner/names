import names
from setuptools import setup, find_packages


setup(
    name=names.__title__,
    version=names.__version__,
    author=names.__author__,
    url="https://github.com/treyhunner/names",
    description="Generate random names",
    long_description='\n\n'.join((
        open('README.rst').read(),
        open('CHANGES.rst').read(),
    )),
    license=names.__license__,
    packages=find_packages(),
    package_data={'names': ['dist.*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'names = names.main:main',
        ],
    },
    test_suite='test_names',
)
