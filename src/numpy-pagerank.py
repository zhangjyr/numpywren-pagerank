import numpy as np

np.random.seed(42)

def pagerank(M, iters = 100, d = 0.85):
 
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    M_hat = (d * M + (1 - d) / N)
    start = time.process_time()
    for i in range(iters):
        v = M_hat @ v
    end = time.process_time()
    return v


M = np.array([[0, 0, 0, 0, 1],
              [0.5, 0, 0, 0, 0],
              [0.5, 0, 0, 0, 0],
              [0, 1, 0.5, 0, 0],
              [0, 0, 0.5, 1, 0]])

v = pagerank(M, 10, 0.85)

print(v)
