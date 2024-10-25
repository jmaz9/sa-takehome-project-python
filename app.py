import os
import stripe
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

# Load environment variables from the .env file
load_dotenv()

# Temporary print to confirm environment variable loading
print("Stripe Secret Key:", os.getenv('STRIPE_SECRET_KEY'))
print("Stripe Publishable Key:", os.getenv('STRIPE_PUBLISHABLE_KEY'))

# Set up your Stripe API key
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

app = Flask(__name__,
            static_url_path='',
            template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "views"),
            static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "public"))

# Home route
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Checkout route
@app.route('/checkout', methods=['GET'])
def checkout():
    item = request.args.get('item')
    title = None
    amount = None
    error = None

    if item == '1':
        title = 'The Art of Doing Science and Engineering'
        amount = 2300
    elif item == '2':
        title = 'The Making of Prince of Persia: Journals 1985-1993'
        amount = 2500
    elif item == '3':
        title = 'Working in Public: The Making and Maintenance of Open Source'
        amount = 2800
    else:
        error = 'No item selected'

    # Get the publishable key from the environment variable
    publishable_key = os.getenv('STRIPE_PUBLISHABLE_KEY')

    # Pass publishable_key to the template
    return render_template('checkout.html', title=title, amount=amount, error=error, publishable_key=publishable_key)

# Create a Payment Intent
@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    try:
        data = request.get_json()  # Get the amount from the frontend
        amount = data['amount']    # Amount in cents

        # Create a Payment Intent with the amount
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
        )

        # Send the client secret to the frontend
        return jsonify({'clientSecret': intent['client_secret']})
    except Exception as e:
        return jsonify(error=str(e)), 403

# Success route
@app.route('/success', methods=['GET'])
@app.route('/success', methods=['GET'])
def success():
    # Get the amount and payment_intent from the query parameters
    amount = request.args.get('amount')
    payment_intent = request.args.get('payment_intent')

    # Pass these details to the success template
    return render_template('success.html', amount=amount, payment_intent=payment_intent)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
