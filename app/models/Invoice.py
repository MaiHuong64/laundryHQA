from migrations.config import db

class Invoice(db.Model):
    __tablename__ = 'Invoice'

    InvoiceID = db.Column(db.Integer, primary_key=True)
    InvoiceCode = db.Column(db.String(20), nullable=False)
    InvoiceDate = db.Column(db.DateTime, nullable=False)
    EmployeeID = db.Column(db.Integer, db.ForeignKey('Employee.EmployeeID'), nullable=False)
    CustomerID = db.Column(db.Integer, db.ForeignKey('Customer.CustomerID'), nullable=False)
    
    def to_dict(self):
        return {
            'InvoiceID': self.InvoiceID,
            'InvoiceCode': self.InvoiceCode,
            'InvoiceDate': self.InvoiceDate,
            'EmployeeID': self.EmployeeID,
            'CustomerID': self.CustomerID
        }