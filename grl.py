#!/usr/bin/python

# Grl is the world's simplest programming language.
# (Is it even a real programming language? Let's claim it is and let
# people debate about it.)

# It is designed to control robots.

# G = go
# R = right
# L = left

# That's all! Any other character is a no-op.

# Since it is really simple this might be the best way to start
# teaching kids programming.
# If I had a real robot hooked up to this, I would just start playing
# with it by myself and kids would be curious what I was doing.

# Once you get the hang of basic grl, you might find yourself wanting
# more features. A more-powerful Grl2 would be neat.
# The interpreter is pretty simple. I wonder how old you would have to
# be to make changes to it.

# TODO: make this actually work with robots
# TODO: this has nothing to do with Parse but is under the Parse
# directory. I should fix that

# NOTE: this is named "Grl" so one might be under the impression that
# it is only for girls. Not true! We must be careful to let our
# children know that programming is not just for girls - boys are
# allowed to be programmers too.

import sys

"Parse a line of Grl code into a list of commands."
def grl(code):
  out = []
  for letter in code.upper():
    if letter == "G":
      out.append("Go!")
    if letter == "R":
      out.append("Right!")
    if letter == "L":
      out.append("Left!")
  return out

if __name__ == "__main__":
  # Run a REPL
  while True:
    code = sys.stdin.readline()
    for command in grl(code):
      print command
