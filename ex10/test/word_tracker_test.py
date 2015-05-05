import unittest

from WordTracker import WordTracker

'''
DIG WARNING (CHAFIROT)
'''


class WordTrackerTest(unittest.TestCase):
    def setUp(self):
        """This method is called once before each test method is called,
        so the word list and the tracker get re-initialized.
        May not be necessary for the list, but when testing it's okay to take
        extra security measures. The tracker, on the other hand, is a different
        story; it has an inner state which is changed in some of the tests.
        It must be re-initialized for the next test."""
        self._word_list = [
            "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday"
        ]
        self._tracker = WordTracker(self._word_list)

    def test_constructor(self):
        """Test class constructor"""
        # change the list used to create the tracker
        self._word_list.remove("Sunday")
        # assert the change is NOT reflected by tracker
        self.assertTrue("Sunday" in self._tracker)

    def test_contains(self):
        """Tests the behaviour of the __contains__ method of WordTracker,
        by using the 'in' keyword on a WordTracker instance."""
        for word in self._word_list:
            # Assert that indeed all words in the list are 'in' the tracker:
            self.assertTrue(word in self._tracker, word + " not in tracker?")

            # TODO: check if WordTracker should be case-sensitive
            # Assert case sensitivity
            self.assertFalse(word.lower() in self._tracker)

        # Simple __contains__ independent (using literals instead of original
        # list items) tests, True and False:
        self.assertTrue("Wednesday" in self._tracker)
        self.assertFalse("Yellow" in self._tracker)

    def test_encounter(self):
        """Tests the encounter method: The encounter method has an input
        (a word), an output (True or False), and a side effect: it documents
        each encounter such that if all words in the inner list have been
        encountered, the encountered_all method will return True. This means
        in order to test the encounter method it is not enough to test the
        input and output, but the inner state of the object must be verified
        too, to make sure the desired side-effect happens. The way to do this
        is by using different combinations of 'encounter' and 'encountered_all'
        on different inputs and outputs, and possibly also on different
        word-lists, or different configurations of word trackers (currently
        we only have one configuration (one instance)."""

        # Initially, that is: before 'encounter' has been used,
        # 'encountered_all' should return False:
        self.assertFalse(self._tracker.encountered_all())

        # For an alien word (one that is not in the word list), 'encounter'
        # should return false (and the inner state should not change.
        self.assertFalse(self._tracker.encounter("Alien"),
                         "This is not X-Files! Third kind encounters should"
                         " not be documented here.")

        # For a word from the list, 'encounter' should return True (and the
        # inner state of the tracker should be changed to reflect that. There
        # is no test for this change though, because it is not well defined
        # to us by the exercise instructions. Meaning, they didn't tell us how
        # to implement this 'inner state', only what the results should be.
        # I can test my implementation, but since yours is probably different
        # it will fail your code in vain. This is where you may want to write
        # your own test file and test your own implementation of testing
        # the change to the inner-state of the word tracker).
        self.assertTrue(self._tracker.encounter("Sunday"))

        # Although the specific change to the inner-state cannot be tested
        # 'globally' for all of us, we can make sure 'encountered_all' still
        # returns False, as it should, since only one of the words has been
        # encountered.
        self.assertFalse(self._tracker.encountered_all())

        # Now let's encounter every word in the list, asserting 'encounter'
        # keeps returning True. That is even though we 'encounter' Sunday for
        # the second time, since the boolean output represents whether or not
        # the word was in the list, not whether or not it's a new encounter.
        # Kind of a crazy idea, but since we run 'encounter' anyway (we need
        # to encounter every word in the list for our last test), why not
        # test it.
        for word in self._word_list:
            self.assertTrue(self._tracker.encounter(word))

        # Now that all words in the list has been encountered,
        # 'encountered_all' should finally return True.
        self.assertTrue(self._tracker.encountered_all())
        # I hope this function was clear enough, even though for a function
        # named 'test_encounter' it has quite a lot of calls to
        # 'encountered_all', but that's the 'effect' of 'side-effects'...

    def test_encounter_all(self):
        """Tests the encounter_all method"""
        # initially should return False
        self.assertFalse(self._tracker.encountered_all())
        # TODO: check if WordTracker should be case-sensitive
        # test case-sensitivity
        for word in self._word_list:
            self.assertFalse(self._tracker.encounter(word.lower()))
        # should return False
        self.assertFalse(self._tracker.encountered_all())
        # encounter all words in the list
        for word in self._word_list:
            self.assertTrue(self._tracker.encounter(word))
        # should return True
        self.assertTrue(self._tracker.encountered_all())
        # reset the tracker
        self._tracker.reset()
        # should return False after reset
        self.assertFalse(self._tracker.encountered_all())

    def test_reset(self):
        """Tests the reset method. This test is contained in the former one,
        since testing side-effects often involves different methods"""
        # encounter all words in the list
        for word in self._word_list:
            self.assertTrue(self._tracker.encounter(word))
        # should return True
        self.assertTrue(self._tracker.encountered_all())
        # reset the tracker
        self._tracker.reset()
        # should return False after reset
        self.assertFalse(self._tracker.encountered_all())


if __name__ == '__main__':
    unittest.main()
