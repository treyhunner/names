#!/usr/bin/env python
from os.path import abspath, join, dirname
from unittest import TestCase, main
from collections import defaultdict
import names


full_path = lambda filename: abspath(join(dirname(__file__), filename))

FILES = {
    'test1': full_path('test/file1.txt'),
}


class patch_file:

    def __init__(self, file_dict):
        self.files = file_dict

    def __enter__(self):
        self.old_files = names.FILES
        names.FILES = self.files

    def __exit__(self, type, value, traceback):
        names.FILES = self.old_files


class NamesTest(TestCase):

    def test_get_name(self):
        counts = defaultdict(int)
        rounds = 5000.0
        for i in range(1, int(rounds)):
            counts[names.get_name(FILES['test1'])] += 1
        self.assertAlmostEqual(counts['Test1'] / rounds, 0.333, delta=0.05)
        self.assertAlmostEqual(counts['Test2'] / rounds, 0.277, delta=0.05)
        self.assertAlmostEqual(counts['Test3'] / rounds, 0.222, delta=0.05)
        self.assertAlmostEqual(counts['Test4'] / rounds, 0.166, delta=0.05)
        self.assertEqual(counts['Test5'] / rounds, 0)

    def test_random_gender(self):
        counts = defaultdict(int)
        rounds = 5000.0
        with patch_file({'first:male': 'test/male.txt',
                         'first:female': 'test/female.txt'}):
            for i in range(int(rounds)):
                names.get_first_name()
                counts[names.get_first_name()] += 1
        self.assertAlmostEquals(counts['Male'] / rounds, 0.500, delta=0.05)
        self.assertAlmostEquals(counts['Female'] / rounds, 0.500, delta=0.05)


if __name__ == '__main__':
    main()
