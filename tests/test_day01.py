def test_day01():
  from aoc.day01 import run
  
  # Enter code here
  input = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
  ]
  expected_count = 7

  actual_count = run(input)
  assert(actual_count == expected_count)
