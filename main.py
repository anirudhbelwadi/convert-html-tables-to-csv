from bs4 import BeautifulSoup
import numpy as np

# Open the HTML file 
html_file= open("test.htm")

# Convert to traversable format
html_file_in_bs4= BeautifulSoup(html_file, 'html.parser')

# Get data of all <table> tags
data_from_all_tables= html_file_in_bs4.findAll('table')

# Set the table numbers to be extracted according to its rank in html file
# Use the Ctrl+f/Cmd+f to find the nth occurrence of "<table"
# DO NOT MISS TO ADD THE < in <table
tables_to_be_extracted = [1,13,108,110]

# We will collect the data of only the required tables in this variable final_tables
final_tables = []
for i in tables_to_be_extracted:
    final_tables.append(data_from_all_tables[i-1])

# This loop will run n number of times, where n = length of tables_to_be_extracted list
for k in range(len(final_tables)):    
    # Get all the <td> tags from the particular table
    table_data=final_tables[k].findAll('td')
    
    # Function to calculate columns in table
    # This loop will run until it finds a number in the table cells
    # Basically we calculating the number of cells before we encounter a cell containing numbers
    # This will give us an extra cell count as there is a non-numeric cell in every second row of all the tables
    # We will subtract this from the count later on
    columns=0
    for tds in table_data:
        if tds.text.replace('.', '', 1).strip().isdigit():
            break
        else:
            columns=columns+1

    # Subtract 1 form the count to get the actual number of columns
    columns = columns - 1
    
    # To calculate the number of rows, divide the total number of cells by columns
    rows = int(len(table_data)/columns)
    
    # This variable will store data that needs to be fed into the csv file
    final_table_data_for_csv=[]
    
    # This is used to temporarily store row data and append it to final_table_data_for_csv list
    temp_array=[]
    
    # This will iterate through all the cells in the table
    for i in range(len(table_data)):
        # Here .text will get the text inside the <td> tag
        # .strip() will remove leading and trailing spaces in the data
        temp_array.append(table_data[i].text.strip())
        
        # Condition to push the row data into final_table_data_for_csv
        # And also to create a new temp_array 
        # whenever we reach the end of a row
        if ((i+1)%columns==0 and i!=0):
            final_table_data_for_csv.append(temp_array)
            temp_array=[]
            
    # Assign any desired file name.
    # Format used here: table_n.csv
    # n --> rank of table in the html file
    fileName = "table_"+str(tables_to_be_extracted[k])+".csv"
    
    #Save the csv file
    np.savetxt(fileName,final_table_data_for_csv,delimiter =", ", fmt ='% s')