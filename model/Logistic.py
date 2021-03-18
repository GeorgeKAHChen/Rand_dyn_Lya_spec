#=========================================
#
#   Logistic model
#
#
#=========================================

a = 3.95

delta_t = 1.0
initial_t = 0
final_t = 100000
initial_val = [random.random()]
model_name = "Logistic"
information = "Logistic" + "(a) = ("  + str(a) + ")"



def f(state, t):
    x = state[0]
    return [a * x * (1 - x)]


def Jf(state):
    x = state[0]
    return np.matrix([a - 2 * a * x])

