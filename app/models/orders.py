from migrations.config import db

class Orders(db.Model):
    __tablename__ = 'Orders'

    OrderID = db.Column(db.Integer, primary_key=True)
    OrderCode = db.Column(db.String(30), nullable=False)
    CreateDate = db.Column(db.DateTime, nullable=False)
    SalesChannel = db.Column(db.String(100), nullable=False)
    Status = db.Column(db.String(100), nullable=False)
    CustomerID = db.Column(db.Integer, db.ForeignKey('Customer.CustomerID'), nullable=False)
    EmployeeID = db.Column(db.Integer, db.ForeignKey('Employee.EmployeeID'), nullable=False)
    
    def to_dict(self):
        return {
            'OrderID': self.OrderID,
            'OrderCode': self.OrderCode,
            'CreateDate': self.CreateDate,
            'SalesChannel': self.SalesChannel,
            'Status': self.Status,
            'CustomerID': self.CustomerID,
            'EmployeeID': self.EmployeeID
        }