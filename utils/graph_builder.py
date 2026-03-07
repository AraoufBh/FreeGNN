import numpy as np


def build_adjacency_matrix(coords, threshold=0.5):

    num_nodes = coords.shape[0]
    A = np.zeros((num_nodes, num_nodes))

    for i in range(num_nodes):
        for j in range(num_nodes):
            dist = np.linalg.norm(coords[i] - coords[j])
            if dist < threshold:
                A[i, j] = 1

    return A


def normalize_adjacency(A):
    
    D = np.sum(A, axis=1)
    D_inv = np.diag(1 / (D + 1e-8))
    return D_inv @ A