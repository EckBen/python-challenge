import os, csv

# Create path to data, open file, and make reader object
csvPath = os.path.join('Resources', 'budget_data.csv')
with open(csvPath, 'r', newline='') as csvFile:
    budgetData = csv.reader(csvFile, delimiter=',')

    # Skip header
    next(budgetData, None)

    # Initialize variables for month counter, net total tracker,
        # greatest increase, and greatest loss
    months = 0
    netTotal = 0
    greatestIncrease = 0
    greatestLoss = 0

    # Iterate through rows
    for rows in budgetData:
        # Store data in easy to call variables
        date = rows[0]
        change = int(rows[1])

        # Determine whether the current value is a greatest increase, loss, or neither
        if change > greatestIncrease:
            # Store new increase and date which it occured
            greatestIncrease = change
            increaseDate = date

        if change < greatestLoss:
            # Store new loss and date which it occured
            greatestLoss = change
            lossDate = date
        
        # Add profit/loss to net total tracker
        netTotal += change

        # Increment month counter
        months += 1
    
    # Calculate the average change
    avgChange = round((netTotal / months), 2)

    # Store a nice results table
    formatted = (f'Financial Analysis\n'
                f'---------------------------\n'
                f'Total Months: {months}\n'
                f'Total: ${netTotal}\n'
                f'Average Change: ${avgChange}\n'
                f'Greatest Increase in Profits: {increaseDate} (${greatestIncrease})\n'
                f'Greatest Decrease in Profits: {lossDate} (${greatestLoss})'
            )
    
    # Print table
    print(formatted)

    # Export a text file with results
    outputPath = os.path.join('Resources', 'FinancialAnalysis.txt')
    with open(outputPath, 'w') as outputFile:
        # Write the table into a txt file
        outputFile.write(formatted)

    # Close all files
        outputFile.close()