import numpy as np
import pandas as pd
import ssl

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

# Disable SSL certificate verification globally
ssl._create_default_https_context = ssl._create_unverified_context

URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
tables = pd.read_html(URL)
df = tables[3]

df.columns = range(df.shape[1])

df = df[[0,2]]