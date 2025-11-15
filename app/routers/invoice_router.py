from flask import Blueprint, request, jsonify
from models.customer import Custmomer
from migrations.config import db
from sqlalchemy import or_

customer_router = Blueprint('customer_router', __name__)

@customer_router.route('/', methods=['GET'])
def get_products():
    try:
        all_customer = Custmomer.query.all()
        return jsonify([cus.to_dict() for cus in all_customer])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customer_router.route('/<int:id>', methods=['GET'])
def get_product_by_id(id):
    product = Custmomer.query.get(id)
    if product:
        return jsonify(product.to_dict())
    return jsonify({'error': 'Product not found'}), 404

@customer_router.route('/create', methods=['POST'])
def handle_products():
        data = request.get_json()
        try:
            new_product = Custmomer(
                ProductCode=data['ProductCode'],
                ProductName=data['ProductName'],
                Brand=data.get('Brand'),
                Price=data['Price'],
                Unit=data.get('Unit')
            )
            db.session.add(new_product)
            db.session.commit()
            return jsonify(new_product.to_dict()), 201
        except Exception as e:
            db.session.rollback();
            return jsonify({'error': str(e)}), 400


@customer_router.route('/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Custmomer.query.get(id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

@customer_router.route('/update/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json(silent=False)
    product = Custmomer.query.get(id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    product.ProductName = data.get('ProductName', product.ProductName)
    product.Brand = data.get('Brand', product.Brand)
    product.Price = data.get('Price', product.Price)
    product.Unit = data.get('Unit', product.Unit)

    db.session.commit()
    return jsonify(product.to_dict())
@customer_router.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('q', '')
    results = Custmomer.query.filter(
        or_(
            Custmomer.ProductCode.ilike(f'%{query}%'),
            Custmomer.ProductName.ilike(f'%{query}%'),
            Custmomer.Brand.ilike(f'%{query}%')
        )
    ).all()
    if not results:
        return jsonify({'message': 'No products found matching the query.'}), 404
    return jsonify([product.to_dict() for product in results])
