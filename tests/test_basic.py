# Copyright (c) 2021 Kohei Kaneshima (kanekou)
# This software is released under the MIT License, see LICENSE.txt.

import unittest
from collections import defaultdict
from snakes.nets import *
import snakes_utils

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.__net = self.init_petrinet()

    def init_petrinet(self):
        n = PetriNet('sample')
        n.add_place(Place('p0', [1]))
        n.add_place(Place('p1', [1]))
        n.add_transition(Transition('t0'))
        n.add_transition(Transition('t1'))
        n.add_input('p0', 't0', Variable('x'))
        n.add_output('p1', 't0', Variable('x'))
        n.add_input('p1', 't1', Variable('x'))

        return n


    def test_extract_post_trans(self):
        expected = {'p0': ['t0'], 'p1': ['t1']}
        su = snakes_utils.Basic(self.__net)
        actual = su.extract_trans(post=True)

        self.assertEqual(expected, actual)

    def test_extract_pre_trans(self):
        expected = {'p1': ['t0']}
        su = snakes_utils.Basic(self.__net)
        actual = su.extract_trans()

        self.assertEqual(expected, actual)

    def test_extract_graph_topology_case_post(self):
        expected = {'t0': ['p1'], 't1': []}
        su = snakes_utils.Basic(self.__net)
        actual = su.postplaces_trans_map

        self.assertEqual(expected, actual)


    def test_extract_graph_topology_case_pre(self):
        expected = {'t0': ['p0'], 't1': ['p1']}
        su = snakes_utils.Basic(self.__net)
        actual = su.preplaces_trans_map

        self.assertEqual(expected, actual)

    def test_guards(self):
        expected = {'t0': 'True', 't1': 'True'}
        su = snakes_utils.Basic(self.__net)
        actual = su.guards

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
