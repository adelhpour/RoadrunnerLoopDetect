import sbmlloopdetect

sbml_file = "path/to/antimony/file/.xml"

loop_list = sbmlloopdetect.detect(sbml_file, filter_loop_length_list=[2, 3, 4], filter_loop_sign=1, max_num_loops=10)
print(loop_list)