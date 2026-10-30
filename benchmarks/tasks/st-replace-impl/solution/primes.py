def primes_upto(n):
    if n < 2:
        return []
    sieve = bytearray([1]) * (n + 1)
    sieve[:2] = b"\0\0"
    for k in range(2, int(n ** 0.5) + 1):
        if sieve[k]:
            sieve[k * k::k] = bytes(len(range(k * k, n + 1, k)))
    return [k for k, is_prime in enumerate(sieve) if is_prime]


def count_primes(n):
    return len(primes_upto(n))
