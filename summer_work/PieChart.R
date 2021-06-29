percent_Of_Sessions <- function(f1, f2, file) {

library(ggplot2)

   fileName <- file
   fileName2 <- paste("/Users/zachg/PycharmProjects/Summer2021a/summer_work/", fileName, sep ="")
   fileNamecsv <- paste(fileName2, ".csv", sep ="")
   pngName <- paste("PieChart", fileName, sep = "")
   addpng <- paste(pngName, ".png", sep ="")
   png(addpng)


percents_Of_Words.df <- read.csv(fileNamecsv, sep = ";")
percents_Of_Words.df

right_Words <- mean(percents_Of_Words.df[c(f1, f2), "Correct"])
wrong_Words <- mean(percents_Of_Words.df[c(f1, f2), "Incorrect"])
unsaid_Words <- mean(percents_Of_Words.df[c(f1, f2), "NoResponse"])

data_frame = data.frame("Words" = c("Correct", "Incorrect", "No Response"), "percentages" = c(right_Words, wrong_Words, unsaid_Words))

bar_Plot <- ggplot(data_frame, aes(x = "", y = percentages, fill = Words)) +
  geom_bar(width = 1, stat = "identity")

pie_Chart <- bar_Plot + coord_polar("y", start = 0) + theme_void() +
  ggtitle("Percentages of Words") +
  theme(plot.title = element_text(hjust = 0.5)) +
  geom_text(aes(label = paste(round(percentages / sum(percentages) * 100, 1), "%")),
            position = position_stack(vjust = 0.5))

print(pie_Chart)
dev.off()

ggsave(addpng, path = "summer_work/Graphs", scale =1)
}
