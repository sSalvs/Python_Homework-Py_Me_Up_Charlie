#PYBank 
import os
import csv

dirname = os.path.dirname(__file__)
PyBank_csv = os.path.join(dirname,'..', 'Resources','PyBank.csv')
#open the csv

with open(PyBank_csv) as csvfile:
    
    #split out the csv 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # print(f"csvheader: {csv_header}")

    for row in csv_reader:
        Total_Months = []
        print(f"Total Months:" + "{Total_Months}")

    # #set the def for total months 
    # def Total_Months(Bank_data):
    #     date = len(bank_data[0])
    #     Print(f"Total Months: {int(date)}")


    
    # Set 

        # Total = len(Profit_Loss)

        # Average_Change = (total / len(total))

        # Greatest_Increase = 
       

    #count the total months 



    



#remove the header so that we do not count that row - done 


#count the total months - use append and len to add?



#count the total profits/losses


#average Change 


#Greatest Increase in profits 


#Greatest Decrease to profits 