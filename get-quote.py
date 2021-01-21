import random

def ok():
 print()

f = open("quotes.txt")
quotes = f.readlines()
f.close()

last = 13
rnd = random.randint(0, 13)
print(quotes[rnd])

if __name__== "__main__":
  ok()
