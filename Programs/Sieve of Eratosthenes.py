"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
    for divisor in range(2, bound):
        for stride in range(2 * divisor, bound, divisor):
            if stride in answer:
                answer.remove(stride)
    return answer

print(len(compute_primes(200)))
print(len(compute_primes(2000)))
