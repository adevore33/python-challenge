import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    rowcount = 0
    total = 0
    diff_list = []
    month_list = []
    previous = 0
    for row in csvreader:
        rowcount += 1
        total += int(row[1])
        if rowcount == 1:
            previous = int(row[1])
        diff_list.append(int(row[1])- previous)
        previous = int(row[1])
        month_list.append(row[0])


    
diff_list.pop(0)
month_list.pop(0)
    
average = sum(diff_list) / len(diff_list)
max_change = max(diff_list)
max_index = diff_list.index(max_change)
max_month = month_list[max_index]
min_change = min(diff_list)
min_index = diff_list.index(min_change)
min_month = month_list[min_index]


print("Financial Analysis")

print("--------------------------")

print("Total Months:", rowcount)
print(f"Total: ${total}")
print(f"Average Change: ${round(average, 2)}")
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

output_path = r'C:\Users\austi\OneDrive\Desktop\python-challenge\PyBank\analysis\pybank_analysis.txt'
with open(output_path, "w") as txtfile:
    
    txtfile.writelines(f"Financial Analysis\n--------------------------\nTotalMonths: {rowcount}\nTotal: ${total} \nAverage Change: ${round(average, 2)} \nGreastes increase in Profits: {max_month} (${max_change}) \nGreatest Decrease in Profits: {min_month} (${min_change}")
    