-- CS300 Project 1 — Ready-to-Run MySQL DDL
-- Implements explicit M:N between Retailer and Shopping_Mall via Retailer_Mall junction table.

-- Shopping Mall Table
CREATE TABLE Shopping_Mall (
    Mall_ID INT NOT NULL PRIMARY KEY,
    Mall_Name VARCHAR(100) NOT NULL,
    Location VARCHAR(100),
    Opening_Date DATE
);

-- Retailer Table
CREATE TABLE Retailer (
    Retailer_ID INT NOT NULL PRIMARY KEY,
    Retailer_Name VARCHAR(100) NOT NULL,
    Discount_Rate DECIMAL(5,2)
);

-- Shop Table (Associative Entity for Retailer ↔ Mall)
CREATE TABLE Shop (
    Shop_ID INT NOT NULL PRIMARY KEY,
    Mall_ID INT NOT NULL,
    Retailer_ID INT NOT NULL,
    Shop_Name VARCHAR(100) NOT NULL,
    Floor_Space INT,
    Rent_Amount DECIMAL(10,2),
    Percent_Sales DECIMAL(5,2),
    FOREIGN KEY (Mall_ID) REFERENCES Shopping_Mall(Mall_ID),
    FOREIGN KEY (Retailer_ID) REFERENCES Retailer(Retailer_ID)
);

-- Maintenance Event Table
CREATE TABLE Maintenance_Event (
    Maintenance_ID INT NOT NULL PRIMARY KEY,
    Shop_ID INT NOT NULL,
    Event_Date DATE NOT NULL,
    Cost DECIMAL(10,2) NOT NULL,
    Type ENUM('Scheduled', 'Unscheduled') NOT NULL,
    FOREIGN KEY (Shop_ID) REFERENCES Shop(Shop_ID)
);

-- Income Record Table (Enforces one record per shop per date)
CREATE TABLE Income_Record (
    Record_ID INT NOT NULL PRIMARY KEY,
    Shop_ID INT NOT NULL,
    Date DATE NOT NULL,
    Rent_Income DECIMAL(10,2) NOT NULL,
    Sales_Revenue DECIMAL(10,2) NOT NULL,
    Total_Income DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (Shop_ID) REFERENCES Shop(Shop_ID),
    CONSTRAINT uq_income_shop_date UNIQUE (Shop_ID, Date)
);
