# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Unit tests
from unit_tests import test_killer_app


def suite():
    suite = unittest.TestSuite()
    suite.addTests(test_killer_app.suite())
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
