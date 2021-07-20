
plotBME <- function(sound, file) {
  library(dplyr)
  library(ggplot2)
  library(stringr)
  library(ggeasy)

   fileName <- file
   fileName1 <- paste("~/../outData/ErrorFileDir/", fileName, sep = "")
   fileNamecsv <- paste(fileName1, ".csv", sep ="")
   pngName <- paste("BMESpecific", fileName, sep = "")
   addpng <- paste(pngName, ".png", sep ="")
   addpng <- paste("~/../Graphs/",addpng,sep = "")
   png(addpng)

incorrectData <- read.csv(fileNamecsv, sep=';')
number_of_lines <- nrow(read.csv(fileNamecsv, sep=';'))

errorWords <-incorrectData %>%
  filter(str_detect(WhereErrorOccurred, "Beginning|Middle|End"))

  s <- paste("^", sound, sep="")
  Words <- errorWords %>%
    filter(str_detect(Word, s))
  BME <- ggplot(Words, aes(x=WhereErrorOccurred, fill=Word)) +
    geom_bar(stat="count") +
    scale_y_continuous(breaks=seq(0,number_of_lines,1)) +
    ggtitle(label="Session Feedback") +
    xlab(label="Error Location") +
    ylab(label="# of Words") +
    ggeasy:: easy_center_title() +
    labs(fill="Expected Word")

print(BME)
dev.off()

ggsave(addpng, path = "../Graphs", scale = 1)
}
