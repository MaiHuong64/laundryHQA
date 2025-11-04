from migrations.config import db

class OrderDetails(db.Model):
    __tablename__ = 'OrderDetails'

    OrderDetailID = db.Column(db.Integer, primary_key=True)
    OrderID = db.Column(db.Integer, db.ForeignKey('Orders.OrderID'), nullable=False)
    ProductID = db.Column(db.Integer, db.ForeignKey('Product.ProductID'), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<OrderDetails {self.OrderDetailID} - Order {self.OrderID}: Product {self.ProductID}, Quantity {self.Quantity}, UnitPrice {self.SalePrice}>"