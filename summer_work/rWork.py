import rpy2.robjects as r1

path = ""
print(path)

def function1(input, output):
    p = 0
    r = r1.r
    print(path+".R")
    r.source(path + "addNum.R")
    p = r.addnumbers(input, output)
    return p


a = function1(12, 10)  # calling the function with passing arguments
print(a)