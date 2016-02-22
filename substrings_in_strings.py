def find_subst_in_str(a_str, sub):
  start = 0
  while True:
    start = a_str.find(sub, start)
    if start == -1: return
    yield start
    start += len(sub) # use start +=1 to find overlapping matches

# list(find_subst_in_str('spam spam spam spam', 'spam')) # [0, 5, 10, 15]