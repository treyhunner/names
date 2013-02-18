import names
from setuptools import setup, find_packages


setup(
    name=names.__title__,
    version=names.__version__,
    author=names.__author__,
    url="https://github.com/treyhunner/names",
    description="Generate random names",
    long_description=open('README.rst').read(),
    license=names.__license__,
    packages=find_packages(),
    package_data={'names': ['dist.*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'names = names.main:main',
        ],
    },
)
