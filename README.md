Stripe Payment Integration Project
Overview
This project is a simple e-commerce application built with Flask. It allows users to select a book, proceed to checkout, and complete a purchase using Stripe for payment processing. The application displays a confirmation page with the total amount and Stripe Payment Intent ID upon successful payment.
1. How to Build, Configure, and Run the Application
Prerequisites
Python 3.7+
Flask: Installed as a dependency

Setup Instructions
Clone the Repository:
git clone <repository-url>
cd <project-directory>


Install Dependencies:
pip install -r requirements.txt

Configure Environment Variables: 
Create a .env file in the project root directory with your Stripe API keys:

STRIPE_SECRET_KEY=sk_test_your_secret_key_here
STRIPE_PUBLISHABLE_KEY=pk_test_your_publishable_key_here


Run the Application:
Start the Flask development server:
python -m flask run

Open your browser and go to http://127.0.0.1:5000/.
2. How the Solution Works
Stripe APIs Used
Stripe Payment Intent API: This API is used to create a PaymentIntent on the server side with a specified amount and currency, and it returns a clientSecret used to confirm the payment on the client side.
Application Architecture
The project is organised as follows:
app.py: Main Flask application file that handles routes and integrates the Stripe API.
Templates (views): Contains HTML templates (index.html, checkout.html, success.html) for rendering pages.
Public Assets (public): Holds static assets like CSS and JavaScript.
Environment Configuration: .env file for securely storing Stripe API keys.
Workflow
Homepage (index.html): Users can select a book to purchase.
Checkout Page (checkout.html): Displays the selected book and total price, integrates Stripe Elements for secure payment input.
Payment Confirmation: The application creates a PaymentIntent on the server side and confirms it with the Stripe API. On success, it redirects to a success page.
Success Page (success.html): Displays the total amount and Payment Intent ID, confirming the purchase.
3. Approach, Resources, and Challenges
Approach
Initial Setup: Set up the Flask server, environment variables, and Stripe configuration.
Frontend-Backend Integration: Integrate Stripe Elements on the frontend and the Payment Intent API on the backend to securely process payments.
Error Handling and Testing: Used Stripe's test cards to simulate different payment outcomes.
Resources and Documentation
Stripe API Documentation
Stripe Elements Documentation
Flask Documentation
Challenges and Solutions
Environment Variables: Ensuring .env variables were loaded correctly by Flask was a minor challenge that required additional verification with print statements.
Error Handling for Payments: Testing different scenarios (e.g., declined cards, 3D Secure authentication) highlighted the importance of handling errors gracefully in the frontend code.
4. Potential Extensions for a More Robust Application
If extending this application, I would consider the following features:
User Authentication: Allow users to create accounts, view order history, and save payment information.
Product Catalog: Expand the application to support multiple product types and integrate a database for managing products.
Order Management: Add an order management system for both customers and administrators.
Additional Payment Methods: Integrate support for additional payment methods through Stripe, such as Apple Pay or Google Pay, to enhance user experience.

