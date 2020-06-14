openfile = open("gonewiththewind.txt", "rt")

filedata = openfile.read()
print(filedata)
#read-returns the entire contents of the file as a string

#never forget to close the file
openfile.close()
