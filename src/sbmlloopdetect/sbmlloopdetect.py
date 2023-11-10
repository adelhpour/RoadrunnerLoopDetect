import os
import roadrunner
import antimony
import loopdetect.core
import pandas


def detect(sbml, filter_loop_length_list=[], filter_positive_loops=False,
           filter_negative_loops=False, use_node_names=True, max_num_loops=100000):
    """

    Function to determine all loops in the Jacobian matrix of an SBML model.

    :Parameters:

        - sbml: an sbml model in the form of an sbml string, sbml file, antimony string, or antimony file
        - filter_loop_length_list (list, optional): a list (default: []) that determines which loop lengths to be
            filtered and not displayed in the returned value
        - filter_positive_loops(boolean, optional): a boolean (default: False) that determines whether to filter
            and not display positive loops or not
        - filter_negative_loops (boolean, optional): a boolean (default: False) that determines whether to filter
            and not display negative loops or not
        - use_node_names (boolean, optional): a boolean (default: True) that determines whether to replace the nodes
            indices with node names or not
        - max_num_loops (int, optional): positive integer (default: 1e5) giving the maximum number of reported
            loops. Note that only up to max_num_loops loops are returned (without warning)

    :Returns:

        A pandas dataframe: dataframe with the three columns "loop", "length", and "sign" that contain the
            information on one feedback loop in each row. "loop" gives the order of the indices (or their names in SBML)
            forming the loop as tuple, "length" indicates the number of participating species and "sign" is +1 or -1
            indicating a positive or a negative loop, respectively.


    :Examples:
        Define the Jacobian matrix of an antiomony model and compute all feedback loops

        #import the relevant packages
        import sbmlloopdetect
        #define an antimony model
        antimony_string = \"""
        # Sample Antimony model:
        J0: S1 -> S2 + S3; k1*S1 # Mass-action kinetics
        J1: S2 -> S3 + S4; k2*S2

        S1 = 10 # The initial concentration of S1
        S2 = 0  # The initial concentration of S3
        S3 = 3  # The initial concentration of S3
        S4 = 0  # The initial concentration of S4

        k1 = 0.1 # The value of the kinetic parameter from J0.
        k2 = 0.2 # The value of the kinetic parameter from J1.
        \"""
        #compute the loop list
        loop_list = sbmlloopdetect.detect(antimony_string, filter_loop_length_list=[2, 3, 4],
                    filter_positive_loops=True, max_num_loops=10)
    """


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
    if filter_positive_loops:
        loop_list = filter_sign(loop_list, 1)
    if filter_negative_loops:
        loop_list = filter_sign(loop_list, -1)
    if use_node_names:
        loop_list = replace_node_index_with_name(loop_list, rr)

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

def replace_node_index_with_name(loop_list, rr):
    species_ids = rr.getModel().getFloatingSpeciesIds()
    loops = list(loop_list['loop'])
    for loop_index in range(len(loops)):
        loop = list(loops[loop_index])
        for item_index in range(len(loop)):
            loop[item_index] = species_ids[loop[item_index]]
        loops[loop_index] = tuple(loop)
    loop_list['loop'] = loops

    return loop_list
