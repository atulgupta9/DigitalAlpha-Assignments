import pandas as pd
from docx import Document
document = Document(r"C:\Users\user\Desktop\New folder\Anthem.docx")
table = document.tables[1]
benefit_list = []
in_network_list = []
out_of_network_list = []
cell_wise_data = []
count = 0
for row in table.rows:
        count = 0
        for cell in row.cells:
            cell_data = cell.text.strip().split("	")
            cell_wise_data.append(cell_data)
            if(len(cell_data)>=3):
                if(count == 0):
                    if(cell_data[0]==""):
                        continue
                    else:
                        benefit_list.append(cell_data[0])
                        count+=1
                if(count == 1 and count<len(cell_data)):
                    in_network_list.append(cell_data[1])
                    count+=1
                if(count == 2 and count<len(cell_data)):
                    out_of_network_list.append(cell_data[2])
                    count+=1            
                if(count == 3 and count<len(cell_data)):
                    in_network_list.append(cell_data[3])
                    count+=1
d = {}
d[benefit_list[0]] =benefit_list[1:]
d[in_network_list[0]] =in_network_list[1:]
d[out_of_network_list[0]] =out_of_network_list[1:]
df = pd.DataFrame.from_dict(d, orient='index')       
df=df.transpose()
df.to_csv(r"C:\Users\user\Desktop\New folder\test.csv")

