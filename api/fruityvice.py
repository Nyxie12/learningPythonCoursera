import pandas as pd
import requests
import json

data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")
results = json.load()

pd.DataFrame(results)

print(results)
