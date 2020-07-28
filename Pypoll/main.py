import os
import csv


csvfilepath = os.path.join('Resources', 'election_data.csv')


count = 0
candidate_list =[]
uni_candiates = []
vote_count = []
vote_percentage = []

with open(csvfilepath) as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    
    for row in reader:


        count = count + 1

        candidate_list.append(row[2])

    for name in set(candidate_list):
        uni_candiates.append(name)

        y = candidate_list.count(name)
        vote_count.append(y)


        z = (y/count)*100
        vote_percentage.append(z)


    winning_vote_count = max(vote_count)

    winner = uni_candiates[vote_count.index(winning_vote_count)]



print('Election Results''\n')
print('----------------------------------''\n')
print(f'Total Votes: {count}''\n')
print('----------------------------------''\n')
for i in range(len(uni_candiates)):
            print(uni_candiates[i] + ": " + str(vote_percentage[i]) +"% (" + str(vote_count[i])+ ")")
print('----------------------------------''\n')
print(f'The winner is: {winner}')


with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write('----------------------------------''\n')
    text.write(f'Total Votes: {count}''\n')
    print('----------------------------------''\n')
    for i in range(len(uni_candiates)):
            text.write(uni_candiates[i] + ": " + str(vote_percentage[i]) +"% (" + str(vote_count[i])+ ")")
    text.write('----------------------------------''\n')
    text.write(f'The winner is: {winner}')
    