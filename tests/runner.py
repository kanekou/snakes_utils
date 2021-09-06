# Copyright (c) 2021 Kohei Kaneshima (kanekou)
# This software is released under the MIT License, see LICENSE.txt.

import unittest
import tests

class TestRunner(unittest.TestCase):

    def test_runner(self):
        test_suite = unittest.TestSuite()

        tests = unittest.defaultTestLoader.discover("tests", pattern="test_*.py")

        test_suite.addTest(tests)
        unittest.TextTestRunner().run(test_suite)
