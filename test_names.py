#!/usr/bin/env python
import unittest
import sys
from os.path import abspath, join, dirname
try:
    from StringIO import StringIO
except:
    from io import StringIO
from collections import defaultdict
import names
from names import bulk as bulk_names
from names.main import main


full_path = lambda filename: abspath(join(dirname(__file__), filename))


class patch_stdout(object):
    def __init__(self):
        self.stdout = StringIO()
        self.real_stdout = sys.stdout

    def __enter__(self):
        sys.stdout = self.stdout
        return sys.stdout

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.close()
        sys.stdout = self.real_stdout


class patch_file:

    def __init__(self, file_dict, names_module=names):
        self.files = file_dict
        self.names_module = names_module

    def __enter__(self):
        self.old_files = self.names_module.FILES
        self.names_module.FILES = self.files

    def __exit__(self, type, value, traceback):
        self.names_module.FILES = self.old_files

test_files = {
    'first:male': full_path('test/male.txt'),
    'first:female': full_path('test/female.txt'),
    'last': full_path('test/last.txt'),
}


class NamesTest(unittest.TestCase):

    def setUp(self):
        self.names = names

    def test_get_name(self):
        counts = defaultdict(int)
        rounds = 5000.0
        test_file = full_path('test/file1.txt')
        for i in range(1, int(rounds)):
            counts[self.names.get_name(test_file)] += 1
        self.assertAlmostEqual(counts['Test1'] / rounds, 0.333, delta=0.05)
        self.assertAlmostEqual(counts['Test2'] / rounds, 0.277, delta=0.05)
        self.assertAlmostEqual(counts['Test3'] / rounds, 0.222, delta=0.05)
        self.assertAlmostEqual(counts['Test4'] / rounds, 0.166, delta=0.05)
        self.assertEqual(counts['Test5'] / rounds, 0)

    def test_random_gender(self):
        counts = defaultdict(int)
        rounds = 5000.0
        with patch_file(test_files, self.names):
            for i in range(int(rounds)):
                self.names.get_first_name()
                counts[self.names.get_first_name()] += 1
        self.assertAlmostEqual(counts['Male'] / rounds, 0.500, delta=0.05)
        self.assertAlmostEqual(counts['Female'] / rounds, 0.500, delta=0.05)

    def test_correct_files(self):
        with patch_file(test_files, self.names):
            self.assertEqual(self.names.get_first_name(gender='male'), "Male")
            self.assertEqual(self.names.get_first_name(gender='female'), "Female")
            self.assertEqual(self.names.get_last_name(), "Last")

    def test_empty_file(self):
        empty_files = {
            'first:male': full_path('test/empty.txt'),
            'first:female': full_path('test/empty.txt'),
            'last': full_path('test/empty.txt'),
        }
        with patch_file(empty_files, self.names):
            self.assertEqual(self.names.get_first_name(gender='male'), "")
            self.assertEqual(self.names.get_first_name(gender='female'), "")
            self.assertEqual(self.names.get_last_name(), "")

    def test_only_male_and_female_gender_are_supported(self):
        with self.assertRaises(ValueError):
            self.names.get_first_name(gender='other')


class BulkNamesTest(NamesTest):

    def setUp(self):
        self.names = bulk_names


class CommandLineTest(unittest.TestCase):

    def test_cli(self):
        with patch_stdout() as stdout:
            with patch_file(test_files):
                main()
                self.assertIn(stdout.getvalue(),
                              ["Male Last\n", "Female Last\n"])


if __name__ == '__main__':
    unittest.main()
