#==================================================
#
#   Lyapunov exponent calclulator
#
#   Box_Dimension
#
#==================================================

import os
import numpy as np
import multiprocessing
from functools import partial
from contextlib import contextmanager

import Init
from Read_Model import Read_Model
import Parameter
COLOR_LOOP = ["r", "g", "b", "c", "m"]


def FindBox(curr_state, axis_set, epsilon):
    appro_axis = []
    for kase in range(0, len(axis_set)):
        appro_axis.append(int( (curr_state[kase] - axis_set[kase][0]) / epsilon ) - 1)

    for kase in range(0, len(axis_set)):
        if appro_axis[kase] < 0:
            appro_axis[kase] = 0

    point_axis = []
    for kase in range(0, len(axis_set)):
        curr_axis = appro_axis[kase]
        for i in range(0, 5):
            new_curr_axis = curr_axis + i
            if new_curr_axis > len(axis_set[kase]):
                point_axis.append(kase - 2)
                break
            else:
                if curr_state[kase] > axis_set[kase][new_curr_axis] and curr_state[kase] < axis_set[kase][new_curr_axis + 1]:
                    point_axis.append(new_curr_axis)
                    break

    string = ""
    for kase in range(0, len(axis_set)):
        string += str(point_axis[kase])
        string += "."
    return string



@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()



def main():
    initial_val, _, _, _, states, _ = Read_Model(Parameter.MODEL_FILE)
    new_states = np.array(states)
    epsilon = Parameter.EPSILON
    min_set = []
    max_set = []
    axis_set = []
    for kase in range(0, len(initial_val)):
        min_set.append(min(new_states[:, kase]))
        max_set.append(max(new_states[:, kase]))

    for kase in range(0, len(initial_val)):
        val = min_set[kase] - epsilon/2
        tmp = []
        while 1:
            tmp.append(val)
            if val > max_set[kase]:
                break
            val += epsilon
        axis_set.append(tmp)

    #pool = multiprocessing.Pool(processes = )
    #Box_Fill = pool.map(, )
    
    #with poolcontext(processes = Parameter.MULTI_CORE) as pool:
    #    Box_Fill = pool.map(partial(FindBox, axis_set=axis_set, epsilon=epsilon), states)
    Box_Fill = []
    for i in range(0, len(states)):
        Box_Fill.append(FindBox(states[i], axis_set, epsilon))
    #print(Box_Fill)
    Box_Fill = set(Box_Fill)
    Box_Dimension = np.log(len(Box_Fill)) / np.log(1/epsilon)
    print(epsilon, len(Box_Fill), Box_Dimension)


if __name__ == '__main__':
    main()




