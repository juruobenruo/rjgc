import taichi as ti
import time 
ti.init(arch=ti.gpu)

#@ti.func

def is_prime(n: int):
    result = True
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            result = False
            break
    return result

#@ti.kernel
def count_primes(n: int,a:str) -> int:
    count = 0
    for k in range(2, n):
        if is_prime(k):
            count += 1

    return count
start = time.clock()
print(count_primes(10000000))
end = time.clock()

print(end-start)