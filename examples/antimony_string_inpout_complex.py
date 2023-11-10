import loopdetect.core

import sbmlloopdetect

antimony_string = """
S0 + S3 -> S5; k0*S0*S3
$S6 -> S3; k3*S6
S5 -> S4; k4*S5
S0 -> S4 + S1; k6*S0
S5 + S1 -> S1; k7*S5*S1
S4 -> S0; k8*S4
S0 + S2 -> S5 + S5; k9*S0*S2
S3 -> S2 ; k12*S3
S2 + S1 -> S2; k13*S2*S1
k0 = 5.568618742610358
k1 = 10.334053929013727
k2 = 12.504071359451485
k3 = 600
k4 = 30
k5 = 0.13857718386978912
k6 = 10.8838639543754
k7 = 0.3232088589872082
k8 = 82.12892372743072
k9 = 0.5482032107469397
k10 = 2.6774814672205745
k11 = 1.0644590769921605
k12 = 32.67282987439573
k13 = 1.526309338016591
k14 = 2.9350756056827865
k15 = 4.080029753799227
k16 = 0.8576073122583439
S0 = 1.0
S1 = 5.0
S2 = 9.0
S3 = 3.0
S4 = 10.0
S5 = 3.0
S6 = 7.0
S7 = 1.0
S8 = 6.0
S9 = 3.0
"""


loop_list = sbmlloopdetect.detect(antimony_string, filter_loop_length_list=[2, 3, 4], filter_positive_loops=True, max_num_loops=10)
print(loop_list)