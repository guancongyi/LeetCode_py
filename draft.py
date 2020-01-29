import functools

l = [1,2,3,5]
def add(x,y): return x+y
def sqr(x): return x**2

list1 = map(lambda x: x ** 2, l)
print(list1)
# z = map(sqr,l)
z = functools.reduce(lambda x, y: x + y, l)

# z=functools.reduce(add, l)
print(z)
