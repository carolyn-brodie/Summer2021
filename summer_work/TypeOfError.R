plotLetter <- function(sound) {
  library(dplyr)
  library(ggplot2)
  library(stringr)
  library(ggeasy)

png("specificTypeOfError.png")

incorrectData <- read.csv("excelFile2.csv", sep=';')
number_of_lines <- nrow(read.csv("excelFile2.csv", sep=';'))

errorWords <-incorrectData %>%
  filter(str_detect(WhereErrorOccurred, "Beginning|Middle|End"))

  s <- paste("^", sound, sep="")
   Words <- errorWords %>%
     filter(str_detect(Word, s))
   TypeOfError <- ggplot(Words, aes(x=TypeOfError, fill=Word)) +
     geom_bar(stat="count") +
     scale_y_continuous(breaks=seq(0,number_of_lines,1)) +
      ggtitle(label="Session Feedback") +
      xlab(label="Type of Error") +
      ylab(label="# of Words") +
      ggeasy:: easy_center_title() +
      labs(fill="Expected Word")

print(TypeOfError)
dev.off()

ggsave("specificTypeOfError.png", path = "summer_work/Graphs", scale = 0.15)
}

plotLetter("r|c")

