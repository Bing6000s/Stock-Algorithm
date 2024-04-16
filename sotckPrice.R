# Read the CSV file into a data frame
data <- read.csv('stock_prices.csv')

# Iterate over indices 1 to 40
for (i in 1:40) {
  # Subset the data to include only the first i values
  subset_data <- data[1:i, ]
  
  # Plot the subset of data
  plot(subset_data$Date, subset_data$Close_Price, type = "l", xlab = "Date", ylab = "Close Price", main = paste("Plot for", i, "values"))
  
  # Add a pause to see each plot (optional)
  Sys.sleep(1)
}

