# Incorporate the library
import os
import csv

# Path to csv file
file = os.path.join('..', 'Resources', 'budget_data.csv')

#read the csv file
with open('budget_data.csv','r') as csvfile:
    filereader = csv.reader(csvfile, delimiter = ',')
    
    #Itrate through the columns
    fileheader = next(filereader)

    #Create empty lists to add the csv values to 
    month = []
    profit = []
    change_profit = []
                  
    #Iterate through the values and add them to the empty list 
    #column as an item in filereaser list
    for column in filereader:
        
        #By appending month (which is the list here that we created above)
            #we are adding to the end of the list the month count 
                #column [0] is basically pulling from the first column which is date 
                #same with [1], we ae pulling column with profits numbers
        month.append(column[0])
        profit.append(int(column[1]))
    
#To store change in profits using a for loop and a value i
# i will keep increasing as we loop thorugh
#Change profit list will store the change  
#In profits if we had a list like profits = [10, 15, 4] then the first value this list would store is 5, then -11
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      
#Evaluate the max and min from the change_profit list
increase = max(change_profit)
decrease = min(change_profit)

#Return the greatest increase in profits and greatest decrease in profits (index function)
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

#Print the analysis to the terminal
print("Financial Analysis\n-------------------------\n")
print(f"Total Months:{len(month)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month[month_decrease]} (${(str(decrease))})")

#Export a text file with the results
output = os.path.join(".", 'output.txt')
with open(output,"w") as new:
    new.write("Financial Analysis\n-------------------------\n")
    new.write(f"Total Months:{len(month)}\n")
    new.write(f"Total: ${sum(profit)}\n")
    new.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}\n")
    new.write(f"Greatest Increase in Profits: {month[month_increase]} (${(str(increase))})\n")
    new.write(f"Greatest Decrease in Profits: {month[month_decrease]} (${(str(decrease))})")