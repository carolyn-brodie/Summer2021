plotLetter <- function() {
  library(dplyr)
  library(ggplot2)
  library(stringr)
  library(ggeasy)

png("TypeOFError.png")

incorrectData <- read.csv("summer_work/excelFile1.csv", sep=';')

number_of_lines <- nrow(read.csv("summer_work/excelFile1.csv", sep=';'))

errorWords <-incorrectData %>%
  filter(str_detect(WhereErrorOccurred, "Beginning|Middle|End"))

   TypeOfError <- ggplot(errorWords, aes(x=TypeOfError, fill=Word)) +
     geom_bar(stat="count") +
     scale_y_continuous(breaks=seq(0,number_of_lines,1)) +
      ggtitle(label="Session Feedback") +
      xlab(label="Type of Error") +
      ylab(label="# of Words") +
      ggeasy:: easy_center_title() +
      labs(fill="Expected Word")

print(TypeOfError)
dev.off()

ggsave("TypeOfError.png", path = "summer_work/Graphs", scale = 0.15)
}

plotLetter()
