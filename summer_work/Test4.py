import random
import rpy2.robjects as ro
import os
import matplotlib.pyplot as plt
numberOfWords = 5
# path = "/Users/zachg/PycharmProjects/BryanResearchProgram/Rough Stuff/"
path = ""

def main():
    inFile = open("animaltext","r")
    # inFile = open("word.txt","r")
    wordList = []
    wrongWordSet = []
    rightWordSet = []
    nothingWordSet = []

    for line in inFile:
        wordList.append(line.strip("\n"))
    inFile.close()

    for count in range(numberOfWords):
        output1 = wordList[random.randrange(len(wordList))]
        # output1 = "meat"
        print("Your word is " + output1)
        input1 = input("Type the word: ")

        if input1 == output1:
            print("Congrats!")
            rightWordSet.append(input1)

        elif input1 == "":
            print("Please try again")
            nothingWordSet.append(output1)

        else:
            print("Sorry")
            wrongWordSet.append(output1)

    # print("rightWordSet = " , rightWordSet)
    # print("wrongWordSet = " , wrongWordSet)
    # print("nothingWordSet = " , nothingWordSet)

    percentageOfRight = (len(rightWordSet)/(len(rightWordSet) + len(wrongWordSet) + len(nothingWordSet)))
    percentageOfWrong = (len(wrongWordSet)/(len(rightWordSet) + len(wrongWordSet) + len(nothingWordSet)))
    percentageOfNothing = (len(nothingWordSet)/(len(rightWordSet) + len(wrongWordSet) + len(nothingWordSet)))

    # print("percentageOfRight = " , percentageOfRight)
    # print("percentageOfWrong = " , percentageOfWrong)
    # print("percentageOfNothing = " , percentageOfNothing)



    # if len(input1) == len(output1):
    #     input2 = list(input1)
    #     output2 = list(output1)
    #     count = 0
    #     for number in output1:
    #         if input2[count] == output2[count]:
    #             count += 1
    #             print("You have the same letter")
    #         else:
    #             count += 1
    #             print("Keep trying")
    #             # print("You added an unnecessary " + input2[count])

    # if len(input1) > len(output1):





        # print(input2)
        # print(output2)

    # elif len(input1) > len(output1):
    #
    #
    # elif len(input1) < len(output1):


    # else:
    #     print("Wrong word!")






    # outFile1 = open("rightWords.txt", "a")
    # for line in rightWordSet:
    #     outFile1.write(line + "\n")
    # outFile1.close()
    #
    # outFile2 = open("wrongWords.txt", "a")
    # for line in wrongWordSet:
    #     outFile2.write(line + "\n")
    # outFile2.close()
    #
    # fileHandle = open("fileForExcel.csv", "a")
    # rightFile = open("rightWords.txt", "r")
    # wrongFile = open("wrongWords.txt", "r")
    #
    # rightWordSet = rightFile.read().split("\n")
    # wrongWordSet = wrongFile.read().split("\n")
    #
    # rightFile.close()
    # wrongFile.close()

    # print(rightWordSet)
    #
    # #for index in range(len(rightWordSet)):
    # #    fileHandle.write(rightWordSet[index])
    # #    if index < len(wrongWordSet):
    # #        fileHandle.write(",")
    # #        fileHandle.write(wrongWordSet[index])
    # #    fileHandle.write("\n")
    # #fileHandle.close()

    # for number in range(1):
    #     fileHandle.write(str(percentageOfRight))
    #     fileHandle.write(",")
    #     fileHandle.write(str(percentageOfWrong))
    #     fileHandle.write(",")
    #     fileHandle.write(str(percentageOfNothing))
    #     fileHandle.write("\n")
    # fileHandle.close()

    a = function1(1, 15, "RightWrongUnheard")
    print(a)

def function1(input, output, filename):
    p = 0
    r = ro.r
    # print(path+"r_To_Python.R")
    # r.source(path + "r_To_Python.R")
    print(path + "PieChart.R")
    r.source(path + "PieChart.R")
    p = r.percent_Of_Sessions(input, output, filename)
    return p

# a = function1(1, 3)
# print(a)

#https://www.codegrepper.com/code-examples/python/python+save+pie+chart

# project_Root_Dir = "."
# chapter_ID = "classification"
# images_Path = os.path.join(project_Root_Dir,  "images", chapter_ID)
# os.makedirs(images_Path, exist_ok = True)
#
# def save_fig(fig_id, tight_layout = True, fig_extension = "png", resolution = 300):
#     path = os.path.join(images_Path, fig_id + "." + fig_extension)
#     print("Saving figure", fig_id)
#     if tight_layout:
#         plt.tight_layout()
#     plt.savefig(path, format = fig_extension, dpi = resolution)



# def add_row_num(filename):
#     file = open(filename,"r")
#     rows = file.read().split("\n")
#     file.close()
#     # print(rows)
#     file = open(filename,"w")
#     count = 1
#     for index in range(0, len(rows)):
#         # print(len(rows[index]))
#         # print(len(rows))
#         if index == 0:
#             file.write(rows[index] + "\n")
#         elif len(rows[index]) > 0:
#             file.write(str(count)+","+rows[index]+"\n")
#             count += 1
#         elif len(rows[index]) == 0:
#             file.write(str(count) + ",")
#             count += 1
#     file.close()

#add_row_num("fileForExcel.csv")
main()
