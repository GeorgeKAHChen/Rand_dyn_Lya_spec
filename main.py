#==================================================
#
#   Lyapunov exponent calclulator
#
#   main
#
#==================================================

import os
import numpy as np
from copy import deepcopy
import Init
from Gram_Schmidt import Gram_Schmidt
import Parameter



def read_model():
    model_path = ""
    for i in range(0, len(Parameter.MODEL_FILE)):
        model_path = os.path.join(model_path, Parameter.MODEL_FILE[i])
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



def main():
    initial_val, initial_t,final_t, delta_t, states, Jacobian = read_model()
    




if __name__ == '__main__':
    main()