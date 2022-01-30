# seed(x)	Generates the same sequence of random numbers every time you call seed(x).
import random
# seed value = 7
random.seed(7)
for i in range(7):
    print(random.random(), end = ' ')

print('\n')

# seed value = 8
random.seed(8)
for i in range(3):
    print(random.random(), end = ' ')

print('\n')

# seed value again = 9
random.seed(9)
for i in range(9):
    print(random.random(), end = ' ')

print('\n')
