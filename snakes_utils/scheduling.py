# Copyright (c) 2021 Kohei Kaneshima (kanekou)
# This software is released under the MIT License, see LICENSE.txt.

from .utils import utils
from collections import defaultdict
from snakes.nets import *
import snakes.plugins
snakes.plugins.load("gv", "snakes.nets", "nets")


class Scheduling:
    def __init__(self, n, rflag='r'):
        self.__n = n
        self.__places = n._place.keys()
        self.__trans = n._trans.keys()
        self.__postplaces_trans_map_include_resources = utils.extract_graph_topology(self.__n, self.__trans, post=True)
        self.__preplaces_trans_map_include_resources = utils.extract_graph_topology(self.__n, self.__trans)
        self.__resources = self.extract_resources(rflag=rflag)
        self.__postplaces_trans_map = self.extract_places(post=True)
        self.__preplaces_trans_map = self.extract_places()
        self.__posttrans_place_map = self.extract_trans(post=True)
        self.__pretrans_place_map = self.extract_trans()
        self.__resources_trans_map = self.extract_required_resources_by_trans()
        self.__trans_resource_map = self.extract_required_trans_by_resource(rflag=rflag)
        self.__jobs = self.get_jobs()
        self.__pt = utils.extract_guards(self.__n)

    @property
    def pt(self):
        return self.__pt

    @property
    def resources(self):
        return self.__resources

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

    @property
    def trans_resource_map(self):
        return self.__trans_resource_map

    @property
    def resources_trans_map(self):
        return self.__resources_trans_map

    @property
    def jobs(self):
        return self.__jobs

    def preplaces_trans_map(self, resource=False):
        if resource:
            return self.__preplaces_trans_map_include_resources
        else:
            return self.__preplaces_trans_map

    def postplaces_trans_map(self, resource=False):
        if resource:
            return self.__postplaces_trans_map_include_resources
        else:
            return self.__postplaces_trans_map

    def extract_resources(self, rflag='r'):
        return [k for k in self.__places if k[0][0] == rflag]

    def extract_places(self, post=False):
        places_include_resource = self.__postplaces_trans_map_include_resources if post else self.__preplaces_trans_map_include_resources
        places = {}
        for (key, value) in places_include_resource.items():
            if (value[0] in self.__resources):
                places.setdefault(key, value[1])
            elif(value[1] in self.__resources):
                places.setdefault(key, value[0])
            else:
                print('no place for trans{}'.format(key))

        return places

    def extract_trans(self, post=False):
        places = self.__preplaces_trans_map if post else self.__postplaces_trans_map
        trans = {}
        for (key, value) in places.items():
            trans.setdefault(value, key)
        return trans

    def extract_required_resources_by_trans(self):
        require_resources = defaultdict(set)
        for (key, value) in self.__preplaces_trans_map_include_resources.items():
            if (value[0] in self.__resources):
                require_resources[key].add(value[0])
            elif(value[1] in self.__resources):
                require_resources[key].add(value[1])
            else:
                print(f'places{value} has not machine resource')

        return require_resources

    # It can receive either preplaces_trans_map_include_resources or postplaces_trans_map_include_resources
    def extract_required_trans_by_resource(self, rflag='r'):
        trans_resource_map = defaultdict(set)
        for trans, places in self.__preplaces_trans_map_include_resources.items():
            for place in places:
                if place[0] == rflag:
                    trans_resource_map[place].add(trans)
        return trans_resource_map

    def get_jobs(self):
        init_tokens = set(self.__places) - \
            set(self.__pretrans_place_map) - set(self.__resources)
        jobs = defaultdict(list)

        for idx, fp in enumerate(init_tokens):
            self.extract_job(jobs, fp, idx)

        return dict(jobs)


    def extract_job(self, jobs, place, job_idx):
        if not (place in self.__posttrans_place_map):
            return

        nt = self.posttrans_place_map[place]
        np = self.postplaces_trans_map(resource=False)[nt]

        # jobs = { job_number: [trans_id,...],... }
        jobs[job_idx].append(nt)

        return self.extract_job(jobs, np, job_idx)
