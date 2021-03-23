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
import Data_Generator

import Parameter
COLOR_LOOP = ["r", "g", "b", "c", "m"]


def main():
    if Parameter.LYAPUNOV_READ_FILE:
        information, initial_val, initial_t, _, delta_t, Val_Set, Jacobian = Read_Model(Parameter.MODEL_FILE)
    else:
        information, initial_val, initial_t, _, delta_t, Val_Set, Jacobian = Data_Generator.main(OutputFile = False, initial_val =  [], old_information = "", Calc_Jaco = True)

    information, initial_val, _, _, delta_t, Val_Set, Jacobian = Data_Generator.main(OutputFile = False, initial_val = Val_Set[len(Val_Set)-1], old_information = "", Calc_Jaco = True)
    output_vals = [[0 for n in range((len(initial_val)))]]
    final_mat_norm = np.eye(len(initial_val))
    curr_time = initial_t
    time_series = [initial_t]
    for ttl in range(0, Parameter.GENERATOR_LOOP):
        print("Lyapunov spectrum")
        print(ttl, Parameter.GENERATOR_LOOP)
        for kase in range(0, len(Jacobian) - 1):
            if ttl != 0 and kase == 0:
                continue
            if kase % 1000 == 0:
                print(kase, len(Jacobian) - 2, end = "\r")
            final_mat_norm = Jacobian[kase] * np.matrix(final_mat_norm)
            final_mat, final_mat_norm = Gram_Schmidt(final_mat_norm)
            new_output = deepcopy(output_vals[len(output_vals) - 1])
            for i in range(0, len(new_output)):
                norm = np.linalg.norm(final_mat[:, i])
                new_output[i] = ((new_output[i] * (curr_time - time_series[0])) + np.log(norm)) / (curr_time + delta_t - time_series[0])
            curr_time += delta_t
            time_series.append(curr_time)
            output_vals.append(new_output)
        
        print(output_vals[len(output_vals) - 1])
        
        if ttl + 1 != Parameter.GENERATOR_LOOP:
            information, _, _, _, _, Val_Set, Jacobian = Data_Generator.main(OutputFile = False, initial_val = Val_Set[len(Val_Set)-1], old_information = information, Calc_Jaco = True)
        
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


"""
Sample Result

Logistic(3.9) = 0.4945
Henon(1.4, 0.3) = (0.418, -1.622)
Ikeda(1, 0.4, 0.9, 6) = (0.51, -0.72)
Lorenz(28, 10, 2.667) = (0.905, 0, -14.571)
Lorenz(142, 10, 2.667) = (1.253, 0, -14.920)
Lorenz(148, 10, 2.667) = (0, -0.4274, -13.2398)
Rossler(0.2, 0.2, 5.7) = (0.0696, 0, -5.392)


"""