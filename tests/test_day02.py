sample_input = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

from aoc import day02

def test_day02():
  final = day02.move((0, 0), sample_input)
  assert(tuple(final) == (15, 10))
  assert(day02.metric(final) == 150)
