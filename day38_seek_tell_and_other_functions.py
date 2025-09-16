# with open('myfile.txt','r') as f:
#     print(type(f))

#     f.seek(10) # Move the cursor to the 10th byte
#     print(f.tell()) # Get the current cursor position
#     data=f.read(4) # Read 4 bytes from the current cursor position
#     print(data)

with open('sample.txt','w') as f:
    f.write("Hello World!")
    f.truncate(5) # Truncate the file to 5 bytes
    
with open('sample.txt','r') as f:
    print(f.read()) 