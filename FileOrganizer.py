import os, shutil

def File_Organizer(workingDir):
    os.chdir('c:\\users\\dchrie504\\Downloads_2')
    #walk through all files and folders to get unique filetypes.
    l_Files = os.walk('c:\\users\\dchrie504\\Downloads_2')
    fileTypes = []
    for walk in l_Files:
        for file in walk[-1]:
            fileTypes.append(file.split('.')[-1])
    #make all items lowercase to create distinct values
    fileTypes = [x.lower() for x in fileTypes]

    #get rid of duplicate filetypes by creating set then back to list. 
    fileTypes = set(fileTypes)
    fileTypes = list(fileTypes)
    # create a folder for each unique filetype. 
    for ft in fileTypes:
        os.mkdir(os.getcwd() + '\\' + ft)
    fileWalk = os.walk('c:\\users\\dchrie504\\Downloads_2')
    
    #Trying to move files to their respective fileType folder.
    for folder, sub, files in os.walk('c:\\users\\dchrie504\\Downloads_2'):
	for file in files:
			for fileType in fileTypes:
				if file.endswith('.' + fileType):
					shutil.move((os.getcwd() + '\\' + file), (os.getcwd() + '\\' + fileType))

    '''
    for fileType in fileTypes:
        for walk in fileWalk:
            for file in walk[-1]:
                if file.endswith('.' + fileType):
			print(file)
			'''

                            
            
    
    
        
    
