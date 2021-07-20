
plotBME <- function(file) {
   library(dplyr)
   library(ggplot2)
   library(stringr)
   library(ggeasy)

   fileName <- file
   fileName1 <- paste("/outData/ErrorFileDir/", fileName, sep = "")
   fileName1 <- paste(getwd(),fileName1,sep = "")
   fileNamecsv <- paste(fileName1,".csv",sep = "")
   pngName <- paste("BMEAll", fileName, sep = "")
   addpng <- paste(pngName, ".png", sep ="")
   addpng <- paste("/Graphs/",addpng,sep = "")
   addpng <- paste(getwd(),addpng,sep = "")
   png(addpng)
   print(addpng)

incorrectData <- read.csv(fileNamecsv, sep=';')

number_of_lines <- nrow(read.csv(fileNamecsv, sep=';'))

errorWords <-incorrectData %>%
  filter(str_detect(WhereErrorOccurred, "Beginning|Middle|End"))

  BME <- ggplot(errorWords, aes(x=WhereErrorOccurred, fill=Word)) +
    geom_bar(stat="count") +
    scale_y_continuous(breaks=seq(0,number_of_lines,1)) +
    ggtitle(label="Session Feedback") +
    xlab(label="Error Location") +
    ylab(label="# of Words") +
    ggeasy:: easy_center_title() +
    labs(fill="Expected Word")
    theme(legend.position = "none")

print(BME)
dev.off()

}
