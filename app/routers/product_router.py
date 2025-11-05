from flask import Blueprint, request, jsonify, render_template
from models.product import Product
from migrations.config import db

product_router = Blueprint('product_router', __name__)

@product_router.route('/', methods=['GET'])
def get_all_products():
    all_products = Product.query.all()
    return render_template('product.html', products=all_products)

@product_router.route('/<int:id>', methods=['GET'])
def get_product_by_id(id):
    product = Product.query.get(ProductID=id)
    if not product:
        return render_template('product.html', products=[],error='Product not found'), 404
    return render_template('product.html', products=[product])

@product_router.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        ProductCode=data['ProductCode'],
        ProductName=data['ProductName'],
        Brand=data.get('Brand'),
        Price=data['Price'],
        Unit=data.get('Unit')
    )
    db.session.add(new_product)
    db.session.commit()
    return render_template('product.html', products=[new_product]), 201

@product_router.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(ProductID=id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return render_template('product.html', products=[]), 204

@product_router.route('/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json(silent=True)
    product = Product.query.get(ProductID=id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    product.ProductCode = data.get('ProductCode', product.ProductCode)
    product.ProductName = data.get('ProductName', product.ProductName)
    product.Brand = data.get('Brand', product.Brand)
    product.Price = data.get('Price', product.Price)
    product.Unit = data.get('Unit', product.Unit)

    db.session.commit()
    return render_template('product.html', products=[product])

@product_router.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('q', '')
    results = Product.query.filter(Product.ProductName.ilike(f'%{query}%')).all()
    if not results:
       return render_template('product.html', products=[], error='No products found matching the query'), 404
    return render_template('product.html', products=results)
