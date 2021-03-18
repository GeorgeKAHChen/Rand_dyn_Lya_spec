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
import matplotlib.pyplot as plt

import Init
from Gram_Schmidt import Gram_Schmidt
from Read_Model import Read_Model
import Parameter
COLOR_LOOP = ["r", "g", "b", "c", "m"]


def main():
    initial_val, initial_t, _, delta_t, _, Jacobian = Read_Model(Parameter.MODEL_FILE)

    output_vals = [[0 for n in range((len(initial_val)))]]
    orth_mat = np.eye(len(initial_val))
    curr_time = initial_t
    time_series = [initial_t]
    for kase in range(0, len(Jacobian) - 1):
        if kase % 1000 == 0:
            print(kase, len(Jacobian) - 2, end = "\r")
        tmp = Jacobian[kase] * np.matrix(orth_mat)
        _, orth_mat = Gram_Schmidt(tmp)
        new_output = deepcopy(output_vals[len(output_vals) - 1])
        for i in range(0, len(new_output)):
            norm = np.linalg.norm(tmp[:, i])
            new_output[i] = ((new_output[i] * (curr_time - initial_t)) + np.log(norm)) / (curr_time + delta_t - initial_t)
        curr_time += delta_t
        time_series.append(curr_time)
        output_vals.append(new_output)
    print()
    
    fig = plt.gcf()
    fig.set_size_inches(25, 3)
    output_vals = np.matrix(output_vals)
    plt.grid(True)
    
    for i in range(0, len(initial_val)):
        val = np.array(output_vals[:, i].reshape(-1).reshape(-1))
        plt.plot(time_series, val[0], COLOR_LOOP[(i + 1) % len(COLOR_LOOP)])

    sum_val = []
    for i in range(0, len(output_vals)):
        sum_val.append(np.sum(output_vals[i][0]))
    plt.plot(time_series, sum_val, COLOR_LOOP[0])

    print()
    output_str = "Output Vals\nLyapunov vals: \t"
    output_str += str(output_vals[len(output_vals) - 1])
    output_str += "\n sum: " + str(sum_val[len(sum_val) - 1])
    print(output_str)
    plt.show()  
    



if __name__ == '__main__':
    main()