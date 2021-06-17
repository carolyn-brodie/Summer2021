plotSessions <- function(f1, f2) {
  library(ggplot2)
  library(ggeasy)

png("PercentagePerSession.png")

  percentCorrect <- read.csv("summer_work/statsForExcels.csv", sep =';')
  number_of_lines <- nrow(read.csv("summer_work/statsForExcels.csv", sep =';'))
  week <-percentCorrect[c(f1:f2), c(1,2,3:4)]
  displayCorrect <- paste(round((week[,2]) * 100, 1), "%", sep="")
  displayIncorrect <- paste(round((week[,3]) * 100, 1), "%", sep="")
  displayNoResponse <- paste(round((week[,4]) * 100, 1), "%", sep="")

  LineGraph <- ggplot(week, aes(x=Sessions)) +
    #Add all 3 columns of data and create legend
    geom_line(aes(y=Correct, col="Correct")) +
    geom_line(aes(y=Incorrect, col="Incorrect")) +
    geom_line(aes(y=NoResponse, col="No Response")) +

    #Add values to points and fill label background
    geom_label(aes(y=Incorrect, label= displayIncorrect), fill = "white") +
    geom_label(aes(y=Correct, label=displayCorrect), fill="white") +
    geom_label(aes(y=NoResponse, label= displayNoResponse), fill="white") +

    #Add colors to lines
    scale_color_manual(values=c("chartreuse2", "slateblue", "red")) +

    #Add Titles
    ggtitle(label="Session Feedback") +
    xlab(label="Session") +
    ylab(label="Percentages") +

    #Create tick marks on x-axis & y-axis
    scale_x_continuous(breaks=seq(0,number_of_lines,1)) +
    scale_y_continuous(labels= scales::percent, breaks=seq(0,1,.1))+

    #Get rid of legend title
    theme(legend.title=element_blank()) +
    ggeasy:: easy_center_title()

print(LineGraph)
dev.off()

ggsave("PercentagePerSession.png", path = "summer_work/Graphs", scale = 0.15)
}
plotSessions(8,14)

