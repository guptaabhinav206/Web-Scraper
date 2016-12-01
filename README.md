# Web-Scraper

A simple web-scraper to get the first 10 products url's and start crawling the relevant data for those products. 
I have tried to incorporate minimal use of existing sources. I have used regular expressions and lxml library to scrap the data. 

Product attributes fetched :

1. Product Name
2. Product ID
3. Product Category
4. Product Thumbnail
5. Product Selling price
6. Product discount
7. Product URL
8. Product Availablity at Pin code
9. Product Estimated delivery time at Pin code


Sample url.json


    {
            "url": [
                    [
                            "http://www.shopclues.com/phillps-lcd-18.5-193v5lsb23-94.html"
                    ]
            ]
    }
    
    

Sample product.json


    {
            "CATEGORY": "Monitors", 
            "DISCOUNT": "Rs. 901", 
            "EST DELIVERY": {
                "575001": [
                    "Tue 13 Dec", 
                    "Fri 9 Dec"
                ], 
                "560070": [
                    "Tue 13 Dec", 
                    "Fri 9 Dec"
                ], 
                "671551": [
                    "Fri 16 Dec", 
                    "Mon 12 Dec"
                ]
            }, 
            "NAME": "Phillps LCD 18.5 193V5LSB23/94", 
            "SELLING_PRICE": "5099.00", 
            "URL": "http://www.shopclues.com/phillps-lcd-18.5-193v5lsb23-94.html", 
            "AVAILABILITY": [
                [
                    560070, 
                    1
                ], 
                [
                    575001, 
                    1
                ], 
                [
                    671551, 
                    1
                ]
            ], 
            "THUMBNAIL": "http://cdn02.shopclues.net/images/thumbnails/16771/160/160/193V5LSB294RTPglobal0011430486062.jpg", 
            "PRODUCT_ID": "76773178"
        }




# Requirements

    1. Python 2.7
    2. Works on Linux Distros

# Get the sources:

    git clone https://github.com/guptaabhinav206/Web-Scraper.git


# Setup

a. Automate:

    1. chmod +x setup.sh
    2. source setup.sh

b. Manual

    1. Intall pip(`sudo apt-get/yum install pip`).

    2. Install virtualenv(`sudo apt-get/yum install virtualenv`).

    3. Create virtualenv and activate it(`virtualenv env && source env/bin/activate`).

    4. Install required packages(`pip install -r requirements.txt`).


# Execute 

    python app.py 

