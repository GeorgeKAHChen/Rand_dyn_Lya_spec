#==================================================
#
#   Lyapunov exponent calclulator
#
#   Parameter
#
#==================================================

MULTI_CORE = 4
# For multi code calculation
#MODEL_FILE = ["./", "Output", "Logistic20210319034455.model"]
#MODEL_FILE = ["./", "Output", "Henon20210319034530.model"]
#MODEL_FILE = ["./", "Output", "Lorenz20210319034625.model"]
#MODEL_FILE = ["./", "Output", "Rossler20210319034729.model"]
#MODEL_FILE = ["./", "Output", "Henon20210319035439.model"]
MODEL_FILE = ["./", "model", "Lorenz20210318225749.model"]

EPSILON = 1/3
GENERATOR_LOOP = 10
BOX_DIMENSION_READ = True