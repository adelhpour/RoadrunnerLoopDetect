import sbmlloopdetect

antimony_file = "path/to/antimony/file/.txt"

loop_list = sbmlloopdetect.detect(antimony_file, filter_loop_length_list=[2, 3, 4], filter_positive_loops=True, max_num_loops=10)
print(loop_list)