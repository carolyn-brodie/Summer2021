read.csv("", sep = ";")
patient1data <- read.csv("", sep =";")
read.csv("", sep = ";")
patient2data <- read.csv("", sep =";")

patient1SubErrors <- patient1data %>%
  filter(str_detect(COLUMNNAME, "substituion"))

patient2SubErrors <- patient2data %>%
  filter(str_detect(COLUMNNAME, "substituion"))