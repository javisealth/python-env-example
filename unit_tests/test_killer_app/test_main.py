# -*- coding: utf-8 -*-

# Python stdlib
import unittest


class MainUnitTest(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True, 'True is not True!')
        number = 7
        self.assertEqual(number, 7, 'number is not 7')

    def other_function(self):
        print('This method is not a test method and will not run as part of the test suite')
        print('But other real test methods can call this method if they need to')


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(MainUnitTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
