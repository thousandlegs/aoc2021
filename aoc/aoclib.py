import os

def project_root():
  return os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

def data_dir():
  return os.path.join(project_root(), 'dat')

def data_fname(base):
  b, ext = os.path.splitext(base)
  if not ext:
    base = b + '.dat'
  return os.path.join(data_dir(), base)

def nwise(iterable, n=2):
  """
  Adapted from more_itertools
  
  s, 2 -> (s0,s1), (s1,s2), (s2, s3), ..." 
  s, 3 -> (s0,s1,2), (s1,s2,s3), (s2,s3,s4), ..."
  """
  from itertools import tee
  parts = tee(iterable, n)
  to_zip = []
  while(parts):
    to_zip.append(parts[0])
    parts = parts[1:]
    for p in parts:
      next(p, None)

  return zip(*to_zip)
