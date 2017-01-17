from __future__ import print_function
from names import get_full_name


def main():
    print(get_full_name(gender="male", locale='ru'))
    print(get_full_name(gender="female", locale='ru'))
    print(get_full_name(gender="male", locale='ru-latin'))
    print(get_full_name(gender="female", locale='ru-latin'))
    print(get_full_name(gender="male", locale='ua'))
    print(get_full_name(gender="female", locale='ua'))
    print(get_full_name(gender="male", locale='ua-latin'))
    print(get_full_name(gender="female", locale='ua-latin'))
    print(get_full_name(gender="male"))
    print(get_full_name(gender="female"))
    print(get_full_name(gender="male", locale='en'))
    print(get_full_name(gender="female", locale='en'))


if __name__ == "__main__":
    main()
