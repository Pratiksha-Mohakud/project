# IMPORTING NECESSARY METHODS FROM CLASS 

from flask import Blueprint, request, render_template, url_for,redirect,flash
from app import db
from .models import Employee

main=Blueprint('main',__name__) # creating a blueprint

# BASIC PAGE FUNCTIONALITIES 

# creating routes to handle different requests

@main.route('/')
def home():
    return render_template('base.html')  # redirecting to base.html file which renders the home page

# VERIFYING TO AVOID DUPLICATE ENTRIES

@main.route('/verify')
def verify():
    return render_template('verify.html')

@main.route('/verify',methods=['POST'])
def verify_post():
    id=request.form["id"]

    user=Employee.query.filter_by(id=id).first()  # checks if the entry is already present or not
    if user:
        print("User already exists") 
        return redirect(url_for("main.home"))
    return redirect(url_for("main.Add_employee"))
    


# **IMPLEMENTING CRUD OPERATIONS**

# C--- CREATING

# creating two different routes to add employees for clarity <1> For GET request <2> For POST request

@main.route('/create')
def Add_employee():
    return render_template('create_emp.html') # renders the html template to create new employee entry 

@main.route('/create', methods=['POST'])
def Add_employee_post():
# getting the values of different fields of database from the form 
    id=request.form["id"]
    name=request.form["name"]
    age=request.form["age"]
    department=request.form["department"]

# adding the entry to the database and commiting
    new_employee=Employee(id=id,name=name,age=age,department=department)
    db.session.add(new_employee)
    db.session.commit()
    flash("Employee added successfully!")
    return redirect(url_for("main.profile"))

# ---------------------------------------------------------------

# R--> READING

@main.route('/display')
def display_all():
    return render_template("display_all",employees=Employee.query.all())

@main.route('/logout')
def logout():
    return redirect(url_for("main.home"))


# ----------------------------------------------------------------------


# U--> UPDATE

@main.route('/update', methods=['GET','POST'])
def update_employee(emp_id):  # getting the id to be updated by post method
    employee = Employee.query.get_or_404(emp_id)  
    if request.method == "POST":
        Employee.name = request.form['pushups']
        Employee.age = request.form['age']
        Employee.department=request.form['department']
        db.session.commit() # updating then commiting the change in database
        flash('Your post has been updated!')
        return redirect(url_for('main.display_all'))

    return render_template('update.html', employee=employee)



# ---------------------------------------------------------------------------


# D--> DELETE

@main.route('/delete', methods=['GET','POST'])
def delete(emp_id):
    employee=Employee.query.get_or_404(emp_id)
    db.session.delete(employee) # deleting the record of employee
    db.session.commit()
    flash('Your post has been deleted!')
    return redirect(url_for('main.display_all'))

    
