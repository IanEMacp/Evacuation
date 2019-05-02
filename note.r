library(readr)
library(dplyr)

results5050 <- read_csv("results5050.csv")
resultsLessAlarms <- read_csv("resultsLessAlarms.csv")
resultsMoreAlarms <- read_csv("resultsMoreAlarms.csv")

# True: Is there Fire
# True_1: Is there Order
# True_2: Did people Leave

View(results5050)
View(resultsLessAlarms)
View(resultsMoreAlarms)