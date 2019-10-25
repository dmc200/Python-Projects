Connect to the database

Get a list of all effected tables prcs_id's and store in list

loop over list with prcs_ids:

	find max_id of table and store in variable

	check if prcs_status = "C" where job_id = variable

		if yes, update to 'R' where job_id = var

	reset current 

