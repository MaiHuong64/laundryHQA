from flask import Blueprint, request, jsonify
from models.customer import Customer
from migrations.config import db
from sqlalchemy import or_

customer_router = Blueprint('customer_router', __name__)

@customer_router.route('/', methods=['GET'])
def get_customers():
    try:
        all_customer = Customer.query.all()
        return jsonify([cus.to_dict() for cus in all_customer])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customer_router.route('/<int:id>', methods=['GET'])
def get_customer_by_id(id):
    cus = Customer.query.get(id)
    if cus:
        return jsonify(cus.to_dict())
    return jsonify({'error': 'Product not found'}), 404

@customer_router.route('/create', methods=['POST'])
def handle_customer():
        data = request.get_json()
        try:
            new_customer = Customer(
                CustomerCode=data['CustomerCode'],
                FullName=data['FullName'],
                ShortName=data.get('ShortName'),
                DeliveryAddress=data['DeliveryAddress'],
                OfficeAddress=data.get('OfficeAddress')
            )
            db.session.add(new_customer)
            db.session.commit()
            return jsonify(new_customer.to_dict()), 201
        except Exception as e:
            db.session.rollback();
            return jsonify({'error': str(e)}), 400


@customer_router.route('/delete/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get(id)
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted successfully'})

@customer_router.route('/update/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.get_json(silent=False)
    customer = Customer.query.get(id)
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    
    customer.FullName = data.get('FullName', customer.FullName)
    customer.ShortName = data.get('ShortName', customer.ShortName)
    customer.DeliveryAddress = data.get('DeliveryAddress', customer.DeliveryAddress)
    customer.OfficeAddress = data.get('OfficeAddress', customer.OfficeAddress)

    db.session.commit()
    return jsonify(customer.to_dict())
@customer_router.route('/search', methods=['GET'])
def search_customer():
    query = request.args.get('q', '')
    results = Customer.query.filter(
        or_(
            Customer.CustomerCode.ilike(f'%{query}%'),
            Customer.FullName.ilike(f'%{query}%'),
            Customer.ShortName.ilike(f'%{query}%')
        )
    ).all()
    if not results:
        return jsonify({'message': 'No customer found matching the query.'}), 404
    return jsonify([product.to_dict() for product in results])
