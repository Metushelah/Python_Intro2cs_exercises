import os
import unittest

from PathScanner import path_iterator, file_with_all_words


class PathScannerTest(unittest.TestCase):
    def setUp(self):
        """This method is called once before each test runs. The chances of
        state changes are pretty slim here, but it is never a bad thing to
        take extra security measures when testing."""
        self._path_iter = path_iterator(os.path.join("test", "a"))
        self._word_list = [
            "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday"
        ]

    def test_path_iterator(self):
        """Tests path_iterator by using the provided iterator on a pre-created
        test directory - 'a'"""
        # hard code the names of the files within 'a' in a set:
        files = {
            os.path.join("test", "a", "b"),
            os.path.join("test", "a", "a_file")
        }
        count = 0
        for file in self._path_iter:
            # assert every file from the iterator is in our hard-coded set.
            self.assertTrue(file in files, file + " not in " + str(files))
            count += 1
        # assert the amount of iterated files is 2, like the cardinality...
        # well, the size of our set. Assures us each item in our set was
        # called by the iterator.
        self.assertEqual(2, count)

    def test_file_with_all_words(self):
        """Tests file_with_all_words(path, word_list). The final test!!!"""
        # So this is the test we've all been waiting for; our final
        # destination in this exercise. Every bit of code we wrote until now
        # was a step in the way to make this function possible: it takes our
        # WordExtractor and WordTracker classes, instantiates them and
        # integrates them into a complete system capable of scanning a
        # file-system and searching for a file which contains all words from
        # our list.
        # In order to test if our system works (if this function works)
        # we have a test file hierarchy, contained in the folder 'a'.
        # a has a file a_file and a directory b in it. b has b_file and c,
        # c has c_file and d, d has d_file. c_file and d_file both
        result = os.path.join("test", "a", "b", "c", "c_file")
        root = os.path.join("test", "a")
        self.assertEqual(result, file_with_all_words(root, self._word_list))


if __name__ == '__main__':
    unittest.main()
