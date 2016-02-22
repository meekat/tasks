# Find the most common word in the file and count how often it was met on file.

def get_most_commomn_word_count(file_name):
  handle = open(file_name, 'r')
  words_file = handle.readline()

  words_count = {}
  for word in words_file:
    if word in word_count:
      word_count = words_count[word]
    else:
      word_count = 0
    words_count[word] = word_count + 1
  close(file_name)

# this may be a separate function e.g. get_most_popular_words_from_dict(words_count)
# on that case:
  # return get_most_popular_words_from_dict(words_count)

  most_popular_word = None
  most_popular_word_count = 0
  for word, word_count in words_count.iteritems():
    if most_popular_word_count < word_count:
      most_popular_word_count = word_count
      most_popular_word = word
  return most_popular_word, most_popular_word_count
