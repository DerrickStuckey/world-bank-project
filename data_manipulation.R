# Read in full dataset
South_Asian_Stats <- read.csv("./South_Asian_Stats.csv")

# Calculate derived attributes
South_Asian_Stats$EnergyIntensity <- South_Asian_Stats$GDP / South_Asian_Stats$Total.Energy.Consumption
#South_Asian_Stats$ElectricityIntensity <- South_Asian_Stats$GDP / South_Asian_Stats$Electricity.Output
South_Asian_Stats$EnergyPerCapita <- South_Asian_Stats$Total.Energy.Consumption / South_Asian_Stats$Total.Population
South_Asian_Stats$GDPPerCapita <- South_Asian_Stats$GDP / South_Asian_Stats$Total.Population

# Construct a separate dataframe for each country to be analyzed
bangladeshStats <- South_Asian_Stats[South_Asian_Stats$country == "Bangladesh",]
bhutanStats <- South_Asian_Stats[South_Asian_Stats$country == "Bhutan",]
indiaStats <- South_Asian_Stats[South_Asian_Stats$country == "India",]
sriLankaStats <- South_Asian_Stats[South_Asian_Stats$country == "Sri Lanka",]
maldivesStats <- South_Asian_Stats[South_Asian_Stats$country == "Maldives",]
nepalStats <- South_Asian_Stats[South_Asian_Stats$country == "Nepal",]
pakistanStats <- South_Asian_Stats[South_Asian_Stats$country == "Pakistan",]

# Store the country-specific dataframes in a list for batch processing
countryStats <- list(bangladeshStats, bhutanStats, indiaStats, sriLankaStats, maldivesStats, nepalStats, pakistanStats)
names(countryStats) <- c("Bangladesh", "Bhutan", "India", "Sri Lanka", "Maldives", "Nepal", "Pakistan")



