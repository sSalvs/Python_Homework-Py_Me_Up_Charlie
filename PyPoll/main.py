#PyPoll
import os
import csv

#open the csv file 

dirname = os.path.dirname(__file__)
PyPoll_csv = os.path.join(dirname, 'Resources','PyPoll.csv')
#open the csv

#set the variables 
votes = 0
Khan_votes = 0
Candidate_List = []
Vote_list = {}


#loop through the sheet

with open(PyPoll_csv) as csvfile:

    #split out the csv 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for rows in csvreader:
        votes += 1
        candidates = str(rows[2])
        if candidates not in Candidate_List:
            Candidate_List.append(candidates)
            Vote_list[candidates] = 1
        # print(Candidate_List)
        
        

        # if Candidate_List[0] == candidates:
        #     Khan_votes = Khan_votes + 1
        
        # print((Khan_votes))

          
    


print("Election Results")
print("-----------------------")
print("Total Votes: " + str(votes))
print("-----------------------")
# print(f"Khan: " + str(Khan_Votes))
