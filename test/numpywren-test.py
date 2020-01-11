# Get numpy results for matrix multiplication:
import numpy as np
import time

N = 10000
shard_size = (5000,5000)
print(f"N = {N}")
print(f"shard_size = {shard_size}")

np.random.seed(42)
X = np.random.randn(N,N)

start = time.time()
XXT_np = X @ X.T
end = time.time()
print("time:")
print(end - start)

#print("Numpy result: ")
#print(XXT_np)


# Test if pywren works:


import pywren

pwex = pywren.lambda_executor()

'''
def f(x): 
    return X @ X.T


futures = pwex.map(f, range(1))

print("Testing pywren:")
start = time.time()
pywren.wait(futures)
end = time.time()
print("time:")
print(end - start)

results = [f.result(throw_except=False) for f in futures]
XXT_pywren = results[0]
'''

#print("Pywren result:")
#print(XXT_pywren)


# Numpywren

from numpywren.matrix import BigMatrix
from numpywren.matrix_init import shard_matrix
from numpywren.binops import gemm

X_sharded = BigMatrix("mulitply_test", shape=X.shape, shard_sizes=shard_size)
shard_matrix(X_sharded, X)

print("Testing numpywren:")
start = time.time()
XXT_sharded = gemm(pwex, X_sharded, X_sharded.T, X_sharded.bucket, 1)
end = time.time()
print("time:")
print(end - start)
#print("Numpywren result ")
#print(XXT_sharded.numpy())
