import random
INT_MAX = 2147483647
# assume date success rate is 50%
def go_to_date():
  return random.random() < 0.5
def find_love():
  required = random.randint(1, INT_MAX)
  count = 0
  while go_to_date() and count < required:
    count += 1
  if count >= required:
    print("You found love!")
  else:
    print("You didn't find love.")
  return count >= required


