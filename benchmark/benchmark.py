from timeit import timeit as t

'''
                    Benchmarking snippets for perfomance
'''


l = list(range(10,1000))

t1 = t(
    '''[x ** 2 for x in list(range(10,1000  ))]''',
    number=100,
)

print(t1)