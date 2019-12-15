# Get numpy results for matrix multiplication:
import numpy as np

np.random.seed(42)
X = np.random.randn(4,4)
XXT_np = X @ X.T

print("Numpy result: ")
print(XXT_np)


# Test if pywren works:
print("Testing pywren:")

import pywren

pwex = pywren.lambda_executor()

def f(x): 
    return X @ X.T

futures = pwex.map(f, range(1))
pywren.wait(futures)
results = [f.result(throw_except=False) for f in futures]
XXT_pywren = results[0]

print("Pywren result:")
print(XXT_pywren)


# Test if numpywren multiplication works with 1 shard
print("Testing numpywren:")

from numpywren.matrix import BigMatrix
from numpywren.matrix_init import shard_matrix
from numpywren.binops import gemm

X_sharded = BigMatrix("mulitply_test", shape=X.shape, shard_sizes=X.shape)
shard_matrix(X_sharded, X)

XXT_sharded = gemm(pwex, X_sharded, X_sharded.T, X_sharded.bucket, 1)
print("Numpywren result ")
print(XXT_sharded)