
# CSV File 
# CSV definition: CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. A CSV file stores tabular data (numbers and text) in plain text. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format
import csv

# PyBank CSV File and text file (Not sure if this was the right link but I wanted to just get to the data without os since I get lots of errors when I try that https://stackoverflow.com/questions/25967479/save-output-values-in-txt-file-in-columns-python)
file_to_load = "C:/Users/evanm/OneDrive/Desktop/PyBank/Resources/budget_data.csv"
file_to_output = "budget_breakdown.txt"

# Variables section
total_months = 0
prev_revenue = 0
revenue_avg = 0
# Empty lists for Month of Change and Average Change
month_of_change = []
revenue_change_summary = []
# "": Empty string
# Explaination: Months and Years will be generated into the strings in the form of Greatest Increases (Month-Year) and Greatest Decrease (Month-Year)
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999]
total_revenue = 0


# Read the CSV and convert it into a list of dictionaries (stumbled upon with open on slack: https://stackoverflow.com/questions/35818124/using-with-open-as-file-method-how-to-write-more-than-once)
with open(file_to_load) as budget_data:
    reader = csv.DictReader(budget_data)
    
    for x in reader: 

        # Ted sent us an example on Slack which was similar but it gave me the same results
        
        total_months = total_months + 1
        total_revenue = total_revenue + int(x["Profit/Losses"])
        # Determine the change in Revenue
        revenue_change = int(x["Profit/Losses"]) - prev_revenue
        prev_revenue = int(x["Profit/Losses"])
        revenue_change_summary = revenue_change_summary + [revenue_change]
        month_of_change = month_of_change + [x["Date"]]
        


        # Greatest Increase value
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = x["Date"]
            greatest_increase[1] = revenue_change

          # Greatest Decrease value
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = x["Date"]
            greatest_decrease[1] = revenue_change  


            

# Change in the Average Revenue 
revenue_avg = sum(revenue_change_summary) / len(revenue_change_summary)

# Print output of PyBank (Wanted to print a bunch of text in one go and found this https://stackoverflow.com/questions/44780357/how-can-i-use-newline-n-in-an-f-string-to-format-output)
# Couldn't get Average Revenue Change
output = (
                f"\nFinancial Analysis\n"
                f"                            \n"
                f"---------------------------\n"
                f"                            \n"
                f"Total Months: {total_months}\n"
                f"                            \n"
                f"Total Revenue: ${total_revenue}\n"
                f"                            \n"
                f"Average Change: ${revenue_avg}\n"
                f"                            \n"
                f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
                f"                            \n"
                f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
                                                                                                         )
    

# Print the output
print (output)



#Export the results to a text file (Ted told us to find a way to put text on a file so I googled it and found https://stackoverflow.com/questions/5214578/print-string-to-text-file)
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
        
