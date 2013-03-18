#!/usr/bin/env python
from os.path import abspath, join, dirname
from unittest import TestCase, main
from collections import defaultdict
import names


full_path = lambda filename: abspath(join(dirname(__file__), filename))

FILES = {
    'test1': full_path('test/file1.txt'),
}


class NamesTest(TestCase):

    def test_get_name(self):
        counts = defaultdict(int)
        rounds = 1000.0
        for i in range(1, int(rounds)):
            counts[names.get_name(FILES['test1'])] += 1
        self.assertAlmostEqual(counts['Test1'] / rounds, 0.333, delta=0.05)
        self.assertAlmostEqual(counts['Test2'] / rounds, 0.277, delta=0.05)
        self.assertAlmostEqual(counts['Test3'] / rounds, 0.222, delta=0.05)
        self.assertAlmostEqual(counts['Test4'] / rounds, 0.166, delta=0.05)
        self.assertEqual(counts['Test5'] / rounds, 0)


if __name__ == '__main__':
    main()
