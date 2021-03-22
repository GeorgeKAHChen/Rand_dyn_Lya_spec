#==================================================
#
#   Lyapunov exponent calclulator
#
#   Data generator
#
#==================================================

#==================================================
# Import your model file here

#from model import Logistic as model
#from model import Henon as model
#from model import Lorenz as model
#from model import Rossler as model
from model import Ikeda as model
#==================================================


import multiprocessing
import numpy as np
import os
import sys

import Init
import Parameter 



MULTI_CORE = Parameter.MULTI_CORE

def Runge_Kutta(func, x0, t0, tn, delta_t):
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


def map_calculator(func, x0, t0, tn, delta_t):
    Val_set = [x0]
    curr_t = t0
    while 1:
        if curr_t > tn:
            break
        Val_set.append(np.array(eval(func)(Val_set[len(Val_set) - 1], curr_t)))
        curr_t += delta_t

    return np.array(Val_set)



def main(OutputFile = False, initial_val = [], old_information = "", Calc_Jaco = True):
    map_model = False

    if len(initial_val) == 0:
        initial_val = model.initial_val
    initial_t = model.initial_t
    final_t = model.final_t
    delta_t = model.delta_t
    information = model.information

    if type(delta_t) == int:
        map_model = True
        delta_t = float(delta_t)

    if len(old_information) != 0:
        if information != old_information:
            while 1:
                print("WARNING, you may used wrong model because old model information is different from new one.")
                print(old_information)
                print(information)
                inp_str = input("Continue? (y/n)")
                if inp_str == "y":
                    break
                elif inp_str == "n":
                    sys.exit()
                else:
                    os.system("clear")
                    print("Input error")
                    continue

    String = information
    String += "\n"
    String += str(initial_t) + " "
    String += str(final_t) + " "
    String += str(delta_t) + " \n"
    print(String)

    print("Data generate")
    if map_model == False:
        Val_set = Runge_Kutta("model.f", initial_val, initial_t, final_t, delta_t)
        Val_set = Val_set.tolist()
        if OutputFile:
            String += Init.ArrOutput(Val_set, Mode = 0, Save_File = False)
    else:
        Val_set = map_calculator("model.f", initial_val, initial_t, final_t, delta_t)
        Val_set = Val_set.tolist()
        if OutputFile:
            String += Init.ArrOutput(Val_set, Mode = 0, Save_File = False)
    Jaco_set = []
    if Calc_Jaco:
        print("Jacobian generate") 
        pool = multiprocessing.Pool(processes = MULTI_CORE)
        Jaco_set = pool.map(model.Jf, Val_set)
    
    if OutputFile:
        print("Model Output")
        tmp = []
        for i in range(0, len(Jaco_set)):
            tmp.append(np.resize(Jaco_set[i], (len(initial_val) * len(initial_val))).tolist())
        String += Init.ArrOutput(tmp, Mode = 0, Save_File = False)
        
        FileName = os.path.join("Output", model.model_name + str(Init.GetTime()) + ".model")
        File = open(FileName, "a")
        File.write(String)
        File.close()

    return information, initial_val, initial_t, final_t, delta_t, Val_set, Jaco_set





if __name__ == '__main__':
    main(OutputFile = True, initial_val = [], old_information = "")