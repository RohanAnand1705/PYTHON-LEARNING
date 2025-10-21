import functools
import time
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n**2

print(fx(2))
print(fx(20))
print(fx(5))
print(fx(9))
print(fx(2))        
print(fx(20))
print(fx(5))
print(fx(7))

'''
for repeated values itr prints instantly vause stored in cache
'''