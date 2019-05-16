import timeit

print '0-1-2-3-....-9'
print timeit.timeit(' "-".join(str(n) for n in range(100))',number=10000)
print timeit.timeit(' "-".join(map(str, range(100))',number=10000)
print %timeit "-".join(str(n) for n in range(100))
