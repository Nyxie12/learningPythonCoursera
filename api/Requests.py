import requests
import os
from PIL import Image
from IPython.display import IFrame
#
# url='https://www.ibm.com/'
# r=requests.get(url)
#
# print(r.status_code)
# print(r.request.headers)
# print('Request body: ', r.request.body)
#
# header = r.headers
# print(r.headers)
# print(header['Date'])
# print(header['Content-Type'])
# print(r.encoding)
# print(r.text[0:100])

# Exercise
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path = os.path.join(os.getcwd(), 'example1.txt')
r = requests.get(url)
with open(path, 'wb') as f:
    f.write(r.content)
