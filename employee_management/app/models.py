from app import db  # IMPORTING THE db OBJECT FROM APP   

class Employee(db.Model): 
    
# DEFINING THE VARIOUS PROPERTIES WE WANT IN OUR DATABASE EMPLOYEE

    id=db.Column(db.Integer,primary_key=True)  # ID IS SET AS THE PRIMARY KEY i.e EACH ENTRY WILL HAVE AN UNIQUE ID
    name=db.Column(db.String(100), nullable=False)
    age=db.Column(db.Integer, nullable=False)
    department=db.Column(db.String(100), nullable=False)


def __repr__(self):
        return f'<Employee{self.name}>'
