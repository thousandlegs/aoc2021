from . import aoclib


def read_data():
  # Kind of want to just make a generator
  return(map(int, open(aoclib.data_fname('day01'))))

def sum_subtuples(seq, tlen):
  """
  First transform <seq> into sliding windows,
  then sum each of those
  """
  return map(sum, aoclib.nwise(seq, tlen))

def count_increasing(seq):
  from more_itertools import pairwise, quantify
  inc = lambda t: t[1] > t[0]
  return quantify(pairwise(seq), inc)

def part1():
  print(count_increasing(read_data()))

def part2():
  sts = sum_subtuples(read_data(), 3)
  print(count_increasing(sts))
