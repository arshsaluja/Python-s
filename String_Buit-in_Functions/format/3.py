name1 = "Pierre"
age1 = 7
name2 = "May"
age2 = 13

line1 = "{0:^7} {1:>3}".format(name1, age1)
line2 = "{0:^7} {1:>3}".format(name2, age2)
"""
 The format specifiers after the colon include a number.
 This number is the width of the field in the output.
 The output will contain exactly that many characters for that field (padded with spaces), 
 regardless of how wide the argument is. In this example the width is preceded by a symbol 
 which indicates how the field should be aligned:< for left aligned,> for right aligned, and 
 ^ for centered.
 """
print(line1)
print(line2)
