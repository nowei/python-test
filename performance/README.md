# Where I test python performance 
Using python timeit, I will test different things in python to better understand how python manages memory.

## variable_assignment 
Is declaring a variable outside a loop and reusing it inside the loop faster than making a new instance of the variable inside the loop?
In ten run averages of running 
inside:
total = 0
for _ in range(1000):
    i = 0
    for _ in range(10):
        i += 1
    total += i

outside:

i = 0
total = 0
for _ in range(1000):
    i = 0
    for _ in range(10):
        i += 1
    total += i
