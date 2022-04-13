import random

class Candidate:
  def __init__(self, name):
    self.name = name
    self.date_count = 0
    self.date_required = random.randint(1, 20)

  def asked_for_date(self, subject):
    return random.random() < 0.5

  def fall_in_love(self, subject):
    return self.date_required <= self.date_count


def find_dates(candidates):
  res = []
  for c in candidates:
    if c.asked_for_date("me"):
      res.append(c)
  return res



