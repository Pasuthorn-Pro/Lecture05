def generate_primes(num):
    if num <= 1:
        return []

    primes = [2]
    for n in range(3, num + 1, 2):
        is_prime = True
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)

    return primes

print(generate_primes(32))
