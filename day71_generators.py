def generator1():
    for i in range(50000):
        yield i
        generator1()

gen = generator1()

for j in gen:
    print(j)

#generator generates value instantly not stores it beforehand
