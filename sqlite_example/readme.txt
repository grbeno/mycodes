	*** sqlite_example/sqlite_example.py ***

	We have a data table (my_table.csv) with columns [ 'Id', my_id, 'my_value'->(float) ] 
	The goal is counting means based on values ('my_value') having the same custom id ('my_id')
	The key concepts are: /count/, /group_by/  
	

	* Python libraries you need to import:
	 
	- you need to download & install with pip or something like that: 
		o sqlite3, csv, reportlab
	
	** Functions:
	
	- csvin
		o args: fname <- name of the csv file to read
		o reading the rows of the csv table to a list of tuples (data)
	- csvout
		o args: fname <- name of the csv file to write
		o writing the results to the csv file 'avg.csv'

	** Algorithm:
	
	1. create database & connect to
	2. check if data table exists 
		-> yes: ignore, no: create
			* with this checking we can avoid error msgs when trying to run the code more than one time!
	3. read input csv file to list
	4. create table
	5. insert into the content of the list(3.) to table created in (4.)
	6. get the means of the 'my_value' with the same 'my_id' /group_by/
		* /count/ is the sum of the numbers the main value consists of
	7. fetch the sql query then insert header in the 0. row
	8. writing results/fetched data to csv file -> 'avg.csv'
	9. create pdf to draw a result table in that
	10. set parameters with the aim of ordering objects in pdf page
	11. close the database

 

	
		
		

