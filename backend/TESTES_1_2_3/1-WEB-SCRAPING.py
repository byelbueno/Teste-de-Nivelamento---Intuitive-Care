import requests
from bs4 import BeautifulSoup
import os
import zipfile


url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

pdf_links = []
for link in soup.find_all('a', href=True):
    if ('Anexo I' in link.text or 'Anexo II' in link.text) and link['href'].endswith('.pdf'):
        pdf_links.append(link['href'])

if len(pdf_links) >= 2:
    pdf_links = pdf_links[:2]

os.makedirs("downloads", exist_ok=True)  
pdf_names = ["Anexo_I.pdf", "Anexo_II.pdf"] 

for url, name in zip(pdf_links, pdf_names):
    response = requests.get(url)
    with open(f"downloads/{name}", 'wb') as file:
        file.write(response.content)

zip_filename = "Anexos.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for name in pdf_names:
        zipf.write(f"downloads/{name}", arcname=name)

print(f"PDFs renomeados e compactados em {zip_filename}")
''