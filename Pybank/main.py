## import first
import os
import csv

## how to get file path
csvpath = os.path.join('Resources', 'budget_data.csv')

## empty list to store data
earnings = []
monthly_delta = []
time_stamp = []

## set variables to zero
num_months = 0
total_earnings = 0
total_monthly_delta = 0
initial_earnings = 0


##opening the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    ## read the header first
    csv_header = next(csvreader)
    ## loop through data
    for row in csvreader:

      ##adding up total num of months
      num_months = num_months + 1
      
      ##adding dates to empty list
      time_stamp.append(row[0])
      
      ##adding profits to empty list
      earnings.append(row[1])

      ##summing up total profits
      total_earnings = total_earnings + int(row[1])
      
      final_earnigs = int(row[1])

      
      monthly_delta_profits = final_earnigs - initial_earnings

      monthly_delta.append(monthly_delta_profits)
      
      total_monthly_delta = total_monthly_delta + monthly_delta_profits
      initial_earnings = final_earnigs

      avg_profit_delta = (total_monthly_delta/num_months)

      greatest_profit_incdelta = max(monthly_delta)
      greatest_profit_decdelta = min(monthly_delta)

      increase_date = time_stamp[monthly_delta.index(greatest_profit_incdelta)]
      decrease_date = time_stamp[monthly_delta.index(greatest_profit_decdelta)]

## print out results in terminal
print('Financial Analysis''\n')
print('----------------------------------''\n')
print(f'Total Months: {num_months}''\n')
print(f'Total Profit: ${total_earnings}''\n')
print(f'Avg. Change: ${avg_profit_delta}''\n')
print(f'Greatest Increase in Profits: {increase_date} ${greatest_profit_incdelta}''\n')
print(f'Greatest Decrease in Profits: {decrease_date} ${greatest_profit_decdelta}''\n')


## write results as a text file
with open('financial_analysis.text', 'w') as text:

  text.write('Financial Analysis''\n')
  text.write('----------------------------------''\n')
  text.write(f'Total Months: {num_months}''\n')
  text.write(f'Total Profit: ${total_earnings}''\n')
  text.write(f'Avg. Change: ${avg_profit_delta}''\n')
  text.write(f'Greatest Increase in Profits: {increase_date} ${greatest_profit_incdelta}''\n')
  text.write(f'Greatest Decrease in Profits: {decrease_date} ${greatest_profit_decdelta}''\n')


  

        


     










