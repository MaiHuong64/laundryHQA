from migrations.config import db

class Customer(db.Model):
    __tablename__ = 'Customer'

    CustomerID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CustomerCode = db.Column(db.String(30), unique=True, nullable=False)
    FullName = db.Column(db.String(255),nullable=False)
    ShortName = db.Column(db.String(50), nullable=False)
    DeliveryAddress = db.Column(db.String(255), nullable=True)
    OfficeAddress = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            'CustomerID': self.CustomerID,
            'CustomerCode': self.CustomerCode,
            'FullName': self.FullName,
            'ShortName': self.ShortName,
            'DeliveryAddress': self.DeliveryAddress,
            'OfficeAddress': self.OfficeAddress
        }