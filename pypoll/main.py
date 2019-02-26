# import 
import os
import csv
csvpath = os.path.join("..", "pypoll", "election_data.csv")
# open file
with open (csvpath, newline="") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvfile)
    #find total votes
    total_votes = []
    candidates = []
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    for row in csvreader: 
        total_votes.append(row[0:])
        #print (total_votes[0])
        #find candidates
        candidates.append(row[2])
        #print (candidates)   
        #4 candidates: Khan, Correy, Li and O'Tooley, find their breakdown
        if row[2] == "Khan": 
            khan_votes += 1
        elif row[2] == "Correy": 
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1
    dict_candidates = dict.fromkeys(candidates)
    candidates = list (dict_candidates)
    #how did the candidates do? 
    def election_rundown (x): 
        election_results = round((x/len(total_votes)*100), 3)
        return election_results

    Khan = election_rundown(khan_votes)
    Correy = election_rundown(correy_votes)
    Li = election_rundown(li_votes)
    OTooley = election_rundown(otooley_votes)
    #print(khan, correy, li, otooley)
    # find winner
    #print (candidates)
    winning_votes = [khan_votes, correy_votes, li_votes, otooley_votes]
    winners_results = max(winning_votes)
    y = winning_votes.index(winners_results)
    winner = candidates[y]
    #print (winner) 
    #--------------RESULTS--------------#
    results = f"""Election Results
        ---------------------------
        Total Votes: {len(total_votes)}
        ---------------------------
        Khan: {Khan}% ({khan_votes})
        Correy: {Correy}% ({correy_votes})
        Li: {Li}% ({li_votes})
        O'Tooley: {OTooley}% ({otooley_votes})        
        ---------------------------
        Winner: {winner}
        """
    print (results)
    #--------------EXPORT--------------#
    txtpath = os.path.join ("..", "pypoll", "main.txt")
    with open (txtpath,'w') as file: 
       file.write(results)