file1 <- read.csv("/Users/zachg/Desktop/ErrorFile5.csv", sep = ";")
file2 <- read.csv("/Users/zachg/Desktop/ErrorFile6.csv", sep = ";")
# file1
# file2

newFile1 <- subset(file1, TypeOfError == "Substitution")
newFile2 <- subset(file2, TypeOfError == "Substitution")
# newFile1
# newFile2

newFile1$Concatenated <- paste(newFile1$ExpectedLetterError, newFile1$SaidLetterError)
newFile2$Concatenated <- paste(newFile2$ExpectedLetterError, newFile2$SaidLetterError)
# newFile1
# newFile2

concat1 <- newFile1[,"Concatenated"]
concat2 <- newFile2[,"Concatenated"]
# concat1
# concat2

a1 <- c("['e'] ['u']", "['d'] ['s']", "['e'] ['o']", "['i'] ['f']",
        "['i'] ['u']", "['i'] ['e']", "['l'] ['v']", "['i'] ['u']")
b1 <- c("['u'] ['o']", "['e'] ['o']", "['d'] ['z']", "['e'] ['u']",
        "['i'] ['y']", "['i'] ['u']", "['i'] ['e']", "['l'] ['y']",
        "['i'] ['u']")

out1 <- intersect(a1, b1)
out1

out2 <- intersect(concat1, concat2)
out2


