import smtplib
import requests
import lxml
from bs4 import BeautifulSoup

YOUR_EMAIL = "YOUR_EMAIL"
YOUR_PASSWORD = "YOUR_PASSWORD"

url = "https://www.amazon.com/Samsung-Wireless-Cancelling-Charging-Included/dp/B08MWZHHKP/ref=sr_1_11?dchild=1&qid" \
      "=1613433217&s=electronics&sr=1-11"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.152 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(id="priceblock_ourprice").get_text()
print(price)
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
