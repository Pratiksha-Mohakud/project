# project

This is an Employee management project created that could perform basic CRUD functionalities i.e CREATE, READ, UPDATE and DELETE
completely based on

-PYTHON 
-FLASK framework
-SQLALCHEMY used as ORM
-HTML 

The project structure is like this

employee_management/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── config.py
│
├── templates/
│
├── run.py
│
└── requirements.txt


init file-- for initialization of the methods installed 
config-- for the setting up configuration of the sqlalchemy installed and other os related functionalities
models-- to describe the required properties of the database to be created like the columns name, type of values etc.
routes-- contains all the routes used in the project to handle different requests
templates-- contains all the html files required 

There are 4 buttons in the home page 

VERIFY- To add new employee first the user needs to verify that the entry is not duplicate. 

DISPLAY- To display data of all employees

UPDATE- To update existing records

DELETE- For deletion of records


--THE ROUTES--


Two routes are used to implement both verify and create routes to ensure clarity
1. With GET request
2. With POST request 


'/' --      This is the route displays the home page by rendering base.html page

'/verify'-- To verify entries 
'/verify', methods=['POST'] -- Handles post request of verify route. It is done by rendering verify.html which takes the id to be added and checks if it is present in database or not. If not then redirects to create route, if found duplicate redirects to home page.

'/create'-- To create new entry. It renders create.html and takes values from the user like form
'/create', methods=['POST'] --  The values returned by the create route are handled by this route with post method. It commits the values to the database

'/display'-- To display all entries

'/update' --  First takes input the id that is to be updated then renders the file update.html that takes updated values using a form. Then commits the changes to the database

'/delete' --  Gets the id to be deleted then deletes and commits it to the database






