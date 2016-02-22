# return reversed list
def reversed_list(lst):
  reversed_list = []
  for i in xrange(len(lst)-1, 0, -1):
    reversed_list.append(list[i])
  return reversed_list

# test
# self.assertTrue([1,2,3], [3,2,1])
# self.assertTrue([], [])

# modify list to it's reversed version
def reverse_list(lst):
  # iterate over elements by indexes from 0 to half (left half)
  for left in xrange(0, len(lst)/2):
    # right indexes/ it may also be (len(lst)+1-left)
    right =  -1 - left
    # swap elements. create tmp to store left element temporary
    tmp = lst[left]
    lst[left] = lst[right]
    lst[right] = tmp
