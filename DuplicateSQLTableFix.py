import pyodbc, time, sys, os

'''
def get_db_info():
	db_name = input("Please provide the db name you want to access: ").lower()
	table_name = input("Please provide the table name you want to access: ").lower()
	return db_name, table_name


# Defined Functions and actions preformed. 
def read(cnxn, table_name, db_name):
    print("Reading . . .")
    cursor = cnxn.cursor()
    cursor.execute("select top 10 * from " + str(db_name) + ".dbo." + str(table_name))
    for row in cursor:
        print(f'row= {row}')
        print("\n")

def get_total_count(cnxn, table_name, db_name):
    total = ''
    print(f"Performing count(*) on {table_name}. . .")
    cursor = cnxn.cursor()
    cursor.execute("select count(*) from " + str(db_name) + ".dbo." + str(table_name))
    for x in cursor:
        print(f'{x[0]}')
'''



def delete_duplicates(cnxn, table_name, db_name):
	# Steps in order to delete duplicates. 
	sql_total_count ='select count(*) from ' + str(db_name) + '.dbo.' + str(table_name)
	sql_distinct_count = 'select count(*) from (select distinct * from ' + str(db_name) + '.dbo.' + str(table_name) + ') d'
	sql_bk_table = 'select * into ' + str(db_name) + '.dbo.' + str(table_name) + backup_date + " from " + str(db_name) + '.dbo.' + str(table_name)
	sql_truncate = 'truncate table ' + str(db_name) + '.dbo.' + str(table_name)
	sql_insert_distinct = "insert into " + str(db_name) + '.dbo.' + str(table_name) +  ' select distinct * from ' + str(db_name) + '.dbo.' + str(table_name) + backup_date
	sql_drop_bkp = "drop table " + database + "dbo." + str(table_name) + backup_date
	
	
	cursor = cnxn.cursor()
	# Fetch data that I need from fetchall() function. 
	cursor.execute(sql_total_count)
	sql_total_count = cursor.fetchall()[0][0]
	cursor.execute(sql_distinct_count)
	sql_distinct_count = cursor.fetchall()[0][0]

	# Remove Duplicates 
	if int(sql_distinct_count) < int(sql_total_count):
		print(f"{table_name} has duplicates. . .")
		print(f'removing now . . .')
		time.sleep(3)
		cursor.execute(sql_bk_table)
		cursor.execute(sql_truncate)
		cursor.execute(sql_insert_distinct)
		cursor.execute(sql_drop_bkp)
		cursor.commit()
		print('Duplicates removed for: ' + str(table_name))
		 
	elif int(sql_total_count) == int(sql_distinct_count):
		print(f"There are no duplicate records in target table {table_name}.")

	cursor.commit()




# change this to your local dir for file 
os.chdir('c:\\users\\dchrie504\\desktop')

f = open('dups.txt', 'r')

trans_content = f.readlines()
trans_content = [x.strip() for x in trans_content]

#Setup Connection Info. (Temporarily Hard Coded.)
server = '' 
database = '' 
username = '' 
password = ''
backup_date = ''


cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=database, user=username, password=password)

#db_name, table_name = get_db_info()
# get_total_count(cnxn, table_name, db_name)
# read(cnxn, table_name, db_name)

for x in trans_content: 
	delete_duplicates(cnxn, str(x), 'ADH_STAGE_QA')


    
cnxn.close()
