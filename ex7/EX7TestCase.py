import unittest

from SolveLinear3 import solve_linear_3
import ex7



# #############################################################################
# Unit testing for ex7
# Written by Yekhezkel Yovel
# Contributors: Dotan Nir, Ziv Ben-Aharon
#
# Feel free to use and distribute for whatever good you find in it.
# BUT: No one, including the writer or any of the contributors, shall be
# seen responsible for this code or any of it's outcomes.
#
# Usage:
# place this file in project folder and:
# in PyCharm: right-click file and click 'run' (green "play" button)
# in CMD/Shell: run the following
# python <filename>.py
# or:
# python3 <filename>.py
# #############################################################################


class EX7TestCase(unittest.TestCase):
    def test_is_point_inside_triangle(self):
        # triangle vertices:
        v1 = (2, 2)
        v2 = (1, 6)
        v3 = (4, 5)

        # True cases:
        # point - inside triangle
        point = (3, 4)

        # a,b and c are defined to be the output of solve_linear_3, so
        # this is how we test them (a lambda is a way to define a function
        # and return it as a value, so that we can put it in a variable):
        get_abc = lambda: solve_linear_3(
            [[v1[0], v2[0], v3[0]], [v1[1], v2[1], v3[1]], [1, 1, 1]],
            [point[0], point[1], 1])
        # We could test a,b,c as well, if we wanted to. But since
        # these are defined to be the output of a different function from
        # the one we test here, we would do it in a different function than
        # this one. Anyway, since we are not supposed to change
        # solve_linear_3 at all it is probably unnecessary to test it.

        self.assertEqual((True, get_abc()),
                         ex7.is_point_inside_triangle(point, v1, v2, v3))
        # point - on triangle edge
        point = (3, 3.5)
        self.assertEqual((True, get_abc()),
                         ex7.is_point_inside_triangle(point, v1, v2, v3))
        # point - same as vertex
        point = (4, 5)
        self.assertEqual((True, get_abc()),
                         ex7.is_point_inside_triangle(point, v1, v2, v3))

        # False cases:
        # point - outside triangle
        point = (4, 3)
        self.assertEqual((False, get_abc()),
                         ex7.is_point_inside_triangle(point, v1, v2, v3))

    def test_create_triangles(self):
        triangles_1 = ex7.create_triangles(
            [(0, 0), (100, 0), (100, 100), (0, 100)])
        triangles_2 = [((0, 0), (100, 0), (100, 100)),
                       ((0, 0), (0, 100), (100, 100))]

        # Since output is a tuple and set-match is required, must manually
        # match items. Defining a match action for multiple use.
        def match(tr_1, tr_2):
            # a different length would suggest different lists.
            self.assertEqual(len(tr_1), len(tr_2))
            matches = {}
            for t1 in tr_1:
                for t2 in tr_2:
                    if t1 in matches or t2 in matches:
                        continue
                    if set(t1) == set(t2):
                        matches[t1] = t2
                        matches[t2] = t1
                        continue
            for t1 in tr_1:
                self.assertTrue(t1 in matches, t1)

        # triggering the match action.
        match(triangles_1, triangles_2)

        triangles_1 = ex7.create_triangles(
            [(0, 0), (100, 0), (100, 100), (0, 100), (80, 10)])
        triangles_2 = [((0, 0), (100, 0), (80, 10)),
                       ((0, 0), (100, 100), (80, 10)),
                       ((100, 100), (100, 0), (80, 10)),
                       ((0, 0), (0, 100), (100, 100))]

        # triggering the match action.
        match(triangles_1, triangles_2)

        triangles_1 = ex7.create_triangles(
            [(0, 0), (100, 0), (100, 100), (0, 100), (80, 10), (70, 5)])
        triangles_2 = [((0, 0), (100, 0), (70, 5)),
                       ((0, 0), (70, 5), (80, 10)),
                       ((70, 5), (100, 0), (80, 10)),
                       ((0, 0), (100, 100), (80, 10)),
                       ((100, 100), (100, 0), (80, 10)),
                       ((0, 0), (0, 100), (100, 100))]

        # triggering the match action.
        match(triangles_1, triangles_2)

        triangles_1 = ex7.create_triangles(
            [(0, 0), (500, 0), (500, 350), (0, 350), (100, 0)])
        triangles_2 = [((0, 0), (0, 350), (500, 350)),
                       ((100, 0), (0, 0), (500, 0)),
                       ((100, 0), (0, 0), (500, 350)),
                       ((100, 0), (500, 0), (500, 350))]

        # triggering the match action.
        match(triangles_1, triangles_2)

    def test_get_intermediate_triangles(self):

        self.assertEqual([((40.0, 40.0), (40.0, 40.0), (40.0, 40.0)),
                          ((80.0, 80.0), (80.0, 80.0), (80.0, 80.0))],
                         ex7.get_intermediate_triangles(
                             [((0, 0), (0, 0), (0, 0)),
                              ((0, 0), (0, 0), (0, 0))],
                             [((100, 100), (100, 100), (100, 100)),
                              ((200, 200), (200, 200), (200, 200))], 0.4))

        self.assertEqual([((50.0, 50.0), (50.0, 50.0), (50.0, 50.0)),
                          ((100.0, 100.0), (100.0, 100.0), (100.0, 100.0))],
                         ex7.get_intermediate_triangles(
                             [((0, 0), (0, 0), (0, 0)),
                              ((0, 0), (0, 0), (0, 0))],
                             [((100, 100), (100, 100), (100, 100)),
                              ((200, 200), (200, 200), (200, 200))], 0.5))

        self.assertEqual([((70.0, 80.0), (75.0, 85.0), (80.0, 80.0)),
                          ((145.0, 155.0), (150.0, 150.0), (150.0, 150.0))],
                         ex7.get_intermediate_triangles(
                             [((30, 40), (20, 30), (10, 0)),
                              ((70, 80), (60, 50), (40, 30))],
                             [((110, 120), (130, 140), (150, 160)),
                              ((220, 230), (240, 250), (260, 270))], 0.5))

        # def test_get_array_of_matching_points(self):
        # triangles = ex7.create_triangles(
        # [(0, 0), (500, 0), (500, 350), (0, 350), (100, 0), (245, 345)])
        # triangles2 = ex7.create_triangles(
        # [(0, 0), (500, 0), (500, 350), (0, 350), (100, 0), (240, 340)])
        # inter_triangles = ex7.get_intermediate_triangles(triangles, triangles2,
        # 0.34)
        #     ex7.get_array_of_matching_points((500, 350), triangles,
        #                                      inter_triangles)


if __name__ == '__main__':
    unittest.main()
