#!/usr/bin/python

import urllib

# Might be better to use some open source thing
# path is defined starting after the /1
def parse(path):
  # TODO: prob doesn't work at all because no keys. Annoying
  response = urllib.urlopen("https://api.parse.com/1/" + path)
