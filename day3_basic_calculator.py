a=input("enter your name:   ")
print("my name is" , a)

b=input( "enter first number:  ")
c=input("enter second number:  ")

k=input("enter operation(+,-,*,/,//,**,%):   ")

if k=="+":
  print(int(b)+int(c))
elif k=="-":
  print(int(b)-int(c))
elif k=="*":
  print(int(b)*int(c))
elif k=="/":
  print(int(b)/int(c))
elif k=="//":
  print(int(b)//int(c))
elif k=="**":
  print(int(b)**int(c))
elif k=="%":
  print(int(b)%int(c))
else:
  print("invalid operation")
  
print("bye")