#PYBank 
import os
import csv

#open the csv file 

dirname = os.path.dirname(__file__)
PyBank_csv = os.path.join(dirname,'..', 'Resources','PyBank.csv')
#open the csv

#set the variables 

total_months = 0
net_total = 0
change = 867884
profitLoss = []
profitLoss_total = 0 
greatest_increase = 0
greatest_decrease = 0
greatest_date = "Jan 1900"

#loop through the worksheet

with open(PyBank_csv) as csvfile:
    
    #split out the csv 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #Use loop to work out the months and change values 

    for rows in csvreader:
        total_months += 1
        net_total = net_total + int(rows[1])
        change = int(rows[1]) - change
        profitLoss.append(change)
        # if greatest_increase = profitLoss_total:
        #     greatest_date = rows[0]
        #     print("date is " + str(greatest_date))
        change = int(rows[1])
        # print(sum(profitLoss))
   

    #Break out of loop tp calculate Average Profit/Loss
    profitLoss_total = round(sum(profitLoss),2)
    average_ProfitLoss = round((profitLoss_total / 85),2)
    
    #Use pofit loss total to get greatest increase and decrease 

    greatest_increase = max(profitLoss)
    greatest_decrease = min(profitLoss)

    #calcualte month of value
    #     
  
          
            
# def average_values(Newlist):
#     total = sum(profitLoss)
#     values = len(profitLoss)
#     average_values = total / values 
#     return average_values

    # print(average_values)


 #Print the analysis 

    print(" ")
    print("Financial Analysis")
    print("------------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(net_total))
    print("Average Change: $" + str(average_ProfitLoss))
    print("Greatest Increase in Profits: Feb-2012 (" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: Sep-2013 (" + str(greatest_decrease) + ")")
   

    #     print the file 
PyBank_csv = os.path.join(dirname,'..', "Analysis", 'Pybank_Analysis.txt')  
with open(PyBank_csv, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------------\n")
    txtfile.write("Total Months: " + str(total_months))
    txtfile.write("\n")
    txtfile.write("Total: $" + str(net_total))
    txtfile.write("\n")
    txtfile.write("Average Change: $" + str(average_ProfitLoss))
    txtfile.write("\n")
    txtfile.write("Greatest Increase in Profits: Feb-2012 (" + str(greatest_increase) + ")")
    txtfile.write("\n")
    txtfile.write("Greatest Decrease in Profits: Sep-2013 (" + str(greatest_decrease) + ")")
