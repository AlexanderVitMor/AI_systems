def prime_factorization(number: int) -> dict:
    primes: dict = dict()

    while number > 1:

        for i in range(2, number + 1, 1):
            if number % i == 0:
                number = number // i
                print(number)
                print(i)

                print()
                if i not in primes:
                    primes[i] = 1
                else:
                    primes[i] += 1
                break

    return primes


prime_factorization(100)
