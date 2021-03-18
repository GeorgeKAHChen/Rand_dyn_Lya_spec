#==================================================
#
#   Lyapunov exponent calclulator
#
#   Data generator
#
#==================================================

import multiprocessing
import numpy as np

import Init
import Parameter 
from model import Lorenz as model


MULTI_CORE = Parameter.MULTI_CORE

def Runge_Kutta(func, x0, t0, tn, delta_t):
    import numpy as np
    Val_set = [x0]
    curr_t = t0
    while 1:
        if curr_t > tn:
            break
        curr_x = Val_set[len(Val_set) - 1]
        k1 = np.array(eval(func)(curr_x, curr_t))
        k2 = np.array(eval(func)(curr_x + delta_t * k1 * 0.5, curr_t + delta_t * 0.5))
        k3 = np.array(eval(func)(curr_x + delta_t * k2 * 0.5, curr_t + delta_t * 0.5))
        k4 = np.array(eval(func)(curr_x + delta_t * k2, curr_t + delta_t))
        curr_x = curr_x + delta_t * (k1 + 2 * k2 + 2 * k3 + k4) * (1/6)
        Val_set.append(curr_x)
        curr_t += delta_t

    return np.array(Val_set)



def main():
    initial_val = model.initial_val
    initial_t = model.initial_t
    final_t = model.final_t
    delta_t = model.delta_t
    information = model.information
    String = information
    String += "\n"
    String += str(initial_t) + " "
    String += str(final_t) + " "
    String += str(delta_t) + " \n"
    print(String)
    
    print("Data generate")
    Val_set = Runge_Kutta("model.f", initial_val, initial_t, final_t, delta_t)
    Val_set = Val_set.tolist()
    String += Init.ArrOutput(Val_set, Mode = 0, Save_File = False)

    Jaco_set = []
    print("Jacobian generate") 
    pool = multiprocessing.Pool(processes = MULTI_CORE)
    Jaco_set = pool.map(model.Jf, Val_set)
    
    print("Model Output")
    tmp = []
    for i in range(0, len(Jaco_set)):
        tmp.append(np.resize(Jaco_set[i], (9)).tolist())
    String += Init.ArrOutput(tmp, Mode = 0, Save_File = False)
    
    FileName = model.model_name + str(Init.GetTime()) + ".model"
    File = open(FileName, "a")
    File.write(String)
    File.close()


if __name__ == '__main__':
    main()