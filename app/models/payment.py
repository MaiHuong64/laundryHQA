from migrations.config import db

class Payment(db.Model):
    __tablename__ = 'Payment'

    PaymentID = db.Column(db.Integer, primary_key=True)
    InvoiceID = db.Column(db.Integer, db.ForeignKey('Invoice.InvoiceID'), nullable=False)
    PaymentMethod = db.Column(db.String(50), nullable=False)
    Amount = db.Column(db.Decimal(10, 2), nullable=False)
   

    def to_dict(self):
        return {
            'PaymentID': self.PaymentID,
            'PaymentMethod': self.PaymentMethod,
            'Amount': self.Amount,
            'InvoiceID': self.InvoiceID
        }