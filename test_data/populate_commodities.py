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
    ]

    db.session.bulk_save_objects(commodities)
    db.session.commit()


if __name__ == "__main__":
    print("adding test data to table commodities")
    app = create_app()
    with app.app_context():
        populate_commodities()
    print("Database populated with example commodities.")
