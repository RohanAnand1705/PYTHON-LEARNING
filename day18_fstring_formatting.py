line=("go to {1} you'll find {0}")
p="patna"
f="food"
# print(line.format(p,f))
print(f"go to {p} you'll find {f}")    #can't add numbers in this
price1=49.28393793483993890339
k=("for only{price:.2f} rupees")
g=(f"for only{price1:.5f} rupees")
print(k.format(price=34.1234))
print(g)
print(f"{32*2}")
print(type(f"{32*2}"))
print(f"{{32*2}}")  # for printing the object add one more bracket