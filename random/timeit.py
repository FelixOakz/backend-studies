import timeit

start_time = timeit.default_timer()
print('meow\n' * 3, end='')
print('print time equals: ', timeit.default_timer() - start_time)

start_time = timeit.default_timer()
for _ in range(3):
    print('meow')
print('for time equals: ', timeit.default_timer() - start_time)

start_time = timeit.default_timer()
i = 1
while i <=3:
    print('meow')
    i += 1
print('while time equals: ', timeit.default_timer() - start_time)
