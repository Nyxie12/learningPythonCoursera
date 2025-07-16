import requests
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

async def download(url, filename):
    reponse = requests.get(url)
    if reponse.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(reponse.content)

download(filename, 'Product-sales.csv')
df = pd.read_csv('Product-sales.csv')

