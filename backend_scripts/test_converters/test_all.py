import unittest
from . import test_english


def suite():
    test_loader = unittest.TestLoader()
    test_names = ['backend_scripts.test_converters.test_english']

    test_suite = test_loader.loadTestsFromNames(test_names)

    # add other test modules here
    return test_suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())