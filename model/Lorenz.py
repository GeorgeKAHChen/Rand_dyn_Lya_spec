#=========================================
#
#   Lorenz model 
#
#
#=========================================
import random
import numpy as np
rho = 28.0
#rho = 142.0
#rho = 148.0
sigma = 10.0
beta = 8.0 / 3.0

#rho = 45.92
#sigma = 4
#beta = 10


#delta_t = 0.01
delta_t = 0.0001
initial_t = 0
final_t = 10
initial_val = [1.0, 1.0, 1.0]
model_name = "Lorenz"
information = "Lorenz" + "(rho, sigma, beta) = ("  + str(rho) + ", " + str(sigma) + ", " + str(beta) + ")"


def f(state, t):
    x, y, z = state 
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

def Jf(state):
    #print(state)
    x, y, z = state
    #return Delta_t * np.matrix([[-sigma, sigma, 0], [(rho - z), -1, -x], [y, x, -beta]]) + np.eye(3)
    return np.matrix([[1 - delta_t * sigma,         delta_t * sigma,        0], 
                      [delta_t * (rho - z),         1 - delta_t ,           -delta_t * x], 
                      [delta_t * y,                 delta_t * x,            1 - delta_t * beta]])

