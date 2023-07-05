"""
Author: Mel Ho
Website: www.mel-ware.com
Created: 07/05/2023

Testing tools to automate the testing of our code from within Maya.
"""
import modules
import os
import unittest


def discoverAndRun(start_dir='.', pattern='test_*.py'):
    """ Discover and run test cases, returning the result.

        Args:
            start_dir: the starting directory
            pattern: the file name pattern for test cases
    """
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir, pattern=pattern)
    runner = unittest.TextTestRunner()
    result = runner.run(tests)
    return result


def getTestOutput(module, pattern='test_*.py'):
    """ Prints test outputs of a given module

        Args:
            module: the desired module
            pattern: the file name pattern for test cases
    """
    result = discoverAndRun(os.path.dirname(module.__file__), pattern)
    print("\n>>> result.testsRun: \t%s" % (result.testsRun))
    print(">>> result.passes: \t\t%s" % (result.testsRun - len(result.errors)))
    print(">>> result.errors: \t\t%s" % (len(result.errors)))
    print(">>> result.failures: \t%s" % (len(result.failures)))
    print(">>> result.skipped: \t%s" % (len(result.skipped)))


def testAllModules():
    """ Tests all modules
    """
    getTestOutput(modules)