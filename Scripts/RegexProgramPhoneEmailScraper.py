#! python3
import re, pyperclip

#  Create Regex Object for Phone Numbers.
phoneRegex = re.compile(r'''
# 415-555-000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x
(
((\d\d\d)|(\(\d\d\d\)))?   # area code (optional)
(\s|-)                     # first separator
\d\d\d                     # first three digits
-                          # separator
\d\d\d\d                   # last 4 digits
(((ext(\.)?\s)|x)          # extension word-part (optional)
 (\d{2,5}))?               # extension number part (Also optional)
)
''',re.VERBOSE)

# Create Regex Object for Email Addresses. 
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-Z0-9.+_]+            # name part
@                          #@ symbol
[a-zA-Z0-9.+_]+            # domain name part. 

''',re.VERBOSE)
# Get the text oof the clipboard.
text = pyperclip.paste()

# Extract the email/phone from this text.
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

phoneNumbers = []

for phone in extractedPhone:
    phoneNumbers.append(phone[0])

results = '\n'.join(phoneNumbers) + "\n" + "\n".join(extractedEmail)




# TODO: Copy the extracted email/phone to the clipboard.

pyperclip.copy(results)
