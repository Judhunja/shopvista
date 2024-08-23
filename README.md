
## ShopVista

ShopVista is a Flask-based e-commerce application that allows users to browse products, add them to their cart, and complete purchases. The app features user authentication, product management, a shopping cart, and payment integration using Stripe.
#### Features

   - User Authentication: Secure signup, login, and logout functionalities.
   - Product Browsing: Users can view and search for products by category.
   - Shopping Cart: Add, view, and remove items from the cart.
   - Checkout Process: Complete purchases with a checkout page and integrated payment via Stripe.
   - Order Management: Orders are stored in the database after successful payment.

### Installation
#### Prerequisites

   - Python 3.x
   - Flask
   - MySQL
   - Stripe API Key

### Setup

   #### Clone the Repository:

      git clone https://github.com/yourusername/shopvista.git

      cd shopvista

##### Create a Virtual Environment:

      python3 -m venv venv
      source venv/bin/activate

##### Install Dependencies:

      pip install -r requirements.txt

#### Configure Environment Variables:

Create a .env file in the root directory and add the following:

      FLASK_APP=run.py
      FLASK_ENV=development
      SECRET_KEY=your_secret_key
      SQLALCHEMY_DATABASE_URI=mysql+pymysql://username:password@localhost/shopvista
      STRIPE_SECRET_KEY=your_stripe_secret_key``

#### Initialize the Database:


      flask db init
      flask db migrate
      flask db upgrade

##### Populate the Database:

Run the populate_commodities.py script to add initial data:


      python test_data/populate_commodities.py

#### Run the Application:


    flask run

Usage

    Home Page: Browse products and filter them by category.
    Product Details: View detailed information about a product, including stock and price.
    Add to Cart: Add items to the cart from the product page.
    Checkout: Proceed to checkout and complete the purchase using Stripe.
    Order Confirmation: After successful payment, the order is saved in the database, and a confirmation page is displayed.

Routes

    /signup: User registration page.
    /login: User login page.
    /logout: Logs out the user and redirects to the home page.
    /cart: Displays items in the user's cart.
    /checkout: Checkout page with payment integration.
    /create-checkout-session: Creates a Stripe checkout session and redirects the user to the payment page.
    /payment-success: Handles successful payments.
    /payment-cancel: Handles canceled payments.


