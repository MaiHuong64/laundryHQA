from migrations.config import db

class Product(db.Model):
    __tablename__ = 'Product'

    ProductID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ProductCode = db.Column(db.String(30), unique=True, nullable=False)
    ProductName = db.Column(db.String(255), nullable=False)
    Brand = db.Column(db.String(10), nullable=True)
    Price = db.Column(db.Float, nullable=False)
    Unit = db.Column(db.String(20), nullable=True)
    def to_dict(self):
        return {
            'ProductID': self.ProductID,
            'ProductCode': self.ProductCode,
            'ProductName': self.ProductName,
            'Brand': self.Brand,
            'Price': self.Price,
            'Unit': self.Unit
        }