a=6753
b=796
print("A") if a>b else print("=") if a==b else print("B") 
#can't use elif in middle, doesn't support
c=89 if a>b else 0
print(c)