import roadrunner
import loopdetect.core


def detect(sbml):
    rr = roadrunner.RoadRunner(sbml)
    return loopdetect.core.find_loops_noscc(rr.getFullJacobian())