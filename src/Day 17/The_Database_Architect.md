**Query**



sqlite3 internship.db

.database



**SQL Data Definition (DDL)**



create table interns(id INTEGER, name TEXT, track TEXT, stipend INTEGER);



**SQL Data Manipulation (DML)**



insert into interns values(101,'Adithya G','Data Science',30000),(102,'Dhanush H','Data Science',25000);

insert into interns values(201,'Kumar','Web Development',33000),(301,'Havyas B','Robotics',15000);

insert into interns values(103,'Dilan B','Data Science',29000);



**SQL Data Query (DQL)**



select name,track from interns;

select \* from interns;

