#PyPoll
import os
import csv

#open the csv file 

dirname = os.path.dirname(__file__)
PyPoll_csv = os.path.join(dirname, 'Resources','PyPoll.csv')
#open the csv

#set the variables 
votes = 0
vote_list = {}
Khan_votes = 0
Khan_percent = 0
Correy_votes = 0
Correy_percent = 0
Li_votes = 0
Li_percent = 0
OTooley_votes = 0 
OTooley_percent = 0 
Candidate_List = []
winner = 0 


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
            vote_list[candidates] = 1
        else:
            vote_list[candidates] += 1

                      
        #calculate votes per candidate 
        if Candidate_List[0] == candidates:
            Khan_votes += 1
        elif Candidate_List[1] == candidates:
            Correy_votes += 1
        elif Candidate_List[2] == candidates:
            Li_votes += 1
        elif Candidate_List[3] == candidates:
            OTooley_votes += 1

#calculate the percentage per candidate 
Khan_percent = round(((Khan_votes / votes)*100),3)
Correy_percent = round((Correy_votes / votes)*100,3)
Li_percent = round((Li_votes / votes)*100,3)
OTooley_percent = round((OTooley_votes / votes)*100,3)

#find the winner - use dictionary set up t
winner = max(vote_list,key=vote_list.get)

#print results to terminal 
print("Election Results")
print("-----------------------")
print("Total Votes: " + str(votes))
print("-----------------------")
print(Candidate_List[0] + ": " + str(Khan_percent) + "% (" + str(Khan_votes) + ")")
print(Candidate_List[1] + ": " + str(Correy_percent) + "% (" + str(Correy_votes) + ")")
print(Candidate_List[2] + ": " + str(Li_percent) + "% (" + str(Li_votes) + ")")
print(Candidate_List[3] + ": " + str(OTooley_percent) + "% (" + str(OTooley_votes) + ")")
print("-----------------------")
print("Winner: " + str(winner))
print("-----------------------")

#print to txt file 
PyPoll_csv = os.path.join(dirname,'Analysis','PyPoll_Analysis.txt')
with open(PyPoll_csv, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-----------------------\n")
    txtfile.write("Total Votes: " + str(votes) + " \n")
    txtfile.write("-----------------------\n")
    txtfile.write(Candidate_List[0] + ": " + str(Khan_percent) + "% (" + str(Khan_votes) + ")\n")
    txtfile.write(Candidate_List[1] + ": " + str(Correy_percent) + "% (" + str(Correy_votes) + ")\n")
    txtfile.write(Candidate_List[2] + ": " + str(Li_percent) + "% (" + str(Li_votes) + ")\n")
    txtfile.write(Candidate_List[3] + ": " + str(OTooley_percent) + "% (" + str(OTooley_votes) + ")\n")
    txtfile.write("-----------------------\n")
    txtfile.write("Winner: " + str(winner) + " \n")
    txtfile.write("-----------------------")