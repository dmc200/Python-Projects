def file_copy_content(file_one, file_two, content, path):
    # Create and Open file1 in write mode. 
    file1 = open(path + "\\" + str(file_one), 'w')
    #Split Content by spaces and pass each into list. 
    content = content.split()
    print(content)
    # write each item in list to file1. 
    for x in content:
        file1.write(str(x) + ' ')

    # Close file 1. 
    file1.close()

    # Create and Open file2 in write mode. 
    file2 = open(path + "\\" + str(file_two), 'w')

    # Re-Open file1 in read mode.
    file1 = open(path + "\\" + str(file_one), 'r')

    # Read the contents of file1 again into a list object. 
    file1Lines = file1.readlines()

    # Write the contents of file1 onto file2
    for x in file1Lines:
        file2.write(str(x))
    # Close file2
    file2.close()



file_copy_content('file_test11.txt', 'file_test22.txt', "Isn't this one really cool message! 123", 'C:\\Users\\dchrie504\\Desktop\\')
