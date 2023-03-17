from bs4 import BeautifulSoup

html_file= open("eplustbl.htm")
html_file_in_bs4= BeautifulSoup(html_file, 'html.parser')
data_from_all_tables= html_file_in_bs4.findAll('table')
tables_to_be_extracted = [1,13,108,110]

final_tables = []
for i in tables_to_be_extracted:
    final_tables.append(data_from_all_tables[i-1])

for table in final_tables:
    temp_table_for_csv=[]
    table_data=table.findAll('td')
    #calculate cols in table
    col=0
    rows=len(table_data)
    for tds in table_data:
        if tds.text.replace('.', '', 1).strip().isdigit():
            break
        else:
            col=col+1
    col = col - 1
    rows = int(rows/col)
    final_table_data=[]
    temp_array=[]
    print(rows)
    for i in range(len(table_data)):
        temp_array.append(table_data[i].text.strip())
        print(i,",",(i+1)%rows)
        if ((i+3)%rows==0 and i!=0):
            final_table_data.append(temp_array)
            temp_array=[]
    print(final_table_data)
    break
        
# not_added.insert(0,["Date","ID","Part Number","Quantity","Error Message", "Existing Quantity", "Requested Quantity"])
# fileName = "notadded_"+str(worker_id)+".csv"
# np.savetxt(os.path.join(UPLOAD_FOLDER,fileName),not_added,delimiter =", ", fmt ='% s')