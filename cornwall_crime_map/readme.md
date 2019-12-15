## Project Overview
Carry out data analysis on a police crime dataset.  From the data analysis prouduce a series of coordinates representing monthly crimes in Corwall.  These coords are then used with Google Maps api to allow a crime scene data map to be produced in the browser.

## Project Steps
Below are the steps taken to complete each component of this project.

### Modeling Apache Cassandra database
- Design tables to answer the queries outlined in the [project template](https://github.com/riched158/UdacityDataEngineering/blob/master/datamodelling/project2/Project_1B_%20Project_Template.ipynb) &nbsp;
- Write Apache Cassandra CREATE KEYSPACE and SET KEYSPACE statements
- Develop CREATE statement for each of the tables to address each question
- Load the data with INSERT statement for each of the tables
- Include IF NOT EXISTS clauses in your CREATE statements to create tables only if the tables do not already exist.
- Test by running the proper select statements with the correct WHERE clause

### Build ETL Pipeline
- Implement the logic in section Part I of the notebook template to iterate through each event file in event_data to process and create a new CSV file in Python
- Make necessary edits to Part II of the notebook template to include Apache Cassandra CREATE and INSERT statements to load processed records into relevant tables in your data model
- Test by running SELECT statements after running the queries on your database

