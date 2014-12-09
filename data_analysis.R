#run a regression of GDP vs Energy Consumption on each country stat set
runRegression <- function(x) {lm(GDP ~ Total.Energy.Consumption, data=x)}
countryEnergyRegression <- lapply(countryStats, runRegression)
beta1Coeffs <- lapply(countryEnergyRegression, function(x) {x$coefficients[[2]]})
rSquaredVals <- lapply(countryEnergyRegression, function(x) {summary(x)[[8]]})
correlationVals <- sqrt(as.double(rSquaredVals))

#create a bar chart of the correlation between GDP and Energy Consumption for each regression model
barplot(as.double(correlationVals), ylim=c(0.0,1.0), ylab="correlation", xlab="country", col="blue", main="Correlation: GDP vs. Energy Consumption", names=substr(names(countryStats),0,3))

