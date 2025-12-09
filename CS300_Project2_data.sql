USE cs300_project2;
-- Sample Malls
INSERT INTO Shopping_Mall (Mall_ID, Mall_Name,Location,Opening_Date) VALUES
(1, 'Riverfront Mall', 'Louisville, KY', '2010-05-01'),
(2, 'Summit Plaza',   'Lexington, KY', '2015-09-15');
-- Sample Retailers
INSERT INTO Retailer (Retailer_ID, Retailer_Name, Discount_Rate) VALUES
(1, 'Tech World',   5.00),
(2, 'Broadway Fashion', 10.00),
(3, 'Cookie Bites', 0.00);
-- Sample Shops
INSERT INTO Shop (
 Shop_ID, Mall_ID, Retailer_ID,
    Shop_Name, Floor_Space, Rent_Amount, Percent_Sales
    ) VALUES
(101, 1, 1, 'Tech World - Riverfront', 2000, 5000.00, 7.50),
(102, 1, 2, 'Broadway Fashion - Riverfront', 1500, 4500.00, 8.00),
(201, 2, 3, 'Cookie Bites - Summit',   1200, 4000.00, 6.50);
-- Sample Maintence Events
INSERT INTO Maintenance_Event ( 
	Maintenance_ID, Shop_ID, Event_Date, Cost, Type
) VALUES
(1, 101, '2025-01-10', 400.00, 'Scheduled'),
(2, 101, '2025-02-20', 250.00, 'Unscheduled'),
(3, 102, '2025-01-05', 500.00, 'Scheduled');
-- Sample Income Records
INSERT INTO Income_Record (
 Record_ID, Shop_ID, Date,
    Rent_Income, Sales_Revenue, Total_Income
) VALUES
(1, 101, '2025-01-01', 5000.00, 30000.00, 35000.00),
(2, 101, '2025-02-01', 5000.00, 28000.00, 33000.00),
(3, 102, '2025-01-01', 4500.00, 20000.00, 24500.00),
(4, 201, '2025-01-01', 4000.00, 15000.00, 19000.00);