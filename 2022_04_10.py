import random
loved = False
# assuming that love is random
def find_love():
  return random.random() < 0.01
def main():
  while not loved:
    loved = find_love()
  print("you are loved")


