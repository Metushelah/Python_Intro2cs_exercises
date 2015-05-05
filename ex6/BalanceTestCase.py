import unittest
import time

import balanced_brackets


class BalanceTestCase(unittest.TestCase):
    def test_is_balanced(self):
        self.assertFalse(balanced_brackets.is_balanced(")"))
        self.assertTrue(balanced_brackets.is_balanced("(2+4)"))
        self.assertFalse(balanced_brackets.is_balanced("(2+4"))
        self.assertTrue(balanced_brackets.is_balanced("((2+4)/(4+3)+4)*5"))
        self.assertFalse(balanced_brackets.is_balanced("(2+4)/(4+3)+4)*5"))
        self.assertFalse(balanced_brackets.is_balanced("a(bb))"))
        self.assertTrue(balanced_brackets.is_balanced("(a(bb))"))
        self.assertFalse(balanced_brackets.is_balanced("(a(bb)"))
        self.assertFalse(balanced_brackets.is_balanced("((((("))
        self.assertTrue(balanced_brackets.is_balanced("141"))
        self.assertTrue(balanced_brackets.is_balanced("1(4)1"))
        self.assertTrue(balanced_brackets.is_balanced("1(((4)))1"))
        self.assertFalse(balanced_brackets.is_balanced("1(41"))
        self.assertFalse(balanced_brackets.is_balanced("1(4154t5t"))
        self.assertFalse(balanced_brackets.is_balanced("14)1"))
        self.assertFalse(balanced_brackets.is_balanced("14))))1"))
        self.assertFalse(balanced_brackets.is_balanced("1(4)1)"))
        self.assertTrue(balanced_brackets.is_balanced("()(())"))
        self.assertFalse(balanced_brackets.is_balanced("()(()"))
        self.assertFalse(balanced_brackets.is_balanced("((())"))
        self.assertFalse(balanced_brackets.is_balanced(")(())"))

    def test_violated_balanced(self):
        self.assertEqual(balanced_brackets.violated_balanced(")"), 0)
        self.assertEqual(balanced_brackets.violated_balanced("(2+4)"), -1)
        self.assertEqual(balanced_brackets.violated_balanced("(2+4"), 4)
        self.assertEqual(
            balanced_brackets.violated_balanced("((2+4)/(4+3)+4)*5"), -1)
        self.assertEqual(
            balanced_brackets.violated_balanced("(2+4)/(4+3)+4)*5"), 13)
        self.assertEqual(balanced_brackets.violated_balanced("a(bb))"), 5)
        self.assertEqual(balanced_brackets.violated_balanced("(a(bb))"), -1)
        self.assertEqual(balanced_brackets.violated_balanced("(a(bb)"), 6)
        self.assertEqual(balanced_brackets.violated_balanced("((((("), 5)
        self.assertEqual(balanced_brackets.violated_balanced("141"), -1)
        self.assertEqual(balanced_brackets.violated_balanced("1(4)1"), -1)
        self.assertEqual(balanced_brackets.violated_balanced("1(((4)))1"), -1)
        self.assertEqual(balanced_brackets.violated_balanced("1(41"), 4)
        self.assertEqual(balanced_brackets.violated_balanced("1(4154t5t"), 9)
        self.assertEqual(balanced_brackets.violated_balanced("14)1"), 2)
        self.assertEqual(balanced_brackets.violated_balanced("14))))1"), 2)
        self.assertEqual(balanced_brackets.violated_balanced("1(4)1)"), 5)
        self.assertEqual(balanced_brackets.violated_balanced("()(())"), -1)
        self.assertEqual(balanced_brackets.violated_balanced("()(()"), 5)
        self.assertEqual(balanced_brackets.violated_balanced("((())"), 5)
        self.assertEqual(balanced_brackets.violated_balanced(")(())"), 0)
        self.assertEqual(balanced_brackets.violated_balanced("()))())"), 2)
        self.assertEqual(balanced_brackets.violated_balanced("(()((()"), 7)

    def test_violated_balance_execution_time(self):
        """Tests execution time. Currently set to 1/100 of a second,
        change max_time if necessary"""
        max_time = 0.001
        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "()(())((()))(((()))())(())()((((((((()(())))()(()))())))))"
            ), -1)
        self.assertTrue(time.time() - start < max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "()(())((()))(((()))())(())()((((((((()(())))()(()))()))))"
            ), 57)
        self.assertTrue(time.time() - start < max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "aab)()b)a)()((a(b(()))bbba(((b))())b(()a))))((aaa)()b(ab()((",
            ), 3)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "()b((bab()((b(()()a)(aa(b))bbbaba)))a((()()a(()))))(a))(a)b(",
            ), 54)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "((b(b(()((()())())))()ba())()())(())(()a())a)))(b)ba)bba)(((()aa)(((()",
            ), 44)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "()())ba())(((ab()))))(a()(((()))((a((b))(()b)(((b)(a)b)((()))aa)()))b(",
            ), 4)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                ")(()a()(bb)(b((a))(b)(a)()aa))())))(((()(b()a()b()))a))(())(((()(())b(",
            ), 0)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "(a)(())b(())))(b(()ab())))((())a()b(()a)()a(()()a()()ba))(b(b((())(())",
            ), 12)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                ")a)()()))())(()))b)(b()()()a(()((()b)()(())ba)((()()()((a)a((ba)(b(b)a",
            ), 0)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "()a()(()()b)()a())a)(aa))b(b)()a((b(b)()(())b(((()()))a))))(()(((()(b)",
            ), 17)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "((a()(ba()(()()ab(())(()))(b)(()()a(()(a))))b)()(((a)))b)b)b(a(())(())",
            ), 58)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "))()))(((b())a)a()())b(b((((a))a(((a(b)(ba)(((b))()()()b(()a)))))())((",
            ), 0)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "(bb)((()aaa))((((a()()(()b()())()((((()()))bb))))ab(()b)(()a()a)())())",
            ), -1)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "(()()b)()(a()(b(())(((a(a)()(((()()a)()bbb(a())(a)(a(())))b)(b()))))))",
            ), -1)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "(((ab()a(())b)ab)()((a((a)b())))(b())a())(()()())(b((a(()()))(())))()b",
            ), -1)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "()(b(ba))()()(()))))()b((ba)a()(bb(a(b()))()))(((())())()a)a(())a(((()",
            ), 17)
        self.assertTrue(time.time()-start<max_time)

        start = time.time()
        self.assertEqual(
            balanced_brackets.violated_balanced(
                "((()(b)((b())))))aa((b((())(b))bb()))())())((a)((()())()a(b))(aa))(a((",
            ), 16)
        self.assertTrue(time.time()-start<max_time)

    def test_match_brackets(self):
        self.assertEqual(balanced_brackets.match_brackets(")"), [])
        self.assertEqual(balanced_brackets.match_brackets("(2+4)"),
                         [4, 0, 0, 0, -4])
        self.assertEqual(balanced_brackets.match_brackets("(2+4"), [])
        self.assertEqual(balanced_brackets.match_brackets("((2+4)/(4+3)+4)*5"),
                         [14, 4, 0, 0, 0, - 4, 0, 4, 0, 0, 0, -4, 0, 0, - 14,
                          0, 0])
        self.assertEqual(balanced_brackets.match_brackets("(2+4)/(4+3)+4)*5"),
            [])
        self.assertEqual(balanced_brackets.match_brackets("a(bb))"), [])
        self.assertEqual(balanced_brackets.match_brackets("(a(bb))"),
                         [6, 0, 3, 0, 0, -3, -6])
        self.assertEqual(balanced_brackets.match_brackets("(a(bb)"), [])
        self.assertEqual(balanced_brackets.match_brackets("((((("), [])
        self.assertEqual(balanced_brackets.match_brackets("141"), [0, 0, 0])
        self.assertEqual(balanced_brackets.match_brackets("1(4)1"),
                         [0, 2, 0, -2, 0])
        self.assertEqual(balanced_brackets.match_brackets("1(((4)))1"),
                         [0, 6, 4, 2, 0, -2, -4, -6, 0])
        self.assertEqual(balanced_brackets.match_brackets("1(41"), [])
        self.assertEqual(balanced_brackets.match_brackets("1(4154t5t"), [])
        self.assertEqual(balanced_brackets.match_brackets("14)1"), [])
        self.assertEqual(balanced_brackets.match_brackets("14))))1"), [])
        self.assertEqual(balanced_brackets.match_brackets("1(4)1)"), [])
        self.assertEqual(balanced_brackets.match_brackets("()(())"),
                         [1, -1, 3, 1, -1, -3])
        self.assertEqual(balanced_brackets.match_brackets("()(()"), [])
        self.assertEqual(balanced_brackets.match_brackets("((())"), [])
        self.assertEqual(balanced_brackets.match_brackets(")(())"), [])

    def test_match_brackets_execution_time(self):
        """Tests execution time. Currently set to 1/100 of a second,
        change max_time if necessary"""
        max_time = 0.001
        start = time.time()
        self.assertEqual(
            balanced_brackets.match_brackets(
                "()(())((()))(((()))())(())()((((((((()(())))()(()))())))))"
            ),
            [1, -1, 3, 1, -1, -3, 5, 3, 1, -1, -3, -5, 9, 5, 3, 1, -1, -3, -5,
             1, -1, -9, 3, 1, -1, -3, 1, -1, 29, 27, 25, 23, 21, 17, 9, 7, 1,
             -1, 3, 1, -1, -3, -7, -9, 1, -1, 3, 1, -1, -3, -17, 1, -1, -21,
             -23, -25, -27, -29])

        self.assertTrue(time.time() - start < max_time)
        start = time.time()
        self.assertEqual(
            balanced_brackets.match_brackets(
                "()(())((()))(((()))())(())()((((((((()(())))()(()))()))))"
            ), [])
        self.assertTrue(time.time() - start < max_time)


if __name__ == '__main__':
    unittest.main()
