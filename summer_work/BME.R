
plotBME <- function(file) {
   library(dplyr)
   library(ggplot2)
   library(stringr)
   library(ggeasy)

   fileName <- file
   fileName2 <- paste("summer_work/", fileName, sep ="")
   fileNamecsv <- paste(fileName2, ".csv", sep ="")
   pngName <- paste("BME", fileName, sep = "")
   addpng <- paste(pngName, ".png", sep ="")

   png(addpng)

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

print(BME)
dev.off()

ggsave(addpng, path = "summer_work", scale = .5)
}

plotBME("ErrorFile2")