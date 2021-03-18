#==================================================
#
#   Lyapunov exponent calclulator
#
#   Read_Model
#
#==================================================

def Read_Model(MODEL_FILE):
    import numpy as np
    from copy import deepcopy
    import os 
    import Init

    model_path = ""
    for i in range(0, len(MODEL_FILE)):
        model_path = os.path.join(model_path, MODEL_FILE[i])
    File = open(model_path, "r")
    FileLine = File.readline()
    information = FileLine
    FileLine = File.readline()
    initial_t, final_t, delta_t = Init.FileReadLine(FileLine, mode = "float")
    initial_val = []
    states = []
    Jacobian = []
    FileLine = File.readline()
    while 1:
        if not FileLine:
            break
        array = Init.FileReadLine(FileLine, mode = "float")
        if len(states) == 0:
            initial_val = deepcopy(array)
        if len(array) == len(initial_val):
            states.append(array)
        else:
            array = np.reshape(np.matrix(array), (3, 3))
            Jacobian.append(array)
        FileLine = File.readline()

    return initial_val, initial_t,final_t, delta_t, states, Jacobian