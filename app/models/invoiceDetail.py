from migrations.config import db

class InvoiceDetail(db.Model):
    __tablename__ = 'InvoiceDetail'

    InvoiceDetailID = db.Column(db.Integer, primary_key=True)
    Quantity = db.Column(db.Integer, nullable=False)
    DiscoutpPercent = db.Column(db.Decimal(5,2), nullable=False)
    DiscountAmount = db.Column(db.Decimal(10,2), nullable=False)
    SalePrice = db.Column(db.Decimal(10,2), nullable=False)
    InvoiceID = db.Column(db.Integer, db.ForeignKey('Invoice.InvoiceID'), nullable=False)
    ProductID = db.Column(db.Integer, db.ForeignKey('Product.ProductID'), nullable=False)

    def __repr__(self):
        return f"<InvoiceDetail {self.InvoiceDetailID} - Invoice {self.InvoiceID}: Product {self.ProductID}, Quantity {self.Quantity}, SalePrice {self.SalePrice}>"