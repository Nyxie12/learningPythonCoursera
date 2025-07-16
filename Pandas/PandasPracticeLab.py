import pandas as pd

# Practice 1
x = {'Name': ['Rose', 'John', 'Jane', 'Mary'],
     'ID': [1, 2, 3, 4],
     'Department': ['Architect Group', 'Software Group', 'Design Team',
                    'Infrastructure'],
     'Salary': [100000, 80000, 50000, 60000]}

df = pd.DataFrame(x)
print(df)
#
# # Print the entire DataFrame
# print(df)
#
# # Print out just the ID's from the DF
# x = df[["ID"]]
# print(x)
#
# print(type(x))
# print(df.loc[0, 'Salary'])

# EXERCISE 1
# x = {
#     'Student': ['David', 'Samuel', 'Terry', 'Evan'],
#     'Age': [27, 24, 22, 32],
#     'Country': ['UK', 'Canada', 'China', 'USA'],
#     'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development'],
#     'Marks': [85, 72, 89, 76]
# }
#
# df = pd.DataFrame(x)
#
# b = df[['Marks']]
# print(b)
#
# c = df[['Country','Course']]
# print(c)
#
# x = df['Student']
# print(x)
# print(type(x))

# Practice 2
df2 = df
df2 = df2.set_index('Name')
# print(df2.head())
#
# print(df2.loc['Jane', 'Salary'])

# Exercise 2
print(df2.loc['Jane', 'Department'])
print(df2.iloc[3, 2])