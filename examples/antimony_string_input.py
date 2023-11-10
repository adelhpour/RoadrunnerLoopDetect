import loopdetect.core

import sbmlloopdetect

antimony_string = """
# Sample Antimony model:
J0: S1 -> S2 + S3; k1*S1 # Mass-action kinetics
J1: S2 -> S3 + S4; k2*S2 
		
S1 = 10 # The initial concentration of S1
S2 = 0  # The initial concentration of S3
S3 = 3  # The initial concentration of S3
S4 = 0  # The initial concentration of S4
			
k1 = 0.1 # The value of the kinetic parameter from J0.
k2 = 0.2 # The value of the kinetic parameter from J1.
"""

loop_list = sbmlloopdetect.detect(antimony_string, filter_loop_length_list=[2, 3, 4], filter_positive_loops=True, max_num_loops=10)
print(loop_list)