import unittest

from WordExtractor import WordExtractor


class WordExtractorTest(unittest.TestCase):
    def setUp(self):
        # from ex10 instructions:
        string = "  Are - you pondering   what\nI am \tpondering pinky?  \n"
        self._parts = ['Are', '-', 'you', 'pondering', 'what', 'I', 'am',
                        'pondering', 'pinky?']

        # create a file with string as it's text:
        test_file_name = "text_file.txt"
        with open(test_file_name, "w") as test_file:
            test_file.write(string)

        # create a word extractor for this file
        self._word_extractor = WordExtractor(test_file_name)

    def test_next(self):
        """Tests the word extractor object to see that the first 10 words from
        the test words file are what they should be.

        WARNING: This does NOT text execution space complexity."""

        # extract the words from the file (using the extractor), and count them
        counter = 0
        for word in self._word_extractor:
            # assert every word from the file is in our independent parts list
            self.assertTrue(word in self._parts)
            counter += 1

        # assert the length of out parts list and the amount of extracted words
        # are the same. This assures the word extractor didn't skip any of the
        # words we expect - the words in self._parts. Of course, this is only
        # good because we currently know all the words in self._parts must be
        # in the file, because we wrote the file this way. When we actually use
        # the extractor, we may not have any idea which words to expect from
        # the file.
        self.assertEqual(len(self._parts), counter)


if __name__ == '__main__':
    unittest.main()
