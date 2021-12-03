import numpy

from . import aoclib

def read_data():
  # Kind of want to just make a generator
  with open(aoclib.data_fname('day02')) as f:
    return f.read()
  
# 'x' is forward and back
# 'd' is depth, increasing downward
def make_coords(x=0, d=0):
  return numpy.array((x, d), dtype=int)

direction = {
  'forward': make_coords(x=1),
  'down':    make_coords(d=1),
  'up':      make_coords(d=-1),

}

def parse_instruction(s):
  """
  Given one of the movement instructions, return a coords tuple
  describing the delta.
  """
  # Could use numpy to simplify the math but I think I like named directions too much
  s = s.strip()
  if not s:
    return (0, 0)
  dir, dist = s.split()
  dist = int(dist)

  unit = direction[dir]
  return unit * dist


def move(start, instructions):
  """
  From coordinates <start>, follow directions in multi-line string
  <instructions>. Return the final coordinates.
  """
  from functools import reduce
  start = numpy.array(start)
  return reduce(numpy.add, 
                [parse_instruction(s) for s in instructions.splitlines()], 
                start)

def metric(coords):
  return numpy.multiply.reduce(coords)


def run():
  program = read_data()
  final = move((0,0), program)
  print('final location:', final)
  print('metric:', metric(final))

if __name__ == '__main__':
  run()
