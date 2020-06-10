#!/usr/bin/env python 

"""
Reverse words in a given string
Example: Let the input string be “i like this program very much”. The function should change the string to “much very program this like i”

- Should handle spacing even at the start & end
"""

def reverse(input: str)-> str:
  split = input.split(" ")
  split.reverse()
  print(*split, sep = ",")
  return " ".join(split)


if __name__ == "__main__":
  reversed = reverse(" this is  a test ")
  assert reversed == " test a  is this "
