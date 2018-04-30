import mammoth
from bs4 import BeautifulSoup
with open(r"C:\Users\user.A713DCOK\Desktop\New folder\Anthem.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value # The generated HTML
    messages = result.messages # Any messages, such as warnings during conversion
f = open(r"C:\Users\user.A713DCOK\Desktop\New folder\t.html","w")
f.write(html)

bs = BeautifulSoup(html,'html.parser')
print(bs.prettify())
for link in bs.find_all('a'):
    if(link.get('href')!= None):
            if(link.contents[0] == "Durable Medical Equipment and Medical Devices, Orthotics, Prosthetics, and Medical and SurgicalSupplies	58"):
                href_to_search=link.get('href')
print(href_to_search)
href=href_to_search.replace("#","")
print(href)
div = bs.find(id=href)
div.parent
p = div.parent

p.next.next.next.next.next.next
div = bs.find(id=href+1)
