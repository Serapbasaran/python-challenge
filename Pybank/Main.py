#Your task is to create a Python script that analyzes the records to calculate each of the following:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The average of the changes in "Profit/Losses" over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period


# Import dependencies
import os
import csv

# Define variables
date = []
profit_loss_changes = []


total_months = 0
total_net_pl = 0
previous_month_pl=0
current_month_pl=0
profit_loss_change=0

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")


# Open and read csv
with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
 
    # Read the header row first
    csv_header = next(csvfile)

    for row in csv_reader:  
        
        # Count of months
        total_months=total_months + 1

        # Calculate net total profit/loss over the time period
        current_month_pl= int(row[1])
        total_net_pl+= current_month_pl
        
        if (total_months==1):
            previous_month_pl=current_month_pl
            continue

        else:
            profit_loss_change=current_month_pl-previous_month_pl

            #Append each change in profit/loss for each month to profit_loss_changes[]   
            profit_loss_changes.append(profit_loss_change)

            #Get the current month"s p/l to be previous month's pl for the next loop
            previous_month_pl=current_month_pl

            #Append each month to total months to find out the month of greatest profit and loss
            date.append(row[0])

            #Calculate total monhtly changes of p/l and get the average of it
            total_profit_loss_changes=sum(profit_loss_changes)
            avarage_monthly_pl_changes=round(total_profit_loss_changes/(total_months-1),2)

            #Greatest change in profits  and greatest change in losses over the time period
            greatest_increase=max(profit_loss_changes)
            greatest_decrease=min(profit_loss_changes)

            #Find out the date of the greatest change in profits and greatest decrease in losses
            date_greatest_increase=date[profit_loss_changes.index(greatest_increase)]
            date_greatest_decrease=date[profit_loss_changes.index(greatest_decrease)]

  
    

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_months}")
print(f"Total: ${total_net_pl}")
print(f"Average Change: ${avarage_monthly_pl_changes}")
print(f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})")
print(f"Greatest Decreasde in Losses: {date_greatest_decrease} (${greatest_decrease})")


#Export a text file with the results

with open ("financial_analysis.text", "w") as text:

    text.write("Financial Analysis\n")
    text.write("----------------------------------\n")
    text.write(f"Total Months:  {total_months}\n")
    text.write(f"Total: ${total_net_pl}\n")
    text.write(f"Average Change: ${avarage_monthly_pl_changes}\n")
    text.write(f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})\n")
    text.write(f"Greatest Decreasde in Losses: {date_greatest_decrease} (${greatest_decrease})\n")

