import numpy

from . import aoclib

# 'x' is forward and back
# 'd' is depth, increasing downward
class SubPosition:
  def __init__(self, x=0, d=0, aim=0):
    self.aim = aim
    self.x = x
    self.d = d

  def forward(self, dist):
    self.x += dist
    self.d += dist * self.aim
  
  def up(self, a):
    self.down(-a)

  def down(self, a):
    self.aim += a

  def coords(self):
    return (self.x, self.d)

  def metric(self):
    return self.x * self.d

  def __str__(self):
    return f"""\
Position: x={self.x} d={self.d}
Metric: {self.metric()}\
"""

def read_data():
  # Kind of want to just make a generator
  with open(aoclib.data_fname('day02')) as f:
    return f.read()
  

commands = {
  'forward': SubPosition.forward,
  'down':    SubPosition.down,
  'up':      SubPosition.up,
}

def parse_instruction(s, pos):
  """
  Given one of the movement instructions, return a coords tuple
  describing the delta.
  """
  # Could use numpy to simplify the math but I think I like named directions too much
  s = s.strip()
  if not s:
    return
  mv, amt = s.split()
  amt = int(amt)
  mv = commands[mv]
  mv(pos, amt)


def move(pos, instructions):
  """
  From SubPosition <pos>, follow directions in multi-line string
  <instructions>. <pos> is modified to represent the final coordinates.
  """
  for s in instructions.splitlines():
    parse_instruction(s, pos)


def run():
  program = read_data()
  pos = SubPosition()
  move(pos, program)
  print(pos)
