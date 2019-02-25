import os, csv, operator

# Create path to data, open file, and make reader object
csvPath = os.path.join('Resources', 'election_data.csv')
with open(csvPath, 'r', newline='') as csvFile:
    electionData = csv.reader(csvFile, delimiter=',')

    # Skip header
    next(electionData, None)

    # Initialize vote counter, mostVotes and dictionary
    totalVotes = 0
    candidateResults = {}


    # Loop through all remaining rows in file
    for rows in electionData:
        # Count the number of votes cast
        totalVotes += 1
        # Add candidate to dictionary if not already there
        if rows[2] not in candidateResults:
            candidateResults[rows[2]] = 0
        # Add vote to appropriate candidate
        candidateResults[rows[2]] += 1
    # Determine winner of election
    winner = max(candidateResults.items(), key=operator.itemgetter(1))[0]

    # Store a nice results table
    formatted = [f'Election Results\n',
                f'---------------------------------\n',
                f'Total Votes: {totalVotes}\n',
                f'---------------------------------\n',
    ]

    # Loop through dictionary
    for candidate, votes in candidateResults.items():
        # Calculate percentage of votes won
        percentVotes = round(votes / totalVotes * 100, 3)
        formatted.append(f'{candidate}: {percentVotes}% ({votes})\n')
    
    # Finish formatting results table
    formatted.append(f'---------------------------------\n')
    formatted.append(f'Winner: {winner}\n')
    formatted.append(f'---------------------------------\n')
    
    # Export a text file with results
    outputPath = os.path.join('Resources', 'ElectionResults.txt')
    with open(outputPath, 'w') as outputFile:
        # Print table to termnial and write table to txt file
        for lines in formatted:
            print(lines, end='')
            outputFile.write(lines)

    # Close all files
        outputFile.close()