CREATE DATABASE LaundryManagement;
GO
USE LaundryManagement;
GO

CREATE TABLE Product (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductCode VARCHAR(30) UNIQUE,
    ProductName NVARCHAR(255),
    Brand VARCHAR(10) DEFAULT NULL,
    Price DECIMAL(10,2),
    Unit NVARCHAR(20)
);

CREATE TABLE Employee (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
    EmployeeCode VARCHAR(20) NOT NULL UNIQUE,
    FullName NVARCHAR(50) NOT NULL,
    Sex CHAR(1) CHECK (Sex IN ('F','M')) DEFAULT 'F',
    PhoneNumber VARCHAR(10) CHECK (PhoneNumber NOT LIKE '%[^0-9]%'),
    Address NVARCHAR(255)
);

CREATE TABLE Customer (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerCode VARCHAR(30) UNIQUE,
    FullName NVARCHAR(255),
    ShortName NVARCHAR(50),
    DeliveryAddress NVARCHAR(255),
    OfficeAddress NVARCHAR(255)
);

CREATE TABLE Department (
    DepartmentID INT IDENTITY(1,1) PRIMARY KEY,
    DepartmentCode VARCHAR(50),
    FullName NVARCHAR(255),
    CustomerID INT,
    CONSTRAINT fk_department_customer FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE Orders (
    OrderID INT IDENTITY (1,1) PRIMARY KEY,
    OrderCode VARCHAR(30) NULL,
    CreateDate DATETIME DEFAULT GETDATE(),
    SalesChannel NVARCHAR(100),
    Status NVARCHAR (100),
    EmployeeID INT,
    CustomerID INT,
    CONSTRAINT fk_order_employee FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
    CONSTRAINT fk_order_customer FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE OrderDetails (
    OrderDetailID INT IDENTITY(1,1) PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    CONSTRAINT fk_orderdetails_order FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    CONSTRAINT fk_orderdetails_product FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

CREATE TABLE Invoice (
    InvoiceID INT IDENTITY(1,1) PRIMARY KEY,
    InvoiceCode VARCHAR(20) NULL UNIQUE,
    InvoiceDate DATETIME DEFAULT GETDATE(),
    EmployeeID INT,
    CustomerID INT,
    CONSTRAINT fk_invoice_employee FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
    CONSTRAINT fk_invoice_customer FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE InvoiceDetail (
    InvoiceDetailID INT IDENTITY(1,1) PRIMARY KEY,
    Quantity DECIMAL(10,2) DEFAULT 0,
    DiscountPercent DECIMAL(5,2) DEFAULT 0,
    DiscountAmount DECIMAL(10,2) DEFAULT 0,
    SalePrice DECIMAL(10,2),
    InvoiceID INT,
    ProductID INT,
    CONSTRAINT fk_invoicedetail_invoice FOREIGN KEY (InvoiceID) REFERENCES Invoice(InvoiceID),
    CONSTRAINT fk_invoicedetail_product FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

CREATE TABLE Recipient (
    RecipientID INT IDENTITY(1,1) PRIMARY KEY,
    RecipientName NVARCHAR(50) NULL,
    RecipientPhone VARCHAR(10) NULL,
    DeliveryAddress NVARCHAR(255) NULL,
    CustomerID INT,
    CONSTRAINT fk_recipient_customer FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE Delivery (
    DeliveryID INT IDENTITY(1,1) PRIMARY KEY,
    Service NVARCHAR(100),
    Weight DECIMAL(10,2),
    Length DECIMAL(10,2),
    Width DECIMAL(10,2),
    Height DECIMAL(10,2),
    ShippingStatus NVARCHAR(50),
    Note NVARCHAR(255),
    InvoiceID INT,
    RecipientID INT,
    CONSTRAINT fk_delivery_invoice FOREIGN KEY (InvoiceID) REFERENCES Invoice(InvoiceID),
    CONSTRAINT fk_delivery_recipient FOREIGN KEY (RecipientID) REFERENCES Recipient(RecipientID)
);

CREATE TABLE Account (
    AccountID INT IDENTITY(1,1) PRIMARY KEY,
    PhoneNumber VARCHAR(10),
    Password VARCHAR(255),
    Role NVARCHAR(20), 
    Status NVARCHAR(50) DEFAULT N'Active',
    EmployeeID INT NULL,
    CONSTRAINT fk_account_employee FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

CREATE TABLE Payment (
    PaymentID INT IDENTITY(1,1) PRIMARY KEY,
    InvoiceID INT NOT NULL,
    PaymentMethod NVARCHAR(20) CHECK (PaymentMethod IN (N'Tiền mặt', N'Thẻ', N'Chuyển khoản', N'Ví điện tử')),
    Amount DECIMAL(10,2),
    CONSTRAINT fk_payment_invoice FOREIGN KEY (InvoiceID) REFERENCES Invoice(InvoiceID)
);

GO
CREATE TRIGGER trg_OrderCode
ON Orders
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH cte AS (
        SELECT 
            o.OrderID,
            ROW_NUMBER() OVER (
                PARTITION BY CAST(GETDATE() AS DATE)
                ORDER BY o.OrderID
            ) AS rn
        FROM Orders o
        INNER JOIN inserted i ON o.OrderID = i.OrderID
    )
    UPDATE o
    SET OrderCode = 'DH' 
                    + CONVERT(VARCHAR(8), GETDATE(), 112) 
                    + RIGHT('000' + CAST(c.rn AS VARCHAR(3)), 3)
    FROM Orders o
    INNER JOIN cte c ON o.OrderID = c.OrderID;
END
GO

CREATE TRIGGER trg_InvoiceCode
ON Invoice
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH cte AS (
        SELECT 
            inv.InvoiceID,
            ROW_NUMBER() OVER (
                PARTITION BY CAST(GETDATE() AS DATE)
                ORDER BY inv.InvoiceID
            ) AS rn
        FROM Invoice inv
        INNER JOIN inserted i ON inv.InvoiceID = i.InvoiceID
    )
    UPDATE inv
    SET InvoiceCode = 'HD' 
                      + CONVERT(VARCHAR(8), GETDATE(), 112) 
                      + RIGHT('000' + CAST(c.rn AS VARCHAR(3)), 3)
    FROM Invoice inv
    INNER JOIN cte c ON inv.InvoiceID = c.InvoiceID;
END
GO

INSERT INTO Product (ProductCode, ProductName, Brand, Price, Unit)
VALUES
('NVU07',N'Đồ NV điều dưỡng nữ mẫu 2024','NVU',573,'gr'),
('NVU02',N'Đồ NV - Điều dưỡng (trắng)','NVU',420,'gr');

INSERT INTO Employee (EmployeeCode, FullName, Sex, PhoneNumber, Address) 
VALUES
('NV001', N'Nguyễn Bích Tuyền', 'F', '0987654321', N'123 Lê Lợi, Ninh Kiều, Cần Thơ'),
('NV002', N'Trần Văn Bình', 'M', '0912345678', N'45 Trần Hưng Đạo, Ninh Kiều, Cần Thơ'),
('NV003', N'Lê Thị Mai', 'F', '0978123456', N'78 Nguyễn Trãi, Cái Răng, Cần Thơ'),
('NV004', N'Phạm Văn Hùng', 'M', '0909876543', N'12 Hai Bà Trưng, Ninh Kiều, Cần Thơ'),
('NV005', N'Hoàng Thị Lan', 'F', '0934567890', N'56 Lý Thường Kiệt, Ô Môn, Cần Thơ'),
('NV006', N'Đặng Văn Dũng', 'M', '0945678901', N'89 Nguyễn Văn Cừ, Ninh Kiều, Cần Thơ'),
('NV007', N'Võ Thị Hoa', 'F', '0923456789', N'34 Pham Ngũ Lão, Ninh Kiều, Cần Thơ');

INSERT INTO Customer (CustomerCode, FullName, ShortName, DeliveryAddress, OfficeAddress)
VALUES 
('THAMREN',N'RENTOKIL INITIAL (VIỆT NAM)','THAM REN',N'Khu dân cư Hưng Phú',N'Số 54 - 56, Nguyễn Trãi, Quận 1, TP.HCM'),
('WINK_CT',N'KHÁCH SẠN WINK BẾN NINH KIỀU','WINK',N'14 Phan Đình Phùng, Ninh Kiều, Cần Thơ',N'14 Phan Đình Phùng, Tân An, Ninh Kiều, Cần Thơ'),
('SOJO_CT',N'KHÁCH SẠN TNH CẦN THƠ','SOJO-CT',N'112 Trần Phú, Cái Khế, Ninh Kiều, Cần Thơ',N'112 Trần Phú, Cái Khế, Ninh Kiều, Cần Thơ'),
('SOJO_HG',N'QUẢN LÝ KHÁCH SẠN TNH','SOJO-HG',N'16A Nguyễn Công Trứ, Vị Thanh, Hậu Giang',N'54A Nguyễn Chí Thanh, Đống Đa, Hà Nội'),
('CHARTMAN',N'KHÁCH SẠN SÀI GÒN CẦN THƠ - Chartman','CHARTMAN',N'45 Ngô Quyền, Ninh Kiều, Cần Thơ',N'1 Đại lộ Hòa Bình, Ninh Kiều, Cần Thơ'),
('COSMO_BL',N'KHÁCH SẠN COSMO','COSMO',N'31A Trần Phú, Bạc Liêu',N'31A Trần Phú, TP Bạc Liêu, Bạc Liêu'),
('KP_HOTEL',N'XUẤT NHẬP KHẨU PHÚC THÀNH (KP HOTEL)','KP HOTEL',N'9 Nam Kỳ Khởi Nghĩa, Ninh Kiều, Cần Thơ',N'9-13-15B Nam Kỳ Khởi Nghĩa, Ninh Kiều, Cần Thơ'),
('BV_SADEC',N'PHÚC AN PHÁT - SA ĐÉC','BV SADEC',N'153 Nguyễn Sinh Sắc, Sa Đéc, Đồng Tháp',N'SA ĐÉC'),
('BV_PC_SADEC',N'PHÚC AN PHÁT - PHƯƠNG CHÂU SA ĐÉC','BV PC SADEC',N'153 Nguyễn Sinh Sắc, Sa Đéc, Đồng Tháp',N'SA ĐÉC'),
('ECOLODGE_CT',N'DL NGHỈ DƯỠNG SINH THÁI CẦN THƠ','ECOLODGE',N'542 Khu vực 3, Ba Láng, Cái Răng, Cần Thơ',N'542 Khu vực 3, Ba Láng, Cái Răng, Cần Thơ'),
('ECORESORT_CT',N'CN CÔNG TIẾN - Ecoresort','ECO RESORT',N'QL61C, Nhơn Thuận, Nhơn Nghĩa, Phong Điền, Cần Thơ',N'KM7+, QL61C, Nhơn Ái, Cần Thơ'),
('BV_HMCL',N'BỆNH VIỆN HOÀN MỸ CỬU LONG','BV HMCL',N'Võ Nguyên Giáp (Quang Trung)',N'Lô 20, Võ Nguyên Giáp, Phú Thứ, Cái Răng, Cần Thơ'),
('HQA',N'CTY HOA QUỲNH ANH','XUONG HQA',N'Cầu Ba Láng',N''),
('BUNNY',N'TIỆM BUNNY','BUNNY',N'170B3 Nguyễn Văn Cừ',N'');

INSERT INTO Department (DepartmentCode, FullName, CustomerID) VALUES
('HM.111','Phòng 111',2),
('HM01_HSTSSĐ','HSTCCĐ',2),
('HM.010-011','Phòng 010-011',2);

INSERT INTO Account (PhoneNumber, Password, Role, Status, EmployeeID)
VALUES
('0987654321', 'tuyen@2024', N'Manager', N'Active', 1),
('0912345678', 'binh@2024', N'Employee', N'Active', 2),
('0978123456', 'mai@2024', N'Employee', N'Active', 3),
('0909876543', 'hung@2024', N'Employee', N'Active', 4),
('0934567890', 'lan@2024', N'Employee', N'Active', 5),
('0945678901', 'dung@2024', N'Employee', N'Active', 6),
('0923456789', 'hoa@2024', N'Employee', N'Active', 7);

INSERT INTO Orders (CreateDate, SalesChannel, Status, EmployeeID, CustomerID)
VALUES
('2025-09-17 14:33:00', N'Bán trực tiếp', N'Phiếu tạm', 1,2);
INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES 
(1,1,6),
(1,2,1);

INSERT INTO Invoice (InvoiceDate, EmployeeID, CustomerID)
VALUES ('2025-09-18 14:34:09', 1, 2);

INSERT INTO InvoiceDetail (Quantity, DiscountPercent, DiscountAmount, SalePrice, InvoiceID, ProductID)
VALUES
(6, 0, 0, 573, 1, 1),
(1, 0, 0, 420, 1, 2);


INSERT INTO Recipient (RecipientName, RecipientPhone, DeliveryAddress, CustomerID)
VALUES 
(N'Lê Văn Khang',NULL,NULL,1);

INSERT INTO Delivery (Service, Weight, Length, Width, Height, ShippingStatus, Note, InvoiceID, RecipientID)
VALUES (N'', 0, 0, 0, 0, NULL, N'27 cục = 30kg', 1, 1);

INSERT INTO Payment (InvoiceID, PaymentMethod, Amount)
VALUES
(1, N'Tiền mặt', 0);

SELECT * FROM Customer
SELECT * FROM Employee
SELECT * FROM Orders
SELECT * FROM Invoice



SELECT 
    i.InvoiceCode,
    pr.ProductName,
    id.Quantity,
    id.SalePrice,
    id.DiscountPercent,
    id.DiscountAmount,
    (id.Quantity * id.SalePrice - id.DiscountAmount) AS LineTotal
FROM Invoice i
JOIN InvoiceDetail id ON id.InvoiceID = i.InvoiceID
JOIN Product pr ON id.ProductID = pr.ProductID
ORDER BY i.InvoiceID, pr.ProductName;

/*
-- Tắt FK
EXEC sp_msforeachtable "ALTER TABLE ? NOCHECK CONSTRAINT ALL";

-- Xóa dữ liệu
DELETE FROM Payment;
DELETE FROM Delivery;
DELETE FROM InvoiceDetail;
DELETE FROM Invoice;
DELETE FROM OrderDetails;
DELETE FROM Orders;
DELETE FROM Account;
DELETE FROM Recipient;
DELETE FROM Department;
DELETE FROM Employee;
DELETE FROM Product;
DELETE FROM Customer;

-- Reset Identity
DBCC CHECKIDENT('Payment', RESEED, 0);
DBCC CHECKIDENT('Delivery', RESEED, 0);
DBCC CHECKIDENT('InvoiceDetail', RESEED, 0);
DBCC CHECKIDENT('Invoice', RESEED, 0);
DBCC CHECKIDENT('OrderDetails', RESEED, 0);
DBCC CHECKIDENT('Orders', RESEED, 0);
DBCC CHECKIDENT('Account', RESEED, 0);
DBCC CHECKIDENT('Recipient', RESEED, 0);
DBCC CHECKIDENT('Department', RESEED, 0);
DBCC CHECKIDENT('Employee', RESEED, 0);
DBCC CHECKIDENT('Product', RESEED, 0);
DBCC CHECKIDENT('Customer', RESEED, 0);

-- Bật lại FK
EXEC sp_msforeachtable "ALTER TABLE ? WITH CHECK CHECK CONSTRAINT ALL";
*/
