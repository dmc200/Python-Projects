#This program will organize files in a folder (recursively) to folders with the files respective file extension.

 for folderName, subfolders, files in os.walk('c:\\users\\dchrie504\\Downloads_2'):
	for file in files:
		if file.endswith('.txt'):
			if not os.path.exists("c:\\users\\dchrie504\\Downloads_2\\text"):
				os.mkdir("c:\\users\\dchrie504\\Downloads_2\\txt")
				shutil.move(file, "c:\\users\\dchrie504\\Downloads_2\\txt")
			else:
				shutil.move(file, "c:\\users\\dchrie504\\Downloads_2\\txt")
		elif file.endswith('.scala'):
			if not os.path.exists('c:\\users\\dchrie504\\Downloads_2\\scala'):
				os.mkdir('c:\\users\\dchrie504\\Downloads_2\\scala')
				shutil.move(file, "c:\\users\\dchrie504\\Downloads_2\\scala")
			else:
				shutil.move(file, "c:\\users\\dchrie504\\Downloads_2\\scala")
		elif file.endswith('.pdf'):
			if not os.path.exists('c:\\users\\dchrie504\\Downloads_2\\pdf'):
				os.mkdir('c:\\users\\dchrie504\\Downloads_2\\pdf')
				shutil.move(file, "c:\\users\\dchrie504\\Downloads_2\\pdf")
			else:
				shutil.move(file, "c:\\users\\dchrie504\\Downloads_2\\pdf")
		elif file.endswith('.zip'):
			if not os.path.exists('c:\\users\\dchrie504\\Downloads_2\\zip'):
				os.mkdir('c:\\users\\dchrie504\\Downloads_2\\zip')
				shutil.move(file, "c:\\users\\dchrie504\\Downloads_2\\zip")
			else:
				shutil.move(file, "c:\\users\\dchrie504\\Downloads_2\\zip")
		elif file.endswith('.jar'):
			if not os.path.exists('c:\\users\\dchrie504\\Downloads_2\\jar'):
				os.mkdir('c:\\users\\dchrie504\\Downloads_2\\jar')
				shutil.move(file, "c:\\users\\dchrie504\\Downloads_2\\jar")
			else:
				shutil.move(file, "c:\\users\\dchrie504\\Downloads_2\\jar")

