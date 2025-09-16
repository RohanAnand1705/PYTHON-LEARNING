# f= open('myfile25.txt','r')
# i=0
# while True:
#     i=i+1
#     line = f.readline()
#     if not line:
#         break
#     m1= line.split(",")[0]
#     m2= line.split(",")[1]
#     m3= line.split(",")[2]
#     print(f"marks of student {i}in maths is: {m1}")
#     print(f"marks of student {i}in science is: {m2}")
#     print(f"marks of student {i}in sst is: {m3}")
#     print(line)

f= open('myfile25.txt','w')
lines= ['this is line 1\n','this is line 2\n','this is line 3\n']
f.writelines(lines)
f.close()