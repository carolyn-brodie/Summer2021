

plotBME <- function(sound) {
library(dplyr)
library(ggplot2)
library(stringr)
library(ggeasy)

incorrectData <- read.csv("summer_work/Graphs/ErrorFile.csv", sep=';')
print(incorrectData)
number_of_lines <- nrow(read.csv("summer_work/Graphs/ErrorFile.csv", sep=';'))

errorWords <-incorrectData %>%
  filter(str_detect(WhereErrorOccurred, "Beginning|Middle|End"))

  s <- paste("^", sound, sep="")
  Words <- errorWords %>%
    filter(str_detect(word, s))
  ggplot(Words, aes(x=WhereErrorOccurred, fill=word)) +
    geom_bar(stat="count") +
    scale_y_continuous(breaks=seq(0,number_of_lines,1)) +
    ggtitle(label="Session Feedback") +
    xlab(label="Error Location") +
    ylab(label="# of Words") +
    ggeasy:: easy_center_title() +
    labs(fill="Expected Word")

}

plotBME("r")
