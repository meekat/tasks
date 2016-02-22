#!/usr/bin/env python
# Find Second Least common element from an Integer array.

def get_second_least_common_element(lst):
  # create empty dictionary.
  count = {}
  # get element:count pairs and store it on count dictionary.
  for e in lst:
    if e in count:
      element_count = count[e]
    else:
      element_count = 0
    count[e] = element_count + 1

  # find least popular element:count pair
  least_popular_item = None
  least_popular_item_count = float("inf")
  for e, element_count in count.iteritems():
    if least_popular_item_count > element_count:
      least_popular_item_count = element_count
      least_popular_item = e
      # remove least popular pair from dictionary
  count.pop(least_popular_item)

  # find least popular element:count pair on remaining dict
  # it will be 2nd least popular item in initial dict/ whole list
  second_least_item = None
  second_least_item_count = float("inf")
  for e, element_count in count.iteritems():
    if second_least_item_count > element_count:
      second_least_item_count = element_count
      second_least_item = e

  # uncomment following line to test
  print count, second_least_item, second_least_item_count
  return second_least_item

# to test: uncomment following line
get_second_least_common_element([4, 3, 4, 4, 4, 8, 7, 7, 8, 8])