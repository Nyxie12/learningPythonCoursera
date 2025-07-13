# Writes to file, if it does not exist in directory it will make one
# with open('example1.txt', 'w') as file:
#     file.write('This is line A')

# Reads the file
# with open('example1.txt', 'r') as file:
#     print(file.read())

# Takes from an array and writes to a txt file
# Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
# with open('lines.txt', 'w') as lineFile:
#     for line in Lines:
#         lineFile.write(line)

# with open('lines.txt', 'a+') as testWriteFile:
#     print("Initial Location: {}".format(testWriteFile.tell()))
#
#     data = testWriteFile.read()
#     if (not data):  # if empty
#         print("Read Nothing")
#     else:
#         print(testWriteFile.read())
#
#     testWriteFile.seek(0, 0)  # moves 0 bytes from the beginning
#
#     print("New Location: {}".format(testWriteFile.tell()))
#     data = testWriteFile.read()
#     if (not data):
#         print('Read nothing')
#     else:
#         print(data)
#
#     print("Location after read: {}".format(testWriteFile.tell()))
#

# with open('lines.txt', 'r+') as testwritefile:
#     testwritefile.seek(0,0) #write at beginning of file
#     testwritefile.write("Line 1" + "\n")
#     testwritefile.write("Line 2" + "\n")
#     testwritefile.write("Line 3" + "\n")
#     testwritefile.write("Line 4" + "\n")
#     testwritefile.write("finished\n")
#     testwritefile.seek(0,0)
#     print(testwritefile.read())

with open('lines.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())