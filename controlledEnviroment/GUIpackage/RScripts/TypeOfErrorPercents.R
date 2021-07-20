#Graphing errors over time
plotErrorPercents <- function(f1, f2, file) {
  library(ggplot2)
  library(ggeasy)

   fileName <- file
   fileName1 <- paste("/outData/", fileName, sep = "")
     fileName1 <- paste(getwd(),fileName1,sep = "")
   fileNamecsv <- paste(fileName1,".csv",sep = "")
   pngName <- paste("TypeOfErrorPercent", fileName, sep = "")
   addpng <- paste(pngName, ".png", sep ="")
   addpng <- paste("/Graphs/",addpng,sep = "")
  addpng <- paste(getwd(),addpng,sep = "")
  print(addpng)
   png(addpng)

  percentError <- read.csv(fileNamecsv, sep = ";")
  week <- percentError[c(f1:f2), c(1,2,3,4)]
  number_of_lines <- nrow(read.csv(fileNamecsv, sep = ";"))
  displayAddition <- paste(round((week[,3]) * 100, 1), "%", sep="")
  displayDeletion <- paste(round((week[,2]) * 100, 1), "%", sep="")
  displaySubstitution <- paste(round((week[,4]) * 100, 1), "%", sep="")

  PercentOfError <- ggplot(week, aes(x= Sessions)) +
    geom_line(aes(y=Addition, col="Addition")) +
    geom_line(aes(y=Deletion, col="Deletion")) +
    geom_line(aes(y=Substitution, col="Substitution")) +

    geom_label(aes(y=Addition, label= displayAddition), fill = "white") +
    geom_label(aes(y=Deletion, label=displayDeletion), fill="white") +
    geom_label(aes(y=Substitution, label= displaySubstitution), fill="white") +

    scale_color_manual(values=c("chartreuse2", "slateblue", "red")) +
    ggtitle(label="Session Feedback") +
    ggeasy:: easy_center_title() +
    xlab(label="Session") +
    ylab(label="Percentages") +
    theme(legend.title=element_blank())+

    scale_x_continuous(breaks=seq(0,number_of_lines,1)) +
    scale_y_continuous(labels= scales::percent, breaks=seq(0,1,.1))
  print(PercentOfError)
dev.off()

}

