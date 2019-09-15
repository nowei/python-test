import timeit

number = 100000
inside_code = """total = 0
for _ in range(1000):
    i = 0
    for _ in range(10):
        i += 1
    total += i
"""
outside_code = """i = 0
total = 0
for _ in range(1000):
    i = 0
    for _ in range(10):
        i += 1
    total += i
"""

def without_gc():
    print('without garbage collection')
    inside = timeit.timeit(inside_code, number=number)
    print("declared inside ({} loops): {}".format(number, inside))
    outside = timeit.timeit(outside_code, number=number)
    print("declared outside ({} loops): {}".format(number, outside))

def with_gc():
    print('with garbage collection')
    inside = timeit.timeit(inside_code, 'gc.enable()', number=number)
    print("declared inside ({} loops): {}".format(number, inside))
    outside = timeit.timeit(outside_code, 'gc.enable()', number=number)
    print("declared outside ({} loops): {}".format(number, outside))

def main():
    # print("inside:\n",inside_code)
    # print("outside:\n",outside_code)
    with_gc()
    without_gc()


if __name__ == '__main__':
    main()