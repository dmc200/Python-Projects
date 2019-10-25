import re, os
os.chdir(r'C:\\Users\\dchrie504\\Desktop\\New folder\\')
pass_regex = re.compile(r'password',  re.IGNORECASE)

for folder, sub, files in os.walk(os.getcwd()):
    for file in files: 
        f = open(file, 'r')
        file_content = f.readlines()
        for x in file_content:
            if pass_regex.search(x):
                print(str(file) + ' ' + str(x))
                
