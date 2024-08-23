#!/usr/bin/python3
""" This module contains a functions populate_commodities """
from app import db, create_app
from app.models import Commodity


def populate_commodities():
    """ Adds sample data to Commodity database to view some of the things for sale """
    commodities = [
        Commodity(name="Laptop",
                  description="A powerful laptop for all your needs, be it programming or even designing your favourite engineering projects.",
                  price=999.99, image_url="https://images.pexels.com/photos/18105/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1/", category="Electronics"),
        Commodity(name="Coffee Maker",
                  description="Brew your favorite coffee every morning without any hustle with our coffee maker premium.",
                  price=49.99, image_url="https://images.pexels.com/photos/5825347/pexels-photo-5825347.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1/", category="Home Appliances"),
        Commodity(name="Running shoes",
                  description="Comfortable and durable running shoes for your marathons and workouts.",
                  price=89.99, image_url="https://images.pexels.com/photos/2529148/pexels-photo-2529148.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1/", category="Footwear"),
        Commodity(name="Loafers",
                  description="Comfortable and stylish shoes for your formal wear.",
                  price=79.99, image_url="https://images.pexels.com/photos/267320/pexels-photo-267320.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1/", category="Footwear"),
        Commodity(name="JBL headphones",
                  description="Noise-cancelling headphones for immersive sound and comfort",
                  price=199.99, image_url="https://images.pexels.com/photos/205926/pexels-photo-205926.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1/", category="Electronics"),
        Commodity(name="Tecno smartphone",
                  description="Latest smartphone from China Tecno with superb cutting-edge features.",
                  price=699.99, image_url="https://images.pexels.com/photos/2643698/pexels-photo-2643698.jpeg?auto=compress&cs=tinysrgb&w=600/", category="Electronics"),
        Commodity(name="Chair",
                  description="Ergonomic chair for office and home.", price=149.99, image_url="https://images.pexels.com/photos/1957477/pexels-photo-1957477.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Furniture"),
        Commodity(name="Bluetooth Speaker",
                  description="Portable speaker with high-quality sound.", price=59.99, image_url="https://images.pexels.com/photos/9767549/pexels-photo-9767549.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Electronics"),
        Commodity(name="Electric Kettle",
                  description="Fast boiling electric kettle.", price=29.99, image_url="https://images.pexels.com/photos/1921673/pexels-photo-1921673.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Home Appliances"),
        Commodity(name="Gaming Mouse",
                  description="Precision mouse for gamers.", price=39.99, image_url="https://images.pexels.com/photos/2115256/pexels-photo-2115256.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Electronics"),
        Commodity(name="Yoga Mat",
                  description="Non-slip mat for yoga and exercise.", price=19.99, image_url="https://images.pexels.com/photos/8437013/pexels-photo-8437013.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Fitness"),
        Commodity(name="Smartwatch",
                  description="Track your fitness and notifications.", price=129.99, image_url="https://images.pexels.com/photos/2861929/pexels-photo-2861929.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Electronics"),
        Commodity(name="Fryer",
                  description="Healthy cooking with less oil.", price=89.99, image_url="https://images.pexels.com/photos/8879638/pexels-photo-8879638.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Home Appliances"),
        Commodity(name="Vacuum Cleaner",
                  description="Powerful vacuum for a clean home.", price=199.99, image_url="https://images.pexels.com/photos/38325/vacuum-cleaner-carpet-cleaner-housework-housekeeping-38325.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Home Appliances"),
        Commodity(name="Table Lamp",
                  description="Stylish lamp for your desk.", price=24.99, image_url="https://images.pexels.com/photos/5094567/pexels-photo-5094567.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Furniture"),
        Commodity(name="Toothbrush",
                  description="Cleaning your teeth.", price=49.99, image_url="https://images.pexels.com/photos/7055269/pexels-photo-7055269.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Personal Care"),
        Commodity(name="Phone charger",
                  description="Keep your phone charged always.", price=34.99, image_url="https://images.pexels.com/photos/4097207/pexels-photo-4097207.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Electronics"),
        Commodity(name="Water Bottle",
                  description="Insulated bottle to keep your drinks cold.", price=19.99, image_url="https://images.pexels.com/photos/4000090/pexels-photo-4000090.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Fitness"),
        Commodity(name="Backpack",
                  description="Durable backpack for daily use.", price=69.99, image_url="https://images.pexels.com/photos/2905238/pexels-photo-2905238.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Accessories"),
        Commodity(name="Sunglasses",
                  description="Protect your eyes with style.", price=89.99, image_url="https://images.pexels.com/photos/701877/pexels-photo-701877.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Accessories"),
        Commodity(name="Wristwatch",
                  description="Classic wristwatch with leather strap.", price=149.99, image_url="https://images.pexels.com/photos/1228517/pexels-photo-1228517.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Accessories"),
        Commodity(name="Gaming Console",
                  description="Old school gaming console.", price=499.99, image_url="https://images.pexels.com/photos/4219892/pexels-photo-4219892.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Electronics"),
        Commodity(name="Blender",
                  description="High-speed blender for smoothies.", price=79.99, image_url="https://images.pexels.com/photos/16969212/pexels-photo-16969212/free-photo-of-blender-standing-on-lawn.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Home Appliances"),
        Commodity(name="Earbuds",
                  description="Compact and powerful earbuds.", price=99.99, image_url="https://images.pexels.com/photos/3780681/pexels-photo-3780681.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Electronics"),
        Commodity(name="Camera",
                  description="Capture and print photos instantly.", price=69.99, image_url="https://images.pexels.com/photos/51383/photo-camera-subject-photographer-51383.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Photography"),
        Commodity(name="Cookware Set",
                  description="Non-stick cookware for all your meals.", price=129.99, image_url="https://images.pexels.com/photos/12156176/pexels-photo-12156176.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Kitchen"),
        Commodity(name="Electric Grill",
                  description="Indoor grill for healthy cooking.", price=89.99, image_url="https://images.pexels.com/photos/18093593/pexels-photo-18093593/free-photo-of-grill-in-yard.jpeg?auto=compress&cs=tinysrgb&w=300/", category="Home Appliances"),]

    db.session.bulk_save_objects(commodities)
    db.session.commit()


if __name__ == "__main__":
    print("adding test data to table commodities")
    app = create_app()
    with app.app_context():
        populate_commodities()
    print("Database populated with example commodities.")
