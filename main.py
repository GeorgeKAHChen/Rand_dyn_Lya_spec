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
from Read_Model import Read_Model
import Parameter


def main():
    initial_val, initial_t,final_t, delta_t, states, Jacobian = Read_Model(Parameter.MODEL_FILE)
    




if __name__ == '__main__':
    main()