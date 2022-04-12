import random

class Candidate:
  def __init__(self, name):
    self.name = name
    self.date_count = 0

  def asked_for_date(self, subject):
    return random.random() < 0.5

def find_dates(candidates):
  res = []
  for c in candidates:
    if c.asked_for_date("me"):
      res.append(c)
  return res



