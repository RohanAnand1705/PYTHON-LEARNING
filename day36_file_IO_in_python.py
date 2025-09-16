#   READING METHOD
# f= open('myfile.txt','rb') # writing 'r' is optional as it is by default in read mode
# text =f.read()
# print(text) 
# f.close()

#         WRITING METHOD
# f= open('myfile2.txt', 'a')
# f.write('Hello, World!')
# f.close()

with open('myfile2.txt', 'a') as f:
    f.write("BYE BYE BYE")