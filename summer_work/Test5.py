import random
import rpy2.robjects as ro


numberOfWords = 1
path = ""

def main():
    print("In main")
    a = function1(1, 2, "RightWrongUnheard")
    print(a)
    print("done")

def function1(input, output, filename):
    print("In function1", input, output)
    p = 0
    r = ro.r
    print(path+"r_To_Python.R")
    # r.source(path + "r_To_Python.R")
    print(path + "PieChart.R")
    r.source(path + "PieChart.R")
    print("In function1 calling % of sessions")
   #p = r.percent_Of_Sessions(input, output, filename)
    return p


if __name__ == "__main__":
    main()