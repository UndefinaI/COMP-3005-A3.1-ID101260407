# COMP 3005 A3.1
 Assignment 3 Question 1 of COMP3005

Author: Thomas Roche


Dependencies: 
This project uses psycopg3 to work. From the command line:
	pip install psycopg3


Setup:

From /database; 
- enter Database_creation.sql and change the user from postgre to your user
- run the scripts in the following order: Database_creation.sql, Table_creation.sql, Initial_data.sql

From /application;
- change the constants at the top of the file in application.py


Using the application:
Run the application from the command line or using your IDE. 
The usage is simple; it's text based input with clear instructions. It gives near-direct access to the functions.



Function Breakdown:
Each function uses sql calls via the cursor to interface with the database. All follow the same basic format: the function first enters a try/except to catch errors and, if an error occurs, it prints what it is. It then executes some sql with cursor.execute("..."). It then informs the user of the results, and commits those results if changes were made. 


Demonstration video:
	https://youtu.be/V8EMY7nk0XI











