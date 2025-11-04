from migrations.config import db

class Recipient(db.Model):
    __tablename__ = 'Recipient'

    RecipientID = db.Column(db.Integer, primary_key=True)
    RecipientName = db.Column(db.String(50), nullable=False)
    RecipientPhone = db.Column(db.String(10), nullable=False)
    DeliveryAddress = db.Column(db.String(255), nullable=False)
    CustomerID = db.Column(db.Integer, db.ForeignKey('Customer.CustomerID'), nullable=False)

    def to_dict(self):
        return {
            'RecipientID': self.RecipientID,
            'RecipientName': self.RecipientName,
            'RecipientPhone': self.RecipientPhone,
            'DeliveryAddress': self.DeliveryAddress,
            'CustomerID': self.CustomerID
        }