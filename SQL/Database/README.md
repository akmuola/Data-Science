# Databases-and-SQL-for-Data-Science-with-Python

A database is a repository of data that provides functionality for adding, modifying, and querying the data. (A database is a logically coherent collection of data with some inherent meaning). SQL is a language used to query or retrieve data from a relational database. 

The Relational Model is the most used data model for databases because it allows for data independence. 

The primary key of a relational table uniquely identifies each tuple or row, preventing duplication of data and providing a way of defining relationships between tables. 

SQL statements fall into two different categories: Data Definition Language (DDL) statements and Data Manipulation Language (DML) statements.


In this lab, you will use MySQL. MySQL is a Relational Database Management System (RDBMS) designed to efficiently store, manipulate, and retrieve data

You can use the WHERE clause to refine your query results.

You can use the wildcard character (%) as a substitute for unknown characters in a pattern.

You can use BETWEEN ... AND ... to specify a range of numbers.

You can sort query results into ascending or descending order, using the ORDER BY clause to specify the column to sort on.

You can group query results by using the GROUP BY clause. 

Functions, Multiple Tables, and Sub-queries

Most databases come with built-in functions that you can use in SQL statements to perform operations on data within the database itself.

When you work with large datasets, you may save time by using built-in functions rather than first retrieving the data into your application and then executing functions on the retrieved data.

You can use sub-queries to form more powerful queries than otherwise.

You can use a sub-select expression to evaluate some built-in aggregate functions like the average function. 

Derived tables or table expressions are sub-queries where the outer query uses the results of the sub-query as a data source.

You can access a database from a language like Python by using the appropriate API. Examples include ibm_db API for IBM DB2, psycopg2 for ProstgreSQL, and dblib API for SQL Server.

DB-API is Python's standard API for accessing relational databases. It allows you to write a single program that works with multiple kinds of relational databases instead of writing a separate program for each one.

The DB_API  connect constructor creates a connection to the database and returns a Connection Object, which is then used by the various connection methods.

The connection methods are:
The cursor() method, which returns a new cursor object using the connection.
The commit() method, which is used to commit any pending transaction to the database.
The rollback() method, which causes the database to roll-back to the start of any pending transaction.
The close() method, which is used to close a database connection. 

You can use SQL Magic commands to execute queries more easily from Jupyter Notebooks. 
Magic commands have the general format %sql select * from tablename.
Cell magics start with a double %% (percent) sign and apply to the entire cell.
Line magics start with a single % (percent) sign and apply to a particular line in a cell.
