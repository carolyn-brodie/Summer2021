
plotBar <- function(file) {
   library(dplyr)
   library(ggplot2)
   library(stringr)
   library(ggeasy)

   fileName <- file
   fileName2 <- paste("/outData/ErrorFileDir/", fileName, sep ="")
   fileName1 <- paste(getwd(),fileName2,sep = "")
   fileNamecsv <- paste(fileName1, ".csv", sep ="")
   pngName <- paste("TypeOfErrorWCorrect", fileName, sep = "")
   addpng <- paste(pngName, ".png", sep ="")
   addpng <- paste("/Graphs/",addpng,sep = "")
   addpng <- paste(getwd(),addpng,sep = "")
   theme(legend.position = "none")
   png(addpng)

number_of_lines <- nrow(read.csv(fileNamecsv, sep=';'))
words <- read.csv(fileNamecsv, sep = ';')
# errorWords <-incorrectData %>%
#   filter(str_detect(WhereErrorOccurred))

  Bar <- ggplot(words, aes(x=TypeOfError, fill=Word)) +
    geom_bar(stat="count") +
    scale_y_continuous(breaks=seq(0,number_of_lines,1)) +
    ggtitle(label="Session Feedback") +
    xlab(label="Type of Error") +
    ylab(label="# of Words") +
    ggeasy:: easy_center_title() +
    labs(fill="Expected Word")

print(Bar)
dev.off()

}
