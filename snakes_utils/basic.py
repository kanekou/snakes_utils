# (C) 2021-2022 Kohei Kaneshima

# This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with this library; If not, see <https://www.gnu.org/licenses/>.

from .utils import utils
from collections import defaultdict
from snakes.nets import *
import snakes.plugins
snakes.plugins.load("gv", "snakes.nets", "nets")


class Basic:
    def __init__(self, n):
        self.__n = n
        self.__places = n._place.keys()
        self.__trans = n._trans.keys()
        self.__postplaces_trans_map = utils.extract_graph_topology(self.__n, self.__trans, post=True)
        self.__preplaces_trans_map = utils.extract_graph_topology(self.__n, self.__trans)
        self.__posttrans_place_map = self.extract_trans(post=True)
        self.__pretrans_place_map = self.extract_trans()
        self.__guards = self.extract_guards()

    @property
    def guards(self):
        return self.__guards

    @property
    def preplaces_trans_map(self):
        return self.__preplaces_trans_map

    @property
    def postplaces_trans_map(self):
        return self.__postplaces_trans_map

    @property
    def trans(self):
        return self.__trans

    @property
    def places(self):
        return self.__places

    @property
    def pretrans_place_map(self):
        return self.__pretrans_place_map

    @property
    def posttrans_place_map(self):
        return self.__posttrans_place_map

    def extract_trans(self, post=False):
        p_t_map = self.__preplaces_trans_map if post else self.__postplaces_trans_map
        data = defaultdict(list)
        for (trans, places) in p_t_map.items():
            if not places:
                continue

            for place in places:
                data[place].append(trans)
        return dict(data)

    def extract_guards(self):
        pt = {}
        for t in self.__n._trans:
            pt[t] = self.__n._trans[t].guard._str

        return pt
