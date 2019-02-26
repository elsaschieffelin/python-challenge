#--------------------SET UP---------------------#
#import 
import os
import csv
csvpath = os.path.join ("..", "pybank", "budget_data.csv")
#define variables
total_months = []
total = 0
change = []
counter1 = 0
#--------------------Open Csv---------------------#
with open (csvpath, newline="") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    # Find total months & change 
    for row in csvreader:
        if counter1 > 0:
            val2 = int(row[1])
            change.append(val2 - val1)
            val1 = val2
        total_months.append(row[0])
        #print (total_months[0])
        #print (len(total_months))
        total += int(row[1])
        #print (total)
        #value.append(int(row[1]))
        val1 = int(row[1])
        counter1 += 1
   #--------------------average change---------------------#
    average = round(sum(change)/len(change), 2)
    #--------------------max increase---------------------#
    greatest_increase = max(change)
    #print (greatest_increase)
    max_index = change.index(greatest_increase)
    #to find the month of the max increase, we will need month_total index
    x = int(max_index) + 1
    max_row = total_months[x]
    #print(max_row)
    #--------------------max decrease---------------------#
    greatest_decrease = min(change)
    min_index = change.index(greatest_decrease)
    y = int(min_index) + 1
    min_row = total_months[y]
    # -------------------- RESULTS -------------------------#
    results = f"""Financial Analysis
    ------------------------------------
    Total Months: {len(total_months)}
    Total: ${total}
    Average Change: ${average}
    Greatest Increase in Profits: {max_row} (${greatest_increase})
    Greatest Decrease in Profits: {min_row} (${greatest_decrease})"""
    print (results)
    export_results = ''.join(results)
    #print (export_results)
    #-------------------- EXPORT ---------------------------#
    txtpath = os.path.join ("..", "pybank", "main.txt")
    with open (txtpath,'w') as file: 
       file.write(export_results)