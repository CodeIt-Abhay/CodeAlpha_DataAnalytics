# 📘 CodeAlpha Internship Project - Task 1 (Improved)
# ✅ Multi-page Amazon Web Scraper
# 🧑 Author: Your Name

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Search keyword (you can change this)
query = "laptop".replace(" ", "+")
base_url = "https://www.amazon.in/s"

# Store scraped data
all_products = []

# 🔁 Scrape first 5 pages
for page in range(1, 6):
    print(f"Scraping page {page}...")
    params = {"k": query, "page": page}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9"
    }
    response = requests.get(base_url, params=params, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all product blocks
    items = soup.find_all("div", {"data-component-type": "s-search-result"})

    for item in items:
        name_tag = item.h2
        price_tag = item.find("span", "a-price-whole")
        rating_tag = item.find("span", class_="a-icon-alt")

        if name_tag:
            name = name_tag.text.strip()
        else:
            continue  # skip if no product name

        price = price_tag.text.replace(",", "") if price_tag else "N/A"
        rating = rating_tag.text if rating_tag else "N/A"

        all_products.append({
            "Product Name": name,
            "Price": price,
            "Rating": rating
        })

    time.sleep(1)  # avoid overloading server

# 📊 Convert to DataFrame
df = pd.DataFrame(all_products)

# 🧹 Clean minimal issues
df.drop_duplicates(subset="Product Name", inplace=True)
df.to_csv("amazon_products.csv", index=False)

print(f"✅ Scraping done! {len(df)} products saved to amazon_products.csv")
