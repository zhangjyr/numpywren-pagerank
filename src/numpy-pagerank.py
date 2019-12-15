import numpy as np

np.random.seed(42)

def pagerank(M, num_iterations = 100, d = 0.85):
 
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    for i in range(num_iterations):
        v = d * M @ v + (1 - d) / N
    return v


M = np.array([[0, 0, 0, 0, 1],
              [0.5, 0, 0, 0, 0],
              [0.5, 0, 0, 0, 0],
              [0, 1, 0.5, 0, 0],
              [0, 0, 0.5, 1, 0]])
              
v = pagerank(M, 100, 0.85)
print(v)