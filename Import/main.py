import functions
from functions import Add
import random
A = random.randint(1,20)
B = random.randint(30,80)

X = functions.multiply(A,B)
Y = Add(A,B)

print(X + Y)