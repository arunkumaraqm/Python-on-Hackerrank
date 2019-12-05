def arrfloor(arr, number):
    for i in range(len(arr)-1, -1, -1):
        if number >= arr[i]:
            return i
        
def memoize_generate_primes(function):
    memory = []
    prime = function()
    def inner(limit):
        try:
            ind = arrfloor(memory, limit)
            yield from memory[:ind + 1]
            if arrfloor < (len(memory) - 1):
                return
                
        except TypeError:
            pass

        while True:
            new_prime = next(prime)
            memory.append(new_prime)
            if new_prime > limit:
                break
            yield new_prime
    return inner

@memoize_generate_primes
def generate_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

for _ in range(int(input())):
    number = int(input())
    try:
        ans = [i for i in generate_primes(number//2) if number % i == 0][-1]
    except IndexError:
        ans = number
    print(ans)
