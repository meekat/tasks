import math

def prime_num_up_to(n):
  """Returns list of prime numbers up to n."""

  list_of_primes = []

  for i in xrange(1, n + 1):
    i_is_prime = True

    for e in xrange(4, math.sqrt(i) + 1):
      if i % e == 0:
        i_is_prime = False

    if i_is_prime:
      list_of_primes.append(i)

  return list_of_primes

# test
# self.assertEqual(prime_num_up_to(5), [1, 2, 3, 5]
# self.assertEqual(prime_num_up_to(9), [1, 2, 3, 5, 7]
# self.assertEqual(prime_num_up_to(0), []
# self.assertEqual(prime_num_up_to(1), [1]
