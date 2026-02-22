import requests

genes = """
BRD4
EIF4G1
GANAB
ITGA3
LMNA
MBOAT7
NSD2
PTPRF
SLC2A1
SMARCA4
STAT2
WDR1
"""

# submit gene list
add_url = 'https://maayanlab.cloud/Enrichr/addList'
payload = {'list': (None, genes)}
response = requests.post(add_url, files=payload)
data = response.json()
user_list_id = data['userListId']

# query TF libraries
libraries = ["ChEA_2022","ENCODE_TF_ChIP-seq_2015","TRRUST_Transcription_Factors_2019"]

for lib in libraries:
    url = f"https://maayanlab.cloud/Enrichr/enrich?userListId={user_list_id}&backgroundType={lib}"
    res = requests.get(url).json()

    with open(f"TF_enrichment_{lib}.txt","w") as f:
        for row in res[lib][:20]:
            f.write(str(row)+"\n")

print("TF enrichment downloaded")
