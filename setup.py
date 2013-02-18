from setuptools import setup, find_packages


setup(
    name="names",
    version="0.1",
    author="Trey Hunner",
    url="https://github.com/treyhunner/names",
    description="Generate random names",
    license="LICENSE.txt",
    packages=find_packages(),
    package_data={'names': ['dist.*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'names = names.main:main',
        ],
    },
)
