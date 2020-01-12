# Get numpy results for matrix multiplication:
import numpy as np
import time


Ns = [5000,10000,15000,20000,25000,30000]
shard_size = (5000,5000)

np.random.seed(42)
print(Ns)

for N in Ns:
    X = np.random.randn(N,N)
    start = time.time()
    XXT_np = X @ X
    end = time.time()
    print(end - start)