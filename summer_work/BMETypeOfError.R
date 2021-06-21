plotWhereError <- function(sound) {
library(dplyr)
 library(ggplot2)
 library(stringr)

png("specificBMETypeOfError.png")

incorrectData <- read.csv("excelFile2.csv", sep=';')
number_of_lines <- nrow(read.csv("excelFile2.csv", sep=';'))

errorWords <-incorrectData %>%
  filter(str_detect(WhereErrorOccurred, "Beginning|Middle|End"))

  s <- paste("^", sound, sep="")
  Words <- errorWords %>%
    filter(str_detect(Word, s))
  BMETypeOfError <- ggplot(Words, aes(x=WhereErrorOccurred, fill=TypeOfError)) +
    geom_bar(stat="count") +
    scale_y_continuous(breaks=seq(0,number_of_lines,1)) +
    ggtitle(label="Session Feedback") +
    xlab(label="Error Location") +
    ylab(label="# of Words") +
    ggeasy:: easy_center_title() +
    labs(fill="Type of Error")

print(BMETypeOfError)
dev.off()

ggsave("specificBMETypeOfError.png", path = "summer_work/Graphs", scale = 0.15)
}

plotWhereError("r")
