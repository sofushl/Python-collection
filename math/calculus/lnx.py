from math import log as ln
from math import exp as e

def f(x):
  return e(x)

dx = float(0.001)

for i in range(1, 11, 1):
    print("f'(" + str(i) + ") er tilnærmet lik", round((f(i + dx)-f(i - dx))/(2*dx), 6))



# Write your code here :-)
