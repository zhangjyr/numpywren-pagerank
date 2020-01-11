import numpy as np
import networkx as nx
import random
import time
np.random.seed(42)
random.seed(42)

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


# experiment parameters

N = 10000
iters = 25



# prepare pagerank matrix

print("constructing pagerank matrix...")
# use nx to create representation of a web graph
d = 0.85
G = nx.scale_free_graph(N, alpha=0.41, beta=0.49, gamma=0.1, delta_in=0)
M = nx.google_matrix(G, alpha=1).T

start = time.process_time()
v = pagerank(M, 25, 0.85)
end = time.process_time()
print("numpy:")
print(end - start)
print(v[1],v[2], v[3])