#=========================================
#
#   Ikeda's model
#
#
#=========================================

import random
import numpy as np

R = 1
C1 = .4
C2 = .9
C3 = 6

delta_t = 1
initial_t = 0
#final_t = 1000000
final_t = 10000
#initial_val = [random.random()/10, random.random()/10]
initial_val = [0.1, 0.1]

model_name = "Ikeda"
information = "Ikeda" + "(R, C1, C2, C3) = ("  + str(R) + ", " + str(C1) + ", " + str(C2) + ", " + str(C3) + ")"



def f(state, t):
    x = state[0]
    y = state[1]
    tau = C1 - C3 / (1 + x*x + y*y)
    var_sin = np.sin(tau)
    var_cos = np.cos(tau)
    return np.array([R+C2*(x*var_cos-y*var_sin), 
                       C2*(x*var_sin+y*var_cos)])


def Jf(state):
    x = state[0]
    y = state[1]
    tau = C1 - C3 / (1 + x*x + y*y)
    var_sin = np.sin(tau)
    var_cos = np.cos(tau)
    z1 = x*var_sin + y*var_cos
    z2 = x*var_cos - y*var_sin
    Px = 2 * C3 * x / ((1 + x*x + y*y) ** 2)
    Py = 2 * C3 * y / ((1 + x*x + y*y) ** 2)
    return np.matrix([[var_cos - Px*z1,  -var_sin - Py*z1], 
                      [var_sin - Px*z2,   var_cos + Py*z2]])


