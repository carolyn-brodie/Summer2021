import csv
TYPE_OF_ERROR = 4
EXPECTED_LETTER_ERROR = 6
SAID_LETTER_ERROR = 7
emptyList = []


with open('./outData/ErrorFile1.csv', newline='') as csvfile:
    csvfile2 = open('./outData/ErrorFile2.csv', newline='')
    file_contents1 = csv.reader(csvfile, delimiter=';', quotechar='|')
    file_contents2 = csv.reader(csvfile2, delimiter=';', quotechar='|')
    for row in file_contents1:
        #test if substitution
        if row[TYPE_OF_ERROR] == "Substitution":
            # print(row)
            emptyList.append(row[EXPECTED_LETTER_ERROR] + row[SAID_LETTER_ERROR])
    for row in file_contents2:
        if row[TYPE_OF_ERROR] == "Substitution":
            # print(row)
            if row[EXPECTED_LETTER_ERROR] + row[SAID_LETTER_ERROR] in emptyList:
                print(row[0] + row[EXPECTED_LETTER_ERROR] + row[SAID_LETTER_ERROR])