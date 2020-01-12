# Get dask results for matrix multiplication:
import dask.array as da
import time


Ns = [5000,10000,15000,20000,25000,30000]
shard_size = (5000,5000)

da.random.seed(42)
print(Ns)

for N in Ns:
    X = da.random.normal(size=(N,N), chunks=shard_size)
    start = time.time()
    XX = X @ X
    XX_np = XX.compute()
    end = time.time()
    print(end - start)