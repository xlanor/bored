
#!/usr/bin/env python 

"""
Reverse words in place in a given string

In a sentence, while preserving spaces, reverse each individual word in place.
"""

def reverse_in_place(current_word: list, start, end):
  if start >= end:
    return current_word
  current_word[start], current_word[end] = current_word[end], current_word[start]
  return reverse_in_place(current_word,start+1,end-1)



def reverse_words_in_sentence(sentence: str):
  # Split into individual words
  sentence_of_words = sentence.split(" ")
  # Convert to lists
  sentence_of_words = [list(word) for word in sentence_of_words]
  sentence_of_words = ["".join(reverse_in_place(cur, 0, len(cur)-1)) for cur in sentence_of_words]
  return " ".join(sentence_of_words)

if __name__ == "__main__":
  rs = reverse_words_in_sentence(" this is.  a  test. ")
  assert rs == " siht .si  a  .tset "

