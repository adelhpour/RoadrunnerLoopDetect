import sbmlloopdetect

antimony_file = "path/to/antimony/file/.txt"

loop_list = sbmlloopdetect.detect(antimony_file)
print(loop_list)