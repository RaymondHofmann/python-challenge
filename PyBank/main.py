import pandas as pd
# Read in the budget_data.csv file
df = pd.read_csv("budget_data.csv")
df
# The total number of months included in the dataset
total_months = df["Date"].count()
total_months
# The net total amount of "Profit/Losses" over the entire period
net_total = df["Profit/Losses"].sum()
net_total
# The changes in "Profit/Losses" over the entire period
df["Changes"] = df["Profit/Losses"].diff()
df["Changes"]
# The average of those changes
average_change = df["Changes"].mean()
average_change
# The greatest increase in profits (date and amount) over the entire period
max_increase = df["Changes"].max()
max_increase_date = df.loc[df["Changes"] == max_increase, "Date"].values[0]
max_increase
max_increase_date
# The greatest decrease in profits (date and amount) over the entire period
max_decrease = df["Changes"].min()
max_decrease_date = df.loc[df["Changes"] == max_decrease, "Date"].values[0]
max_decrease
max_decrease_date
# Print the results
print("Total Months: " + str(total_months))
print("Net Total: " + str(net_total))
print("Average Change: " + str(average_change))
print("Greatest Increase in Profits: " + max_increase_date + " (" + str(max_increase) + ")")
print("Greatest Decrease in Profits: " + max_decrease_date + " (" + str(max_decrease) + ")")