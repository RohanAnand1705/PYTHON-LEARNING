s1={2,3,4,5,6}
s2={9,8,7,6,5}
# print(s1.union(s2))
# print(s1,s2)
# (s1.update(s2))
# print(s1)
# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1)
s3={3,4}
p=s1.symmetric_difference(s2)
print(p)
k=s1.difference(s2)
print(k)
print(s1.isdisjoint(s2))
print(s1.issuperset(s3))
print(s3.issubset(s1))
s3.remove(4)
print(s3)
#when we try to remove item not present in se , remove raises error but discard doesn't
t=s1.pop()
print(t)
s1.clear
print(s1)

#if   in   can also be used in set