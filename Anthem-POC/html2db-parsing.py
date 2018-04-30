import re
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

url = r"C:\Users\user\Desktop\New folder\t.html" 
page = open(url)
bs = BeautifulSoup(page.read(),'html.parser')
#print(bs.prettify())
for link in bs.find_all('a'):    
    if(link.get('href')!= None):
            if(str(link.contents[0]).find("Benefits/Coverage (What is Covered)") != -1):
                href_to_search=link.get('href')
            if(str(link.contents[0]).find("Section 8. Limitations/Exclusions (What is Not Covered)") != -1):
            	  href_to_stop_before = link.get('href')  
print(href_to_search)
href_to_stop_before = href_to_stop_before.replace("#","")
number = int(re.findall(r"\d+",href_to_search)[0])
href_init_string = str(re.findall(r"[A-Za-z_]+",href_to_search)[0])

article_starting_number=number + 1
article_ending_number = article_starting_number + 1

starting_id = href_init_string + str(article_starting_number)
ending_id = href_init_string + str(article_ending_number)


init_div = bs.find(id=starting_id)

para_data = ""
heading = ""
count = 0
benefits={}
while(ending_id!= href_to_stop_before):
    while(init_div != bs.find(id=ending_id)):
        
        init_div = init_div.next
    
        if(init_div.string == None):
            continue
        if(count==0):        
            heading = str(init_div.string)
            count += 1    
        else:
            para_data +=  init_div.string
            init_div  = init_div.next
            para_data += "\n"
    benefits[heading]=para_data
    para_data = ""
    count=0
    article_starting_number += 1  
    article_ending_number =article_starting_number + 1      
    starting_id = href_init_string + str(article_starting_number)
    init_div = bs.find(id=starting_id)
    ending_id = href_init_string + str(article_ending_number)
mydatabase = client['mydb']
mydatabase.benefit_table.insert(benefits,check_keys=False)    



