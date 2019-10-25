import os

os.chdir("c:\\users\\dchrie504\\Desktop")

for filename in os.listdir():
    if filename.endswith(".txt"):
        print(filename)
    else:
        continue

    
