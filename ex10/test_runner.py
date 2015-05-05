# #############################################################################z
# Unit testing for ex10
# Written by Yekhezkel Yovel
# Contributors:
# Idan Tene, Reshef Mintz, Yuval Jacoby, Abdallah Samara
#
# Feel free to use and distribute for whatever good you find in it.
# BUT: No one, including the writer or any of the contributors, shall be
# seen responsible for this code or any of it's outcomes.
#
# Usage:
# place the 'test' folder in project folder and run from CMD/Shell:
# python test_runner.py
# or:
# python3 test_runner.py
###############################################################################
import unittest

testmodules = [
    'test.path_scanner_test',
    'test.word_extractor_test',
    'test.word_tracker_test',
]

suite = unittest.TestSuite()

for t in testmodules:
    try:
        # If the module defines a suite() function, call it to get the suite.
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        # else, just load all the test cases from the module.
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)