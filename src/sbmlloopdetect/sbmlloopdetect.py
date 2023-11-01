import os
import roadrunner
import antimony
import loopdetect.core


def detect(sbml):
    rr = None
    antimony.clearPreviousLoads()
    antimony.freeAll()
    is_file = check_if_it_is_file(sbml)
    if is_file:
        rr = get_roadrunner_object_from_file(sbml)
    else:
        rr = get_roadrunner_object_from_string(sbml)

    return loopdetect.core.find_loops_noscc(rr.getFullJacobian())

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
