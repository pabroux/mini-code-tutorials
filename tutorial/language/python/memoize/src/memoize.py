from functools import cache, lru_cache

@cache  # Memoize function results (unlimited cache, like `lru_cache(maxsize=None)`)
def factorial(n: int) -> int:
    print(f"Computing factorial({n})")  # Shows when an actual computation occurs
    return n * factorial(n - 1) if n else 1

# First call: computes everything (factorial(2), factorial(1) and factorial(0))
factorial(2)

# Second call: reuses memoized results for 0, 1, 2 (cache hit!)
factorial(4) # Only computes factorial(3) and factorial(4)

# Inspect cache performance
print(factorial.cache_info())
# CacheInfo(hits=1, misses=5, maxsize=None, currsize=5)

# Clear the memoized results
factorial.cache_clear()
