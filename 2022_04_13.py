def find_lucky_one(candidates):
  max_date = 10
  for c in candidates:
    while c.asked_for_date("me"):
      c.date_count += 1
      if c.date_count > max_date:
        print("Move on!")
        break
      if c.fall_in_love("me"):
        print("Found the lucky one! {}".format(c.name))
        return c
  return None