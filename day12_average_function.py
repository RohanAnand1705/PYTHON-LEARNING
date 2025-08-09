# def average(a=13,b=21):
#     print("The average is", (a+b)/2)
# # average(12,23)
# # average(12,13)
# # average(12, )
# # average(  ,23)  can't writenothing before comma, for default value of a need to specify as below
# average(b=45)

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    # print("average is",sum/len(numbers))
    # return sum/len(numbers)
# average(2,3,4)
# average(2)
# average(2,3)
c= average(2,3,4,6,7,9)
print(c)
