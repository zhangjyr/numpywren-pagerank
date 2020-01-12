import numpy as np

# params
N = 4
shard_size = (4,4)
# print(f"N = {N}")
# print(f"shard_size = {shard_size}")

np.random.seed(42)
X = np.random.randn(N,N)


# numpy:
print("Running numpy version...")
XX_np = X @ X


# pywren:
print("Running pywren version...")

import pywren

def f(x): 
    return X @ X

pwex = pywren.lambda_executor()

futures = pwex.map(f, range(1))
pywren.wait(futures)
results = [f.result(throw_except=False) for f in futures]
XX_pywren = results[0]


# numpywren:
print("Running numpywren version...")

from numpywren.matrix import BigMatrix
from numpywren.matrix_init import shard_matrix
from numpywren.binops import gemm

X_sharded = BigMatrix("mulitply_test", shape=X.shape, shard_sizes=shard_size)
shard_matrix(X_sharded, X)
XX_sharded = gemm(pwex, X_sharded, X_sharded, X_sharded.bucket, 1)
XX_numpywren = XX_sharded.numpy()

print("Numpy result: ")
print(XX_np)

print("Pywren result:")
print(XX_pywren)

print("Numpywren result ")
print(XX_numpywren)
