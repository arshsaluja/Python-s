"""
Reading files.
"""

print("Opening Files")
print("=============")

# Open takes a filename and a mode
openfile = open("the_idiot.txt", "rt")

# Modes for reading:
#  r - read (default)
#  t - text (default)
#  b - binary

print(type(openfile))
print(openfile)
# Must close file after opening it
openfile.close()

