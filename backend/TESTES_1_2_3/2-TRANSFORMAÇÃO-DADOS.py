import pdfplumber
import pandas as pd
import zipfile

pdf_path = "downloads/Anexo_I.pdf"

data = []
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                if any(cell.strip() for cell in row):  
                    data.append([cell.strip() if cell else "" for cell in row])

if len(data) > 1:
    df = pd.DataFrame(data[1:], columns=data[0]) 
else:  
    df = pd.DataFrame(data)

substituicoes_od = {
    "OD": "Seg. Odontológica"
}
substituicoes_amb = {
    "AMB": "Seg. Ambulatorial"
}

if 'OD' in df.columns:
    df['OD'] = df['OD'].replace(substituicoes_od)
if 'AMB' in df.columns:
    df['AMB'] = df['AMB'].replace(substituicoes_amb)

csv_filename = "Rol_Procedimentos.csv"
df.to_csv(csv_filename, index=False)

zip_filename = f"Teste_Gabryel.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write(csv_filename, arcname=csv_filename)

print(f"Dados transformados e compactados em {zip_filename}")
