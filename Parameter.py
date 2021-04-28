#==================================================
#
#   Lyapunov exponent calclulator
#
#   Parameter
#
#==================================================
import Init
MULTI_CORE = 1
if Init.SystemJudge() == "Dos":
    MULTI_CORE = 16
elif Init.SystemJudge() == "Darwin":
    MULTI_CORE = 4
else:
    MULTI_CORE = MULTI_CORE

# For multi code calculation
#MODEL_FILE = ["./", "Output", "Logistic20210319034455.model"]
#MODEL_FILE = ["./", "Output", "Henon20210319034530.model"]
#MODEL_FILE = ["./", "Output", "Lorenz20210319034625.model"]
#MODEL_FILE = ["./", "Output", "Rossler20210319034729.model"]
#MODEL_FILE = ["./", "Output", "Henon20210319035439.model"]
#MODEL_FILE = ["./", "model", "Lorenz20210318225749.model"]
MODEL_FILE = ["./", "Output", "Ikeda20210322145714.model"]

EPSILON = 1/3
GENERATOR_LOOP = 100
BOX_DIMENSION_READ = True
LYAPUNOV_READ_FILE = False
CAL_ERROR = True