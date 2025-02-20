import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Get email credentials from environment variables
my_email=os.getenv("my_email")
password=os.getenv("password")


URL="https://appbrewery.github.io/instant_pot/"
response=requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
o_price=soup.find(class_="a-offscreen")
price=float(o_price.text.split("$")[1])

#get product title
title=soup.find(id="productTitle").getText().strip()
message=f"{title} is now available at ${price}!"
email_body=f"Subject:Price drop alert!\n\n {message}".encode("utf-8")

if price<100:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()  # provides security so no interprets the message#
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=email_body)
        connection.close()

