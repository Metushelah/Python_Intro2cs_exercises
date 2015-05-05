import unittest

import palindrome


class PalindromeTestCase(unittest.TestCase):
    def test_is_palindrome_1(self):
        self.assertTrue(palindrome.is_palindrome_1("141"),
                        "returned false for 141")
        self.assertFalse(palindrome.is_palindrome_1("143"),
                         "returned true for 143")
        self.assertTrue(palindrome.is_palindrome_1(""),
                        "returned false for empty string")
        self.assertTrue(palindrome.is_palindrome_1("a"),
                        "returned false for a")
        self.assertTrue(palindrome.is_palindrome_1("aabbcbbaa"),
                        "returned false for aabbcbbaa")
        self.assertFalse(palindrome.is_palindrome_1("aabbcbbca"),
                         "returned true for aabbcbbca")
        self.assertTrue(palindrome.is_palindrome_1("evilolive"),
                        "returned false for evilolive")
        self.assertFalse(palindrome.is_palindrome_1("evil olive"),
                         "returned true for evil olive")
        self.assertTrue(palindrome.is_palindrome_1("mirrorrim"),
                        "returned false for mirrorrim")
        self.assertFalse(palindrome.is_palindrome_1("mirror rim"),
                         "returned true for mirror rim")
        self.assertTrue(palindrome.is_palindrome_1("stackcats"),
                        "returned false for stackcats")
        self.assertFalse(palindrome.is_palindrome_1("stack cats"),
                         "returned true for stack cats")


    def test_is_palindrome_2(self):
        self.assertTrue(palindrome.is_palindrome_2("141", 0, 2),
                        "returned false for 141")
        self.assertFalse(palindrome.is_palindrome_2("143", 0, 2),
                         "returned true for 143")
        self.assertTrue(palindrome.is_palindrome_2("", 0, 0),
                        "returned false for empty string")
        self.assertTrue(palindrome.is_palindrome_2("a", 0, 0),
                        "returned false for a")
        self.assertTrue(palindrome.is_palindrome_2("aabbcbbaa", 0, 8),
                        "returned false for aabbcbbaa")
        self.assertFalse(palindrome.is_palindrome_2("aabbcbbca", 0, 8),
                         "returned true for aabbcbbca")
        self.assertTrue(palindrome.is_palindrome_2("evilolive", 0, 8),
                        "returned false for evilolive")
        self.assertFalse(palindrome.is_palindrome_2("evil olive", 0, 9),
                         "returned true for evil olive")
        self.assertTrue(palindrome.is_palindrome_2("mirrorrim", 0, 8),
                        "returned false for mirrorrim")
        self.assertFalse(palindrome.is_palindrome_2("mirror rim", 0, 9),
                         "returned true for mirror rim")
        self.assertTrue(palindrome.is_palindrome_2("stackcats", 0, 8),
                        "returned false for stackcats")
        self.assertFalse(palindrome.is_palindrome_2("stack cats", 0, 9),
                         "returned true for stack cats")
        self.assertTrue(palindrome.is_palindrome_2("bubbles", 0, 2),
                        "returned false for bubbles, 0, 2")
        self.assertFalse(palindrome.is_palindrome_2("bubbles", 0, 3),
                         "returned true for bubbles, 0, 3")
        self.assertTrue(palindrome.is_palindrome_2("bubbles", 2, 3),
                        "returned false for bubbles, 2, 3")
        self.assertFalse(palindrome.is_palindrome_2("bubbles", 1, 3),
                         "returned true for bubbles, 1, 3")
        self.assertTrue(palindrome.is_palindrome_2("143", 2, 1),
                        "returned false for 143")
        self.assertFalse(palindrome.is_palindrome_2("143", 2, 0),
                        "returned true for 143")


if __name__ == '__main__':
    unittest.main()
