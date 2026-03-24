import requests
import pandas as pd

genes = [
"BRD4","EIF4G1","GANAB","ITGA3","LMNA","MBOAT7",
"NSD2","PTPRF","SLC2A1","SMARCA4","STAT2","WDR1"
]

string_api_url = "https://string-db.org/api"
output_format = "tsv-no-header"
method = "network"

request_url = "/".join([string_api_url, output_format, method])

params = {
    "identifiers": "%0d".join(genes),
    "species": 9606,
    "required_score": 400
}

response = requests.post(request_url, data=params)

with open("string_network.tsv", "w") as f:
    f.write(response.text)

print("STRING network downloaded")
