library(ggplot2)

#Plot Energy Intensity vs. Time for all South Asian countries
ggplot(data = South_Asian_Stats, aes(x=date, y=EnergyIntensity)) + ggtitle("South Asia Energy Intensity of GDP") + xlab("Year") + ylab("Energy Intensity of GDP") + geom_line(aes(colour=country))

#Exclude Maldives and plot again, as Maldives appear to be an outlier
No_Maldives <- South_Asian_Stats[South_Asian_Stats$country != "Maldives",]
ggplot(data = No_Maldives, aes(x=date, y=EnergyIntensity)) + ggtitle("Energy Intensity of GDP (Selected Countries)") + xlab("Year") + ylab("Energy Intensity of GDP") + geom_line(aes(colour=country))
