# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Unit tests
from unit_tests.test_killer_app import test_main


def suite():
    suite = unittest.TestSuite()
    suite.addTests(test_main.suite())
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
