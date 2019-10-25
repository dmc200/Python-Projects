def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me at 155-555-1245 tomorrow, or at 113-123-1222 at my office line'

foundNumber = False

chunk = ''

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("phone number found: " + str(chunk))
        foundNumber = True
if not foundNumber:
    print("Could not find any phone numbers")
    

