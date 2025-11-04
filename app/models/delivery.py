from migrations.config import db

class delivery(db.Model):
    __tablename__ = 'Delivery'

    DeliveryID = db.Column(db.Integer, primary_key=True)
    Service = db.Column(db.String(255), nullable=False)
    Weight = db.Column(db.Decimal(10, 2), nullable=False)
    Length = db.Column(db.Decimal(10, 2), nullable=False)
    Width = db.Column(db.Decimal(10, 2), nullable=False)
    Height = db.Column(db.Decimal(10, 2), nullable=False)
    ShippingStatus = db.Column(db.String(50), nullable=False)
    Note = db.Column(db.String(255), nullable=True)
    InvoiceID = db.Column(db.Integer, db.ForeignKey('Invoice.InvoiceID'), nullable=False)
    RecipientID = db.Column(db.Integer, db.ForeignKey('Recipient.RecipientID'), nullable=False)
    def to_dict(self):
        return {
            'DeliveryID': self.DeliveryID,
            'Service': self.Service,
            'Weight': str(self.Weight),
            'Length': str(self.Length),
            'Width': str(self.Width),
            'Height': str(self.Height),
            'ShippingStatus': self.ShippingStatus,
            'Note': self.Note,
            'InvoiceID': self.InvoiceID,
            'ReceipientID': self.ReceipientID
        }