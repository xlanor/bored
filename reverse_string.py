#!/usr/bin/env python 

def reverse(input: str)-> str:
  split = input.split(" ")
  split.reverse()
  print(*split, sep = ",")
  return " ".join(split)


if __name__ == "__main__":
  reversed = reverse(" this is  a test ")
  assert reversed == " test a  is this "
