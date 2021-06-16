
plotBME <- function() {
   library(dplyr)
   library(ggplot2)
   library(stringr)
   library(ggeasy)

incorrectData <- read.csv("/Users/larakallem/PycharmProjects/Summer2021/summer_work/Graphs/fooddata", sep=';')
#print(incorrectData)
number_of_lines <- nrow(read.csv("/Users/larakallem/PycharmProjects/Summer2021/summer_work/Graphs/fooddata", sep=';'))

errorWords <-incorrectData %>%
  filter(str_detect(WhereErrorOccurred, "Beginning|Middle|End"))

  ggplot(errorWords, aes(x=WhereErrorOccurred, fill=Word)) +
    geom_bar(stat="count") +
    scale_y_continuous(breaks=seq(0,number_of_lines,1)) +
    ggtitle(label="Session Feedback") +
    xlab(label="Error Location") +
    ylab(label="# of Words") +
    ggeasy:: easy_center_title() +
    labs(fill="Expected Word")

}

plotBME()


