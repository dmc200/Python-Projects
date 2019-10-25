import re

message = 'Call me at 155-555-1245 tomorrow, or at 113-123-1222 at my office line'

#specity the pattern.
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

#search the message string and return a "Match Object" in this case mo
#findall() retruns a list of all matches

print(phoneNumRegex.findall('Call me at 155-555-1245 tomorrow, or at 113-123-1222 at my office line'))

#Print out the result using print and group()

#print(mo.group())
