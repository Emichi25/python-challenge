# CSV File 
# CSV definition: CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. A CSV file stores tabular data (numbers and text) in plain text. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format
import csv

# PyPoll CSV File and text file (Not sure if this was the right link but I wanted to just get to the data without os since I get lots of errors when I try that https://stackoverflow.com/questions/25967479/save-output-values-in-txt-file-in-columns-python)
file_to_load = "C:/Users/evanm/OneDrive/Desktop/PyPoll/Resources/election_data.csv"
file_to_output = "election_breakdown.txt"

# Total Vote Count
total_votes = 0
# Candidate Options and Vote Counters
candidate_votes = {}
candidate_options = []
# Winning Candidate and Winning Count Tracker
winning_count = 0
winning_candidate = ""


# Read the CSV and convert it into a list of dictionaries  (stumbled upon with open on slack: https://stackoverflow.com/questions/35818124/using-with-open-as-file-method-how-to-write-more-than-once)
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    for j in reader: 

        # Determine the Total Vote Count
        total_votes = total_votes + 1

        # Extract the candidate name for each row
        candidate_name = j["Candidate"]

        # If the candidate does not match any existing candidates
        if candidate_name not in candidate_options:

          # Add it to the list of candidates in the running (Ted explained what you can use append for. See notes but end of list)
            candidate_options.append(candidate_name)


         # Track that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
   

# Print the results and export the results to a text file
with open(file_to_output, "w") as txt_file:


    # Print the final vote count (Wanted to print a bunch of text in one go and found this https://stackoverflow.com/questions/44780357/how-can-i-use-newline-n-in-an-f-string-to-format-output)
    election_results = (
                f"\nElection Results\n"
                 f"---------------------------\n"
                f"                            \n"
                f"Total Votes: {total_votes}\n"
                f"                           \n"
                f"---------------------------\n"
                
                                                                                                         )
    

    # Print the results
    print(election_results)


    # Save the final vote count to the text file (Ted told us to find a way to put text on a file so I googled it and found https://stackoverflow.com/questions/5214578/print-string-to-text-file)
    txt_file.write(election_results)



    # Determine the winner by looping the votes
    # Joesph point out one of my errors was becuase I had code in the for loop
    for candidate in candidate_votes:

        #Retrieves the vote count and  the percentages
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determines the winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            # votes = candidate
            winning_candidate = candidate

        # Print out each candidate's voter count and percentage
        voter_output = f"{candidate}: {vote_percentage:.5}% ({votes})\n"
        print(voter_output)

        #Send the candidates voter count and percentage to a text file
        txt_file.write(voter_output)

        # Print the winning candidate;s name
        winning_candidate_summary = (

                f"---------------------------\n"
                f"                           \n"
                f"Winner: {winning_candidate}\n"
                f"                           \n"
                f"---------------------------\n"

        )

        


    print(winning_candidate_summary)

        # Send the winner's name to the text file
    txt_file.write(winning_candidate_summary)