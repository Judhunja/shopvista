#!/usr/bin/python3
""" This module contains a functions populate_commodities """
from ..app import db
from ..app.models import Commodity


def populate_commodities():
    """ Adds sample data to Commodity database to view some of the things for sale """
    commodities = [
        Commodity(name="Laptop",
                  description="A powerful laptop for all your needs, be it programming or even designing your favourite engineering projects.",
                  price=999.99, image_url="https://www.pexels.com/photo/macbook-pro-near-iphone-and-apple-fruit-18105/", category="Electronics"),
        Commodity(name="Coffee Maker",
                  description="Brew your favorite coffee every morning without any hustle with our coffee maker premium.",
                  price=49.99, image_url="https://www.pexels.com/photo/coffee-machine-near-a-stove-in-the-kitchen-5825347/", category="Home Appliances"),
        Commodity(name="Running Shoes",
                  description="Comfortable and durable running shoes for your marathons and workouts.",
                  price=79.99, image_url="https://www.pexels.com/photo/three-unpaired-red-gray-and-blue-horsebit-loafers-267320/", category="Footwear"),
        Commodity(name="JBL headphones",
                  description="Noise-cancelling headphones for immersive sound and comfort",
                  price=199.99, image_url="https://www.pexels.com/photo/black-corded-headset-205926/", category="Electronics"),
        Commodity(name="Tecno smartphone",
                  description="Latest smartphone from China Tecno with superb cutting-edge features.",
                  price=699.99, image_url="https://pixabay.com/vectors/mobile-phone-mobile-phone-2198770/", category="Electronics"),
    ]

    db.session.bulk_save_objects(commodities)
    db.session.commit()


if __name__ == "__main__":
    print("adding test data to table commodities")
    populate_commodities()
    print("Database populated with example commodities.")
