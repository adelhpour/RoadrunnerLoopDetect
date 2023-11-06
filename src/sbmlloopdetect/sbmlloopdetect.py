import os
import roadrunner
import antimony
import loopdetect.core
import pandas


def detect(sbml, filter_loop_length_list=[], filter_loop_sign=None, max_num_loops=100000):
    rr = None
    initialize_antimony()
    is_file = check_if_it_is_file(sbml)
    if is_file:
        rr = get_roadrunner_object_from_file(sbml)
    else:
        rr = get_roadrunner_object_from_string(sbml)

    loop_list = loopdetect.core.find_loops_noscc(rr.getFullJacobian(), max_num_loops)
    if len(filter_loop_length_list):
        loop_list = filter_length(loop_list, filter_loop_length_list)
    if filter_loop_sign:
        loop_list = filter_sign(loop_list, filter_loop_sign)

    return loop_list


def initialize_antimony():
    antimony.clearPreviousLoads()
    antimony.freeAll()


def check_if_it_is_file(possible_file):
    if os.path.isfile(possible_file):
        return True

    return False


def get_roadrunner_object_from_file(file):
    code = antimony.loadAntimonyFile(file)
    if code != -1:
        return roadrunner.RoadRunner(antimony.getSBMLString())
    else:
        return roadrunner.RoadRunner(file)


def get_roadrunner_object_from_string(string):
    code = antimony.loadAntimonyString(string)
    if code != -1:
        return roadrunner.RoadRunner(antimony.getSBMLString())
    else:
        return roadrunner.RoadRunner(string)

def filter_length(loop_list, loop_length_list):
    return loop_list[~loop_list['length'].isin(loop_length_list)]

def filter_sign(loop_list, loop_sign):
    return loop_list[loop_list['sign'] != loop_sign]
