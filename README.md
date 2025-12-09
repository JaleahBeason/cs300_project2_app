=== CS300 Project 2 – Mall Database Application ===
=== Jaleah Beason
CS300 – Database Systems
Fall 2025 ===

This project implements a relational database and a Python application that performs CRUD operations and executes stored procedures for managing a shopping mall system. It uses MySQL, SQL stored procedures, and a Python command-line application built with mysql-connector-python.

===Project Contents ===
cs300_project2_app/
│
├── app.py                      # Main application with menu + DB operations
├── db.py                       # MySQL connection helper
├── CS300_Project1_schema.sql   # Database table definitions (DDL)
├── CS300_Project2_data.sql     # Data population script (INSERTs)
└── CS300_Project2_procedures.sql  # Stored procedures

===Database Setup Instructions ===
=== 1. Create the database 

Open MySQL Workbench and run:

CREATE DATABASE cs300_project2;
USE cs300_project2;

=== 2. Run the schema file

Load and execute:

CS300_Project1_schema.sql


This creates the tables:

Shopping_Mall

Retailer

Shop

Maintenance_Event

Income_Record

=== 3. Insert sample data

Run:

CS300_Project2_data.sql


This populates the database with example malls, retailers, shops, maintenance events, and income records.

=== 4. Create stored procedures

Run:

CS300_Project2_procedures.sql


This adds all required stored procedures for Project 2.

=== Application Setup (Python) ===
=== 1. Install required library
python -m pip install mysql-connector-python


(or python3, depending on your system)

=== 2. Update database credentials

Open db.py and make sure your MySQL username/password match your Workbench login:

conn = mysql.connector.connect(
    host="localhost",
    user="root",               # or your MySQL user
    password="YOUR_PASSWORD",
    database="cs300_project2"
)

=== 3. Run the app
cd cs300_project2_app
python app.py

=== Program Menu Features ===

When running app.py, you will see:

===== CS300 Project 2 – Mall DB App =====
1. Add Shop
2. Delete Shop
3. Update Shop Rent
4. Get Shop Total Income (SP)
5. Get Shops in Mall (SP)
6. Add Maintenance Event (SP)
7. Get Mall Income Summary (SP)
8. Get Average Discount for Mall (SP)
0. Exit

CRUD Operations (Requirement Met)

Add Shop

Delete Shop (only possible when foreign keys allow)

Update Shop Rent

Stored Procedures (Requirement Met)

The app calls five stored procedures:

GetShopTotalIncome(IN, OUT)

GetShopsInMall(IN)

AddMaintenanceEvent(IN, IN, IN, IN)

GetMallIncomeSummary()

GetAverageDiscountForMall(IN, OUT)

These procedures include:

IN parameters

OUT parameters

JOINs

INSERTs executed via stored procedure

=== How to Test the Features ===
=== Stored Procedure Example
Enter choice: 4
Shop ID: 101
Total income for shop 101: 68000.00

=== Add → Update → Delete a Shop

Add Shop → ID 300

Update Shop 300 Rent

Delete Shop 300

All three operations should succeed and demonstrate required CRUD functionality.
