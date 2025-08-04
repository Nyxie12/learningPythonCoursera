import pandas as pd
import requests
import pandas
import json

url = requests.get('https://official-joke-api.appspot.com/jokes/ten')

data = json.loads(url.text)

df = pd.DataFrame(data)
df.drop(columns=['type','id'], inplace=True)
print(df)


