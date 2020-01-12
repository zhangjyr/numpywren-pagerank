# Get numpywren results for matrix multiplication:
import numpy as np
import time
from numpywren.matrix import BigMatrix
from numpywren.matrix_init import shard_matrix
from numpywren.binops import gemm
import pywren
pwex = pywren.lambda_executor()

Ns = [5000,10000,15000,20000,25000,30000]
shard_size = (5000,5000)

np.random.seed(42)


# Only run this if matrices not already in the bucket.
# This takes a very long time (for 30000x30000xf64 - 8GB of data)
# Big_X = BigMatrix("multiply_test2", shape=(max(Ns),max(Ns), shard_sizes=shard_size)
# for i in range():
#     for j in range():
#         X = np.random.randn(5000,5000)
#         Big_X.put_block(X, i, j)

# start = time.time()
# gemm(pwex, Big_X, Big_X, Big_X.bucket, 1)
# end = time.time()
# print(end - start)

for N in Ns:
    X_sharded = BigMatrix("multiply_test2", shape=(N,N), shard_sizes=shard_size)
    start = time.time()
    gemm(pwex, X_sharded, X_sharded, X_sharded.bucket, 1)
    end = time.time()
    print(end - start)