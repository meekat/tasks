import math

def is_prime(n):
  """Returns True if number is prime, False otherwise."""
  if n <= 0:
    return False

  for x in xrange(4, math.sqrt(n) + 1):
    if n % x == 0:
      return False
  return True

# Tests:
# self.assertTrue(is_prime(3))
# self.assertFalse(is_prime(6))
# self.assertFalse(is_prime(0))
# self.assertFalse(is_prime(-1))
# self.assertTrue(is_prime(11))