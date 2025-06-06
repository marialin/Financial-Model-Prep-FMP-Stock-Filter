from flask import Blueprint, request, jsonify
import stripe

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/create-checkout-session', methods=['POST'])
def create_checkout():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Premium Access',
                    },
                    'unit_amount': 1000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:5000/dashboard',
            cancel_url='http://localhost:5000/',
        )
        return jsonify({ 'url': checkout_session.url })
    except Exception as e:
        return jsonify(error=str(e)), 403
