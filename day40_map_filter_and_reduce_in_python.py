# cube= lambda x: x*x*x

# l=[3,4,5,6,7]
# # newl=[]
# # for object in l:
# #     newl.append(cube(object))
# # print(newl)

# newl = list(map(cube,l))
# print(newl)

# filter_function= lambda x: x>4
# newnewl=list(filter(filter_function,l))
# print(newnewl) 

from functools import reduce
numbers=[1,2,3,4,5]

sum= reduce(lambda x,y: x+y,numbers)
print(sum)