from bs4 import BeautifulSoup
import requests

# html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
# soup = BeautifulSoup(html, 'html.parser')
#
# print(soup.prettify())
#
# tag_object = soup.title
# print('tag object', tag_object)
# tag_object = soup.h3
# print(tag_object)
# tag_child = tag_object.b
# print(tag_child)
# tag_parent = tag_child.parent
# print(tag_parent)
#
# L_Salary = tag_object.next_sibling
# print(L_Salary)
# Steph = L_Salary.next_sibling
# print(Steph)
# S_Salary = Steph.next_sibling
# print(S_Salary)


table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, 'html.parser')

table_rows = table_bs.find_all('tr')
print(table_rows)

first_row = table_rows[0]
print(first_row)
print(first_row.td)

for i, row in enumerate(table_rows):
    print('row', i, 'is', row)