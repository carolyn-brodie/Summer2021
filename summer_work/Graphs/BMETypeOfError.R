 library(dplyr)
 library(ggplot2)
 library(stringr)
print(read.csv("ErrorFile.csv", sep=';'))
#print(errorWords)

incorrectData <- read.csv("ErrorFile.csv", sep=';')
number_of_lines <- nrow(read.csv("ErrorFile.csv", sep=';'))

errorWords <-incorrectData %>%
  filter(str_detect(WhereErrorOccurred, "Beginning|Middle|End"))

plotWhereError <- function(sound) {
  s <- paste("^", sound, sep="")
  Words <- errorWords %>%
    filter(str_detect(EWord, s))
  ggplot(Words, aes(x=WhereErrorOccurred, fill=TypeOfError)) +
    geom_bar(stat="count") +
    scale_y_continuous(breaks=seq(0,number_of_lines,1)) +
    ggtitle(label="Session Feedback") +
    xlab(label="Error Location") +
    ylab(label="# of Words") +
    ggeasy:: easy_center_title() +
    labs(fill="Type of Error")
}

plotWhereError("r")
