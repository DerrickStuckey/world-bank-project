South_Asian_Stats <- read.csv("./South_Asian_Stats.csv")
South_Asian_Stats$EnergyIntensity <- South_Asian_Stats$GDP / South_Asian_Stats$Total.Energy.Consumption
#South_Asian_Stats$ElectricityIntensity <- South_Asian_Stats$GDP / South_Asian_Stats$Electricity.Output
South_Asian_Stats$EnergyPerCapita <- South_Asian_Stats$Total.Energy.Consumption / South_Asian_Stats$Total.Population
South_Asian_Stats$GDPPerCapita <- South_Asian_Stats$GDP / South_Asian_Stats$Total.Population

bangladeshStats <- South_Asian_Stats[South_Asian_Stats$country == "Bangladesh",]
bhutanStats <- South_Asian_Stats[South_Asian_Stats$country == "Bhutan",]
indiaStats <- South_Asian_Stats[South_Asian_Stats$country == "India",]
sriLankaStats <- South_Asian_Stats[South_Asian_Stats$country == "Sri Lanka",]
maldivesStats <- South_Asian_Stats[South_Asian_Stats$country == "Maldives",]
nepalStats <- South_Asian_Stats[South_Asian_Stats$country == "Nepal",]
pakistanStats <- South_Asian_Stats[South_Asian_Stats$country == "Pakistan",]

library(ggplot2)
ggplot(data = South_Asian_Stats, aes(x=date, y=EnergyIntensity)) + ggtitle("South Asia Energy Intensity of GDP") + xlab("Year") + ylab("Energy Intensity of GDP") + geom_line(aes(colour=country))
No_Maldives <- South_Asian_Stats[South_Asian_Stats$country != "Maldives",]
ggplot(data = No_Maldives, aes(x=date, y=EnergyIntensity)) + ggtitle("Selected Countries Energy Intensity of GDP") + xlab("Year") + ylab("Energy Intensity of GDP") + geom_line(aes(colour=country))

countryStats <- list(bangladeshStats, bhutanStats, indiaStats, sriLankaStats, maldivesStats, nepalStats, pakistanStats)
names(countryStats) <- c("Bangladesh", "Bhutan", "India", "Sri Lanka", "Maldives", "Nepal", "Pakistan")

#run a regression of GDP vs Energy Consumption on each country stat set
runRegression <- function(x) {lm(GDP ~ Total.Energy.Consumption, data=x)}
countryEnergyRegression <- lapply(countryStats, runRegression)
beta1Coeffs <- lapply(countryEnergyRegression, function(x) {x$coefficients[[2]]})
rSquaredVals <- lapply(countryEnergyRegression, function(x) {summary(x)[[8]]})
correlationVals <- sqrt(as.double(rSquaredVals))
  
#create a bar chart of the beta1 coefficients for each regression model
barplot(as.double(correlationVals), col="blue", main="GDP, Energy Correlation", names=substr(names(countryStats),0,3))


