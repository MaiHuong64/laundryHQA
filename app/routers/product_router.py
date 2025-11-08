from flask import Blueprint, request, jsonify, render_template
from models.product import Product
from migrations.config import db
from sqlalchemy import or_

product_router = Blueprint('product_router', __name__)

@product_router.route('/', methods=['GET'])
def get_products():
    try:
        all_products = Product.query.all()
        return jsonify([product.to_dict() for product in all_products])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@product_router.route('/<int:id>', methods=['GET'])
def get_product_by_id(id):
    product = Product.query.get(ProductID=id)
    if product:
        return jsonify(product.to_dict())
    return jsonify({'error': 'Product not found'}), 404

@product_router.route('/create', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        ProductName=data['ProductName'],
        Brand=data.get('Brand'),
        Price=data['Price'],
        Unit=data.get('Unit')
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

@product_router.route('/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(ProductID=id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

@product_router.route('/update/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json(silent=True)
    product = Product.query.get(ProductID=id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    product.ProductName = data.get('ProductName', product.ProductName)
    product.Brand = data.get('Brand', product.Brand)
    product.Price = data.get('Price', product.Price)
    product.Unit = data.get('Unit', product.Unit)

    db.session.commit()
    return jsonify(product.to_dict())
@product_router.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('q', '')
    results = Product.query.filter(
        or_(
            Product.ProductCode.ilike(f'%{query}%'),
            Product.ProductName.ilike(f'%{query}%'),
            Product.Brand.ilike(f'%{query}%')
        )
    ).all()
    if not results:
        return jsonify({'message': 'No products found matching the query.'}), 404
    return jsonify([product.to_dict() for product in results])
