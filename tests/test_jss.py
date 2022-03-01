# (C) 2021-2022 Kohei Kaneshima

# This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with this library; If not, see <https://www.gnu.org/licenses/>.

import unittest
from collections import defaultdict
from snakes.nets import *
import snakes_utils


class TestJSS(unittest.TestCase):
    def setUp(self):
        self.__net = self.init_petrinet()
        self.__rflag = 'm'

    def init_petrinet(self):
        n = PetriNet('Job Shop Scheduling')
        n.add_place(Place('p0', [1]))
        n.add_place(Place('p1'))
        n.add_place(Place('p2'))
        n.add_place(Place('p3'))
        n.add_place(Place('p4'))
        n.add_place(Place('p5', [1]))
        n.add_place(Place('p6'))
        n.add_place(Place('p7'))
        n.add_place(Place('p8'))
        n.add_place(Place('p9'))
        n.add_place(Place('p10', [1]))
        n.add_place(Place('p11'))
        n.add_place(Place('p12'))
        n.add_place(Place('p13'))
        n.add_place(Place('p14'))

        n.add_place(Place('m0'))
        n.add_place(Place('m1'))
        n.add_place(Place('m2'))

        pt = {'t1': '1',
              't2': '1',
              't3': '2',
              't0': '2',
              't4': '1',
              't6': '2',
              't7': '1',
              't5': '3',
              't8': '2',
              't9': '3',
              't10': '2',
              't11': '2'}

        t_num = 12  # Number of operations
        for i in range(t_num):
            t_name = f't{i}'
            t_pt = pt[t_name]
            n.add_transition(Transition(t_name, Expression(t_pt)))

        start = 0
        end = per_p = 4
        job_num = 3
        for j in range(job_num):
            for i in range(start, end):
                n.add_input('p{}'.format(i+j), 't{}'.format(i), Variable('x'))
                n.add_output('p{}'.format(i+j+1),
                             't{}'.format(i), Variable('x'))

            start = end
            end += per_p

        # Machines
        m_dict = {'m1': {'t2', 't5', 't6', 't1'},
                  'm2': {'t7', 't3', 't11', 't10'},
                  'm0': {'t8', 't9', 't4', 't0'}}
        for m, t in m_dict.items():
            for e in t:
                n.add_input(m, e, Variable('x'))
                n.add_output(m, e, Variable('x'))

        return n

    def test_extract_post_places(self):
        expected = {'t1': 'p2',
                    't2': 'p3',
                    't3': 'p4',
                    't0': 'p1',
                    't4': 'p6',
                    't6': 'p8',
                    't7': 'p9',
                    't5': 'p7',
                    't8': 'p11',
                    't9': 'p12',
                    't10': 'p13',
                    't11': 'p14'}

        su = snakes_utils.JSS(self.__net, rflag=self.__rflag)
        actual = su.extract_places(post=True)

        self.assertEqual(expected, actual)

    def test_extract_post_trans(self):
        expected = {'p0': 't0',
                    'p1': 't1',
                    'p2': 't2',
                    'p3': 't3',
                    'p5': 't4',
                    'p6': 't5',
                    'p7': 't6',
                    'p8': 't7',
                    'p10': 't8',
                    'p11': 't9',
                    'p12': 't10',
                    'p13': 't11'}

        su = snakes_utils.JSS(self.__net, rflag=self.__rflag)
        actual = su.extract_trans(post=True)

        self.assertEqual(expected, actual)

    def test_extract_resources(self):
        expected = ['m0', 'm1', 'm2']
        su = snakes_utils.JSS(self.__net, rflag=self.__rflag)
        actual = su.extract_resources(rflag=self.__rflag)

        self.assertEqual(expected, actual)

    def test_extract_processing_time(self):
        expected = {'t1': 1,
                    't2': 1,
                    't3': 2,
                    't0': 2,
                    't4': 1,
                    't6': 2,
                    't7': 1,
                    't5': 3,
                    't8': 2,
                    't9': 3,
                    't10': 2,
                    't11': 2}

        su = snakes_utils.JSS(self.__net, self.__rflag)
        actual = su.pt

        self.assertEqual(expected, actual)

    def test_extract_graph_topology_case_post(self):
        expected = {'t1': ['p2', 'm1'],
                    't2': ['p3', 'm1'],
                    't3': ['p4', 'm2'],
                    't0': ['p1', 'm0'],
                    't4': ['p6', 'm0'],
                    't6': ['p8', 'm1'],
                    't7': ['p9', 'm2'],
                    't5': ['p7', 'm1'],
                    't8': ['p11', 'm0'],
                    't9': ['p12', 'm0'],
                    't10': ['p13', 'm2'],
                    't11': ['p14', 'm2']}

        su = snakes_utils.JSS(self.__net, rflag=self.__rflag)
        actual = su.postplaces_trans_map(resource=True)

        self.assertEqual(expected, actual)

    def test_extract_graph_topology_case_pre(self):
        expected = {'t1': ['p1', 'm1'],
                    't2': ['p2', 'm1'],
                    't3': ['p3', 'm2'],
                    't0': ['p0', 'm0'],
                    't4': ['p5', 'm0'],
                    't6': ['p7', 'm1'],
                    't7': ['p8', 'm2'],
                    't5': ['p6', 'm1'],
                    't8': ['p10', 'm0'],
                    't9': ['p11', 'm0'],
                    't10': ['p12', 'm2'],
                    't11': ['p13', 'm2']}

        su = snakes_utils.JSS(self.__net, rflag=self.__rflag)
        actual = su.preplaces_trans_map(resource=True)

        self.assertEqual(expected, actual)

    def test_extract_required_resources_by_trans(self):
        expected = defaultdict(set,
                               {'t1': {'m1'},
                                't2': {'m1'},
                                   't3': {'m2'},
                                   't0': {'m0'},
                                   't4': {'m0'},
                                   't6': {'m1'},
                                   't7': {'m2'},
                                   't5': {'m1'},
                                   't8': {'m0'},
                                   't9': {'m0'},
                                   't10': {'m2'},
                                   't11': {'m2'}})

        su = snakes_utils.JSS(self.__net, rflag=self.__rflag)
        actual = su.extract_required_resources_by_trans()

        self.assertEqual(expected, actual)

    def test_extract_required_trans_by_resource(self):
        expected = {'m1': {'t2', 't5', 't6', 't1'},
                    'm2': {'t7', 't3', 't11', 't10'},
                    'm0': {'t8', 't9', 't4', 't0'}}

        su = snakes_utils.JSS(self.__net, rflag=self.__rflag)
        actual = su.extract_required_trans_by_resource(rflag=self.__rflag)
        self.assertEqual(expected, actual)

    def test_get_jobs(self):
        expected = defaultdict(list,
                    {0: ['t0', 't1', 't2', 't3'],
                    1: ['t4', 't5', 't6', 't7'],
                    2: ['t8', 't9', 't10', 't11']})

        su = snakes_utils.JSS(self.__net, rflag=self.__rflag)
        actual = su.jobs
        self.assertTrue(self.assert_equal_jobs(expected, actual))

    # Without considering the order of the keys
    def assert_equal_jobs(self, jobs, jobs2):
        def subtract_list(lst1, lst2):
            lst = lst1.copy()
            for element in lst2:
                try:
                    lst.remove(element)
                except ValueError:
                    return False
            if not lst:
                return True
            return False

        jobs_values = list(jobs.values())
        jobs2_values = list(jobs2.values())
        if not (subtract_list(jobs_values, jobs2_values) or subtract_list(jobs2_values, jobs_values)):
            return False
        return True

if __name__ == "__main__":
    unittest.main()
