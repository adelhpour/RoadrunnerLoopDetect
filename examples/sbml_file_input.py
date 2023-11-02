import sbmlloopdetect

sbml_file = "path/to/antimony/file/.xml"

loop_list = sbmlloopdetect.detect(sbml_file)
print(loop_list)