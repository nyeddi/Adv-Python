def hyperVolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v

print(hyperVolume(1, 2, 3, 4, 5))

def func():
    def local_func():
        a = 'hello, '
        b = 'world'
        return a + b
    x = 1
    y = 2
    return local_func() #x + y

print(func())

def outer(x):
    def inner(y):
        return x+y
    return inner

add10 = outer(10)
print(add10(5))
print(add10.__closure__)



