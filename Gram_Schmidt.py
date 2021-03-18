#==================================================
#
#   Lyapunov exponent calclulator
#
#   gram-schmidt method
#
#==================================================


def Gram_Schmidt(input_matrix):
    import numpy as np 
    from copy import deepcopy

    # Initial and check size of matrix
    input_matrix = np.array(input_matrix)
    input_matrix = np.transpose(input_matrix)
    
    size1 = np.size(input_matrix[:, 0])
    size2 = np.size(input_matrix[0, :])

    if size1 != size2:
        ValueError("Input matrix in Gram_Schmidt must be a square.")
    
    # Main gram-schmidt method
    squ_vals = []
    return_matrix = []
    
    for kase in range(0, size1):
        curr_mat = input_matrix[kase, :]
        final_mat = input_matrix[kase, :]
        for i in range(0, kase):
            final_mat -= (sum(return_matrix[i] * curr_mat) / squ_vals[i]) * return_matrix[i]
        return_matrix.append(final_mat)
        squ_vals.append(sum(final_mat * final_mat))
    
    # return normalization and non-normalization solution
    final_mat = []
    final_mat_norm = []
    for kase in range(0, size1):
        curr_vec = return_matrix[kase]
        final_mat.append(deepcopy(curr_vec))
        curr_vec /= np.linalg.norm(curr_vec)
        final_mat_norm.append(deepcopy(curr_vec))
    
    final_mat = np.matrix(np.transpose(final_mat))
    final_mat_norm = np.matrix(np.transpose(final_mat_norm))
    
    return final_mat, final_mat_norm
